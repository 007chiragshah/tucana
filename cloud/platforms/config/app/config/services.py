from typing import List

from fastapi import Depends
from starlette.requests import Request

from app.common import kafka_admin
from app.config.events import (
    CreateAppSettingsEvent,
    UpdateAppSettingsEvent,
    UpdateSystemSettingsEvent,
)
from app.config.models import SystemSettings
from app.config.repository import ReadAppSettingsRepository, ReadSystemSettingsRepository
from app.config.schemas import (
    AppSettingResources,
    AppSettingSchema,
    CreateOrUpdateAppSettingSchema,
    SystemSettingsPayload,
    SystemSettingsSchema,
)
from app.config.stream import AppSettingsEventStream, SystemSettingsEventStream
from app.settings import config


class SystemSettingsService:
    def __init__(
        self,
        request: Request,
        event_stream: SystemSettingsEventStream = Depends(),
        read_system_settings_repository: ReadSystemSettingsRepository = Depends(),
    ):
        self.username = request.state.username
        self.event_stream = event_stream
        self.read_system_settings_repository = read_system_settings_repository

    async def _get_system_settings(self) -> SystemSettings:
        return await self.read_system_settings_repository.get()

    async def get_system_settings(self) -> SystemSettingsSchema:
        current_settings = await self._get_system_settings()
        return SystemSettingsSchema.model_validate(current_settings)

    async def update_system_settings(self, payload: SystemSettingsPayload) -> SystemSettings:
        current_settings = await self._get_system_settings()

        if payload.patient_vitals_retention_time_changed(
            current_settings.patient_vitals_retention_period_ms
        ):
            kafka_admin.change_topic_retention(
                config.PATIENT_VITALS_KAFKA_TOPIC_NAME, payload.patient_vitals_retention_period_ms
            )

        event = UpdateSystemSettingsEvent(self.username, payload)
        await self.event_stream.add(event, current_settings)


class AppSettingsService:
    def __init__(
        self,
        request: Request,
        event_stream: AppSettingsEventStream = Depends(),
        repository: ReadAppSettingsRepository = Depends(),
    ):
        self.username = request.state.username
        self.event_stream = event_stream
        self.repository = repository

    async def create_or_update_app_settings(
        self, settings: List[CreateOrUpdateAppSettingSchema]
    ) -> AppSettingResources:
        existing_settings = await self.repository.get_settings_by_key(
            keys=[setting.key for setting in settings]
        )
        existing_settings_by_key = {setting.key: setting for setting in existing_settings}

        events = []
        for new_setting in settings:
            if new_setting.key not in existing_settings_by_key:
                event = CreateAppSettingsEvent(self.username, new_setting)
            else:
                event = UpdateAppSettingsEvent(self.username, new_setting)
            events.append((event, existing_settings_by_key.get(new_setting.key)))

        processed_settings = await self.event_stream.batch_add(events)

        return AppSettingResources.model_construct(
            resources=[AppSettingSchema.model_validate(settings) for settings in processed_settings]
        )

    async def get_all_settings(self) -> AppSettingResources:
        settings = await self.repository.get_all_settings()
        return AppSettingResources.model_construct(
            resources=[AppSettingSchema.model_validate(settings) for settings in settings]
        )
