from fastapi import APIRouter
from pydantic import BaseModel

from src.settings import settings

api = APIRouter()


class VersionResponse(BaseModel):
    version: str


@api.get(
    "/version",
    summary="Get the application version",
    description="Returns the current version of the application as configured in the settings.",
)
async def get_app_version_api() -> VersionResponse:
    return VersionResponse(version=settings.SIBEL_VERSION)
