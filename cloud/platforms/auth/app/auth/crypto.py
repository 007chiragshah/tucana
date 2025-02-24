import secrets
from datetime import UTC, datetime, timedelta
from typing import Literal

import argon2
import jwt
from common_schemas.jwt import AccessTokenClaims, RefreshTokenClaims, RoleNames

from app.auth.models import User
from app.settings import config

ph = argon2.PasswordHasher()


def hash_password(password: str) -> str:
    return ph.hash(password)


def verify_password(password: str, hashed_password: str) -> tuple[bool, bool]:
    try:
        ph.verify(hashed_password, password)
        match = True
    except argon2.exceptions.VerifyMismatchError:
        match = False
    return match, ph.check_needs_rehash(hashed_password)


def get_token(user: User, token_type: Literal["access", "refresh"]) -> str:
    iat = datetime.now(UTC)
    claims = {
        "iat": iat.timestamp(),
        "sub": str(user.id),
        "nbf": iat.timestamp(),
        "roles": [RoleNames(role.name) for role in user.roles],
        "username": user.username,
        "jti": secrets.token_urlsafe(8),
        "aud": config.JWT_AUDIENCE,
        "iss": config.JWT_ISSUER,
    }
    if token_type == "access":
        claims["exp"] = (
            iat + timedelta(minutes=config.JWT_ACCESS_TOKEN_DURATION_MINUTES)
        ).timestamp()
        claims = AccessTokenClaims(**claims).model_dump()
    elif token_type == "refresh":
        claims["exp"] = (
            iat + timedelta(minutes=config.JWT_REFRESH_TOKEN_DURATION_MINUTES)
        ).timestamp()
        claims = RefreshTokenClaims(**claims).model_dump()
    encoded_jwt = jwt.encode(
        payload=claims, key=config.JWT_SIGNING_KEY, algorithm=config.JWT_ALGORITHM
    )
    return encoded_jwt
