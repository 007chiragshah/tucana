import asyncio
import random
from datetime import datetime, timedelta
from typing import Optional
from uuid import UUID

from cache import RedisCache
from common_schemas.jwt import AccessTokenClaims, RoleNames
from fastapi import HTTPException
from fastapi.params import Depends
from pydantic import SecretStr
from starlette import status

from app.auth import crypto, rate_limiting
from app.auth.events import (
    AddRoleToUserEvent,
    CreateUserEvent,
    FailedLoginAttemptEvent,
    FailedLogoutEvent,
    SuccessfulLoginEvent,
    SuccessfulLogoutEvent,
    UserAccountLockedEvent,
)
from app.auth.models import Role, User
from app.auth.repository import UserRepository
from app.auth.schemas import CreateUserSchema, TokenPairSchema, UserSchema
from app.auth.stream import UserEventStream
from app.common.event_sourcing.events import Event
from app.settings import config


def role_requires_password_to_logout(user_roles: list[RoleNames]) -> bool:
    return any(role in config.ROLES_REQUIRING_PASSWORD_FOR_LOGOUT for role in user_roles)


def user_account_is_blocked(username: str) -> bool:
    client = RedisCache()

    if not config.BRUTE_FORCE_PROTECTION_ENABLED or not client.connected:
        return False

    key = f"{config.PROJECT_NAME}:{username}:account_blocked"

    is_blocked = bool(client.get(key))

    return is_blocked


def get_backoff_delay(attempt: int) -> float:
    if config.AUTHENTICATION_FAILURE_BACKOFF_ENABLED:
        delay = min(15, 1 * (2 ** (attempt - 1)))
        jitter = random.uniform(0, delay / 2)
        return delay + jitter
    return 0


def blacklist_token(claims: AccessTokenClaims) -> None:
    if config.JWT_TOKEN_BLACKLIST_ENABLED:
        client = RedisCache().client
        if claims.has_expired():
            return
        key = f"SHARED:AUTH:TOKEN-BLACKLIST:{claims.jti}"
        client.set(name=key, value=claims.jti, ex=claims.remaining_duration())


def token_is_blacklisted(claims: AccessTokenClaims) -> bool:
    client = RedisCache().client
    key = f"SHARED:AUTH:TOKEN-BLACKLIST:{claims.jti}"
    return client.get(key) is not None


class UserService:
    def __init__(
        self,
        read_user_repository: UserRepository = Depends(),
        user_event_stream: UserEventStream = Depends(),
    ):
        self.read_user_repository = read_user_repository
        self.user_event_stream = user_event_stream

    async def get_roles_by_id(self) -> dict[UUID, Role]:
        roles = await self.read_user_repository.get_roles()
        return {r.id: r for r in roles}

    async def get_roles_by_name(self) -> dict[str, Role]:
        roles = await self.read_user_repository.get_roles()
        return {r.name: r for r in roles}

    async def get_user(self, username: str) -> Optional[UserSchema]:
        user = await self.read_user_repository.get_user_by_username(username)
        if not user:
            return None
        return UserSchema.model_validate(user)

    async def create_user(self, claims: AccessTokenClaims, payload: CreateUserSchema) -> UserSchema:
        roles_by_id = await self.get_roles_by_id()
        events = [CreateUserEvent(claims.username, payload.username, payload.password)]

        for role in payload.roles:
            found_role = roles_by_id[role.id]
            events.append(AddRoleToUserEvent(claims.username, found_role))

        user = None
        for event in events:
            user = await self.user_event_stream.add(event, user)
        return UserSchema.model_validate(user)

    async def _authentication_failed_penalization(self, user: User, event: Event):
        rate_limiting.add_failed_authentication_attempt(user.username)
        attempts_count = rate_limiting.get_failed_authentication_attempts_count(user.username)
        await self.user_event_stream.add(event, user)
        if attempts_count >= config.AUTHENTICATION_FAILURE_THRESHOLD:
            rate_limiting.block_account_temporarily(user.username)
            blocked_until = datetime.now() + timedelta(
                seconds=config.AUTHENTICATION_ACCOUNT_LOCKOUT_IN_SECONDS
            )
            account_locked_event = UserAccountLockedEvent(user.username, blocked_until)
            await self.user_event_stream.add(account_locked_event, user)
        await asyncio.sleep(get_backoff_delay(attempts_count))

    # TODO: Implement password rehashing
    async def login(self, username: str, password: SecretStr) -> Optional[TokenPairSchema]:
        user = await self.read_user_repository.get_user_by_username(username)

        if not user:
            return None

        if user_account_is_blocked(user.username):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

        passwords_match, _ = crypto.verify_password(password.get_secret_value(), user.password)
        if not passwords_match:
            event = FailedLoginAttemptEvent(user.username)
            await self._authentication_failed_penalization(user, event)
            return None

        event = SuccessfulLoginEvent(user.username)
        await self.user_event_stream.add(event, user)
        access_token = crypto.get_token(user, token_type="access")
        refresh_token = crypto.get_token(user, token_type="refresh")
        return TokenPairSchema(access=access_token, refresh=refresh_token)

    async def logout(self, claims: AccessTokenClaims, password: Optional[SecretStr]) -> bool:
        user = await self.read_user_repository.get_user_by_username(claims.username)
        if not user:
            return False

        if role_requires_password_to_logout(claims.roles):
            if user_account_is_blocked(user.username):
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

            if not password:
                event = FailedLogoutEvent(user.username)
                await self._authentication_failed_penalization(user, event)
                return False

            match, _ = crypto.verify_password(password.get_secret_value(), user.password)
            if not match:
                event = FailedLogoutEvent(user.username)
                await self._authentication_failed_penalization(user, event)
                return False

        event = SuccessfulLogoutEvent(user.username)
        await self.user_event_stream.add(event, user)
        blacklist_token(claims)
        return True
