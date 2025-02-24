import pickle
import uuid
from datetime import UTC, datetime

from behave import *
from common_schemas import AccessTokenClaims
from jwt import decode

from app.settings import config


@step("a valid request to logout")
def step_impl(context):
    context.password = "secretpass"
    context.request = {"url": "/auth/Logout", "json": {"password": context.password}}


@when("the request to logout is made")
def step_impl(context):
    context.response = context.client.post(**context.request)


@step("the password is not provided")
def step_impl(context):
    context.request["json"].pop("password")


@step("a wrong password is provided")
def step_impl(context):
    context.request["json"]["password"] = "wrongpass"


@step("the account logging out was locked")
def step_impl(context):
    username = context.username
    assert context.cache.get(f"{config.PROJECT_NAME}:{username}:account_blocked") is not None


@step("is the last available logout attempt")
def step_impl(context):
    username = context.username
    for i in range(config.AUTHENTICATION_FAILURE_THRESHOLD):
        unique_identifier = uuid.uuid4()
        context.cache.set(
            f"{config.PROJECT_NAME}:{username}:authentication_attempt_fail:{unique_identifier}",
            datetime.now(UTC).timestamp(),
        )


@step("the logout account is locked")
def step_impl(context):
    username = context.username
    context.cache.set(f"{config.PROJECT_NAME}:{username}:account_blocked", pickle.dumps(True))


@step("the token is blacklisted")
def step_impl(context):
    token = context.internal_token
    claims = AccessTokenClaims(
        **decode(
            token.split(" ")[1],
            config.JWT_VERIFYING_KEY,
            audience=config.JWT_AUDIENCE,
            algorithms=[config.JWT_ALGORITHM],
        )
    )
    assert context.cache.get(f"SHARED:AUTH:TOKEN-BLACKLIST:{claims.jti}") is not None
