from cache import add_cache, remove_cache
from fastapi import APIRouter, Depends
from starlette import status
from starlette.requests import Request

from app.common.schemas import ErrorsSchema
from app.config.schemas import (
    AppSettingResources,
    AppSettingSchema,
    BatchCreateOrUpdateAppSettingsSchema,
    CreateOrUpdateAppSettingSchema,
    SystemSettingsSchema,
)
from app.config.services import AppSettingsService, SystemSettingsService
from app.settings import config

api = APIRouter(prefix=config.BASE_PATH)


@api.get("/system-settings")
async def get_current_system_settings(
    service: SystemSettingsService = Depends(),
) -> SystemSettingsSchema:
    return await service.get_system_settings()


@api.post(
    "/app-settings",
    responses={
        status.HTTP_200_OK: {"model": AppSettingSchema},
        status.HTTP_401_UNAUTHORIZED: {"model": {}},
        status.HTTP_403_FORBIDDEN: {"model": {}},
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": ErrorsSchema},
    },
)
@remove_cache("AppSettings")
async def set_app_settings(
    payload: CreateOrUpdateAppSettingSchema,
    service: AppSettingsService = Depends(),
) -> AppSettingSchema:
    resources = await service.create_or_update_app_settings([payload])
    return resources.resources[0]


@api.post(
    "/app-settings/batch",
    responses={
        status.HTTP_200_OK: {"model": AppSettingResources},
        status.HTTP_401_UNAUTHORIZED: {"model": {}},
        status.HTTP_403_FORBIDDEN: {"model": {}},
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": ErrorsSchema},
    },
)
async def batch_create_app_settings(
    payload: BatchCreateOrUpdateAppSettingsSchema,
    service: AppSettingsService = Depends(),
) -> AppSettingResources:
    return await service.create_or_update_app_settings(payload.settings)


@api.get(
    "/app-settings",
    responses={
        status.HTTP_200_OK: {"model": AppSettingResources},
        status.HTTP_401_UNAUTHORIZED: {"model": {}},
        status.HTTP_403_FORBIDDEN: {"model": {}},
    },
)
@add_cache("AppSettings")
async def get_app_settings(
    request: Request,  # pylint: disable=unused-argument
    service: AppSettingsService = Depends(),
) -> AppSettingResources:
    return await service.get_all_settings()
