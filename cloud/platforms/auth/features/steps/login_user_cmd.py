import pickle
import uuid
from datetime import UTC, datetime

from behave import *
from features.environment import get_new_db_engine, get_new_db_session
from sqlalchemy import create_engine, select

from app.auth import crypto
from app.auth.models import User
from app.auth.schemas import TokenPairSchema
from app.common import database as database_module
from app.settings import config


@step("a valid request to login a user")
def step_impl(context):
    context.request = {
        "url": "/auth/Login",
        "json": {
            "username": "admin@sibel.com",
            "password": "secretpass",
        },
    }


@step("the user trying to login exists")
def step_impl(context):
    username = context.request["json"]["username"]
    password = context.request["json"]["password"]
    context.user = User(
        id="73bdc86f-22a3-4047-b033-85ab1c4b0266",
        username=username,
        password=crypto.hash_password(password),
    )
    context.db.add(context.user)
    context.db.commit()
    context.db.refresh(context.user)


@when("the request is made to login a user")
def step_impl(context):
    context.response = context.client.post(**context.request)


@step("access and refresh tokens are provided")
def step_impl(context):
    assert TokenPairSchema.model_validate_json(context.response.content)


@step("the provided password is wrong")
def step_impl(context):
    context.request["json"]["password"] = "wrongpass"


@step("the provided password is empty")
def step_impl(context):
    context.request["json"]["password"] = ""


@step("the account logging in was locked")
def step_impl(context):
    username = context.request["json"]["username"]
    assert context.cache.get(f"{config.PROJECT_NAME}:{username}:account_blocked") is not None


@step("is the last available login attempt")
def step_impl(context):
    username = context.request["json"]["username"]
    for i in range(config.AUTHENTICATION_FAILURE_THRESHOLD):
        unique_identifier = uuid.uuid4()
        context.cache.set(
            f"{config.PROJECT_NAME}:{username}:authentication_attempt_fail:{unique_identifier}",
            datetime.now(UTC).timestamp(),
        )


@step("the account is locked")
def step_impl(context):
    username = context.request["json"]["username"]
    context.cache.set(f"{config.PROJECT_NAME}:{username}:account_blocked", pickle.dumps(True))
