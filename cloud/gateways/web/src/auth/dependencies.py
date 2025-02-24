from typing import Any, Dict

from common_schemas import AccessTokenClaims
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt import decode
from jwt.exceptions import (
    ExpiredSignatureError,
    InvalidSignatureError,
    InvalidTokenError,
)
from pydantic import ValidationError
from starlette import status
from starlette.requests import Request

from src.settings import settings


class GetAuthenticationCredentials:
    async def __call__(
        self,
        request: Request,
        auth_credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer(auto_error=False)),
    ) -> str:
        cookie_token = request.cookies.get("sibel-sc-session", "").strip()
        if not cookie_token and not auth_credentials:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
        return cookie_token if cookie_token else auth_credentials.credentials


class InternalAuthRequired:
    async def __call__(
        self,
        request: Request,
        internal_token: str = Depends(GetAuthenticationCredentials()),
    ) -> Dict[str, Any]:
        public_key = settings.JWT_VERIFYING_KEY
        try:
            raw_claims = decode(internal_token, public_key, audience="tucana", algorithms=["RS256"])
            claims = AccessTokenClaims(**raw_claims).model_dump()
            request.state.internal_token = internal_token
            request.state.internal_claims = claims
            request.state.username = claims["user_id"]
        except (
            ValidationError,
            KeyError,
            ExpiredSignatureError,
            InvalidSignatureError,
            InvalidTokenError,
        ) as exc:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED) from exc
        return claims


class PasswordRequired:
    async def __call__(
        self,
        request: Request,
    ) -> Dict[str, Any]:
        body = await request.json()
        request.state.username = settings.DEFAULT_CLINICAL_USERNAME
        return body


class TechnicalPasswordRequired:
    async def __call__(
        self,
        request: Request,
    ) -> Dict[str, Any]:
        body = await request.json()
        request.state.username = settings.DEFAULT_TECHNICAL_USER_USERNAME
        return body
