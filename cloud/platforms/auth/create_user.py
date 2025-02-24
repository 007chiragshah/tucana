import argparse
import asyncio
import secrets
from datetime import UTC, datetime, timedelta

from common_schemas.jwt import AccessTokenClaims, RoleNames
from loguru import logger
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.repository import UserRepository
from app.auth.schemas import CreateUserSchema, RoleSchema
from app.auth.services import UserService
from app.auth.stream import UserEventStream
from app.common.database import session_maker
from app.settings import config


def get_system_claims() -> AccessTokenClaims:
    iat = datetime.now(UTC)
    return AccessTokenClaims(
        iat=iat.timestamp(),
        sub="system",
        nbf=iat.timestamp(),
        exp=(iat + timedelta(minutes=config.JWT_ACCESS_TOKEN_DURATION_MINUTES)).timestamp(),
        username="system",
        roles=[RoleNames.ADMIN],
        jti=secrets.token_urlsafe(8),
        aud=config.JWT_AUDIENCE,
        iss=config.JWT_ISSUER,
    )


async def create_user(session: AsyncSession, username: str, password: str, roles: str):
    user_service = UserService(
        read_user_repository=UserRepository(session),
        user_event_stream=UserEventStream(session),
    )
    roles_by_name = await user_service.get_roles_by_name()
    found_roles = [RoleSchema(id=roles_by_name[r.strip()].id) for r in roles.split(",")]
    payload = CreateUserSchema(
        username=username,
        password=password,
        roles=found_roles,
    )
    adapted_claims = get_system_claims()

    user = await user_service.get_user(payload.username)
    if not user:
        logger.info(f"Creating new user: {payload.username}, with roles: {roles}")
        await user_service.create_user(adapted_claims, payload)
    else:
        logger.info(f"User already exists: {user.username}, with roles: {user.roles}")


class DatabaseAdapter:
    def __init__(self, f):
        self.f = f

    async def __call__(self, username: str, password: str, roles: str) -> None:
        async with session_maker() as db_session, db_session.begin():
            await self.f(db_session, username, password, roles)
            await db_session.commit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process user details.")
    parser.add_argument("--username", required=True, help="The username of the user.")
    parser.add_argument("--password", required=True, help="The password of the user.")
    parser.add_argument("--roles", required=True, help="Comma-separated list of roles.")

    args = parser.parse_args()
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            DatabaseAdapter(create_user)(args.username, args.password, args.roles)
        )
    except KeyError as err:
        logger.error(f"Role doesn't exist: {err.args}")
        exit(1)
    except ValidationError as err:
        logger.exception(err)
        exit(1)
    finally:
        exit(0)
