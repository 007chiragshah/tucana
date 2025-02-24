from behave import *
from sqlalchemy import select

from app.config.models import AppSetting

use_step_matcher("re")


@step("a request to add multiple app settings")
def step_impl(context):
    settings = [{"key": row["key"], "value": row["value"]} for row in context.table]
    context.request = {
        "method": "POST",
        "url": "/config/app-settings/batch",
        "json": {"settings": settings},
    }


@step("app settings are updated")
def step_impl(context):
    stmt = select(AppSetting)
    setting_list = context.db.execute(stmt).scalars().all()
    existing_settings = {setting.key: setting.value for setting in setting_list}
    expected_settings = {row["key"]: row["value"] for row in context.table}
    assert expected_settings.items() <= existing_settings.items()
