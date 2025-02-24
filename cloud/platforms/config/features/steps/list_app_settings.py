import uuid

from behave import *

from app.config.models import AppSetting

use_step_matcher("re")


@step("multiple app settings exist")
def step_impl(context):
    for row in context.table:
        setting = AppSetting(id=uuid.uuid4(), key=row["key"], value=row["value"])
        context.db.add(setting)

    context.db.commit()


@step("a request to list all settings")
def step_impl(context):
    context.request = {
        "method": "GET",
        "url": "/config/app-settings",
    }


@step("the list of all settings is returned")
def step_impl(context):
    response_json = context.response.json()
    actual_settings = {setting["key"]: setting["value"] for setting in response_json["resources"]}
    expected_settings = {row["key"]: row["value"] for row in context.table}
    assert expected_settings == actual_settings
