import respx
from behave import *

from features.steps.common import generate_valid_jwt_token
from src.settings import settings


@step("a valid request to start a user session")
def step_impl(context):
    context.request = {
        "url": "/web/auth/session",
        "json": {
            "username": "user@sibel.com",
            "password": "secretpass",
        },
    }
    context.expected_token = generate_valid_jwt_token(context).split(" ")[1]
    respx.mock.request("POST", f"{settings.AUTH_PLATFORM_V2_BASE_URL}/Login").respond(
        status_code=200,
        json={
            "token": context.expected_token,
        },
    )


@when("the request to start a user session is made")
def step_impl(context):
    context.response = context.client.post(**context.request)


@step("the response includes the new session")
def step_impl(context):
    assert context.response.cookies.get("sibel-sc-session") == context.expected_token
