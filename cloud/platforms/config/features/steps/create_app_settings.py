import uuid

from behave import *
from sqlalchemy import select

from app.config.models import AppSetting


@step('a request to add an app setting with key "{key}" and value "{value}"')
def step_impl(context, key, value):
    context.request = {
        "method": "POST",
        "url": "/config/app-settings",
        "json": {"key": key, "value": value},
    }


@step('an app setting with key "{key}" and value "{value}" exists')
def step_impl(context, key, value):
    setting = AppSetting(id=uuid.uuid4(), key=key, value=value)
    context.db.add(setting)
    context.db.commit()


@step('the app setting with key "{key}" is updated to "{value}"')
def step_impl(context, key, value):
    stmt = select(AppSetting)
    setting_list = context.db.execute(stmt).scalars().all()
    existing_settings = {setting.key: setting.value for setting in setting_list}
    assert existing_settings[key] == value
