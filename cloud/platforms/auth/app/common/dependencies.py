from common_schemas import AccessTokenClaims
from common_schemas.jwt import RoleNames
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt import decode
from jwt.exceptions import (
    ExpiredSignatureError,
    InvalidSignatureError,
    InvalidTokenError,
)
from starlette import status
from starlette.requests import Request

from app.auth.services import token_is_blacklisted
from app.settings import config


class BlacklistedToken(RuntimeError):
    pass


class InternalAuthRequired:
    async def __call__(
        self,
        request: Request,
        auth_credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
    ) -> AccessTokenClaims:
        internal_token = auth_credentials.credentials
        public_key = config.JWT_VERIFYING_KEY
        try:
            claims = AccessTokenClaims(
                **decode(
                    internal_token,
                    public_key,
                    audience=config.JWT_AUDIENCE,
                    algorithms=[config.JWT_ALGORITHM],
                )
            )
            request.state.internal_token = internal_token
            request.state.internal_claims = claims
            request.state.username = claims.username
            if token_is_blacklisted(claims):
                raise BlacklistedToken()
        except (
            KeyError,
            ExpiredSignatureError,
            InvalidSignatureError,
            InvalidTokenError,
            BlacklistedToken,
        ) as exc:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED) from exc
        return claims


class UserHasRole:
    def __init__(self, roles: set[RoleNames]):
        self.required_roles = roles

    async def __call__(
        self, claims: AccessTokenClaims = Depends(InternalAuthRequired())
    ) -> AccessTokenClaims:
        for role in claims.roles:
            if role in self.required_roles:
                return claims
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
