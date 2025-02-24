from common_schemas import AccessTokenClaims
from common_schemas.jwt import RoleNames
from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from starlette.responses import Response

from app.auth.schemas import (
    CreateUserSchema,
    LoginSchema,
    LogoutSchema,
    TokenPairSchema,
    UserSchema,
)
from app.auth.services import UserService
from app.common.dependencies import InternalAuthRequired, UserHasRole
from app.common.schemas import ErrorsSchema
from app.settings import config

api = APIRouter(prefix=config.BASE_PATH)


@api.post(
    "/CreateUser",
    operation_id="auth-create-user-cmd",
    responses={
        status.HTTP_200_OK: {"model": UserSchema},
        status.HTTP_401_UNAUTHORIZED: {"model": {}},
        status.HTTP_403_FORBIDDEN: {"model": {}},
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": ErrorsSchema},
    },
    description="Create a new user with required roles.",
)
async def create_user_command(
    payload: CreateUserSchema,
    service: UserService = Depends(),
    claims: AccessTokenClaims = Depends(UserHasRole({RoleNames.ADMIN})),
) -> UserSchema:
    user = await service.create_user(claims, payload)
    return user


@api.post(
    "/Login",
    operation_id="auth-login-cmd",
    responses={
        status.HTTP_200_OK: {"model": UserSchema},
        status.HTTP_401_UNAUTHORIZED: {"model": {}},
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": ErrorsSchema},
    },
    description="Login a user.",
)
async def login_command(
    payload: LoginSchema,
    service: UserService = Depends(),
) -> TokenPairSchema:
    token_schema = await service.login(payload.username, payload.password)
    if not token_schema:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return token_schema


@api.post(
    "/Logout",
    operation_id="auth-logout-cmd",
    responses={
        status.HTTP_204_NO_CONTENT: {"model": {}},
        status.HTTP_401_UNAUTHORIZED: {"model": {}},
    },
    description="Logouts a user.",
)
async def logout_command(
    payload: LogoutSchema,
    service: UserService = Depends(),
    claims: AccessTokenClaims = Depends(InternalAuthRequired()),
) -> Response:
    success = await service.logout(claims, payload.password)
    if not success:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
