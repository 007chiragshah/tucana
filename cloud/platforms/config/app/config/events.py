import uuid
from typing import Any, Optional

from app.common.event_sourcing.events import Event
from app.config.models import AppSetting, SystemSettings
from app.config.schemas import CreateOrUpdateAppSettingSchema, SystemSettingsPayload


class UpdateSystemSettingsEvent(Event):
    display_name: str = "System settings updated"
    event_type: str = "SYSTEM_SETTINGS_UPDATED_EVENT"

    def __init__(self, username: str, settings: SystemSettingsPayload):
        super().__init__(username)
        self.settings = settings

    def process(self, entity: SystemSettings) -> SystemSettings:
        if self.settings.patient_vitals_retention_period_ms:
            entity.patient_vitals_retention_period_ms = (
                self.settings.patient_vitals_retention_period_ms
            )
        return entity


class CreateAppSettingsEvent(Event[AppSetting]):
    display_name: str = "App setting created"
    event_type: str = "APP_SETTING_CREATED_EVENT"

    def __init__(self, username: str, payload: CreateOrUpdateAppSettingSchema):
        super().__init__(username)
        self.payload = payload

    def process(self, entity: Optional[AppSetting] = None) -> AppSetting:
        return AppSetting(
            id=uuid.uuid4(),
            key=self.payload.key,
            value=self.payload.value,
        )

    def as_dict(self) -> dict[Any, Any]:
        return {
            "key": self.payload.key,
            "value": self.payload.value,
        }


class UpdateAppSettingsEvent(Event[AppSetting]):
    display_name: str = "App setting updated"
    event_type: str = "APP_SETTING_UPDATED_EVENT"

    def __init__(self, username: str, payload: CreateOrUpdateAppSettingSchema):
        super().__init__(username)
        self.payload = payload

    def process(self, entity: Optional[AppSetting]) -> AppSetting:
        entity.value = self.payload.value
        return entity

    def as_dict(self) -> dict[Any, Any]:
        return {
            "key": self.payload.key,
            "value": self.payload.value,
        }
