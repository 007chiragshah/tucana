import asyncio
from contextlib import asynccontextmanager

import httpx
import sentry_sdk
from fastapi import Depends, FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, PlainTextResponse
from healthcheck import KafkaHealthcheckService
from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.httpx import HttpxIntegration
from sentry_sdk.integrations.starlette import StarletteIntegration
from starlette import status
from starlette.requests import Request

from src.audit.api import api as audit_trail_api
from src.auth.api import api as auth_api
from src.auth.dependencies import InternalAuthRequired
from src.bed.api import api as bed_api
from src.bed_group.api import api as bed_group_api
from src.common.exceptions import BaseValidationException
from src.common.schemas import ErrorsSchema
from src.config.api import api as config_api
from src.consumer import KafkaConsumerFactory, event_consumer
from src.device.api import api as device_api
from src.event_sourcing.publisher import KafkaProducerFactory
from src.health_check.api import api as health_check_api
from src.middleware import CorrelationIDMiddleware
from src.patient.api import api as patient_api
from src.settings import settings
from src.version.api import api as version_api

sentry_sdk.init(
    dsn=settings.SENTRY_DSN,
    traces_sample_rate=settings.SENTRY_TRACE_SAMPLE_RATE,
    debug=settings.DEBUG,
    environment=settings.ENVIRONMENT,
    release=settings.SIBEL_VERSION,
    profiles_sample_rate=settings.SENTRY_PROFILES_SAMPLE_RATE,
    integrations=[
        StarletteIntegration(),
        FastApiIntegration(),
        HttpxIntegration(),
    ],
)

PATIENT_TAG = "Patient"
BED_TAG = "Bed"
BED_GROUP_TAG = "BedGroup"
AUDIT_TRAIL_TAG = "AuditTrail"
DEVICE_TAG = "Device"
CONFIG_TAG = "Configuration"
AUTHENTICATION_TAG = "Authentication"

tags_metadata = [
    {
        "name": PATIENT_TAG,
        "description": (
            "This tag encompasses all endpoints related to "
            "managing patient information and resources. "
            "These APIs allow for the creation, retrieval, "
            "updating, and deletion of patient records, "
            "as well as other patient-related operations. "
            "Authentication is required for all endpoints "
            "under this tag to ensure secure access."
        ),
    },
    {
        "name": BED_TAG,
        "description": (
            "This tag groups all endpoints related to the "
            "management of bed resources. "
            "These APIs are designed to handle individual "
            "and bulk operations on beds. "
            "Authentication is enforced to ensure secure "
            "and authorized access."
        ),
    },
    {
        "name": BED_GROUP_TAG,
        "description": (
            "This tag encompasses all endpoints related to managing "
            "bed groups, which are collections of bed resources that "
            "can be grouped based on shared characteristics, purposes, "
            "or locations. These APIs allow for the creation, updating, "
            "deletion, and retrieval of bed groups, as well as operations "
            "to manage beds within these groups. Authentication is required"
            " for all endpoints under this tag to ensure secure and authorized "
            "access."
        ),
    },
    {
        "name": AUDIT_TRAIL_TAG,
        "description": (
            "This tag groups endpoints related to tracking and retrieving audit "
            "trails. Audit trails are records of actions or changes made to specific "
            "entities, providing a detailed log for accountability, debugging, and "
            "compliance purposes. Authentication is enforced to ensure secure access."
        ),
    },
    {
        "name": DEVICE_TAG,
        "description": (
            "This tag includes endpoints for managing and interacting with devices. "
            "Devices may represent hardware or software components that are associated "
            "with beds in the system. These APIs allow for retrieving, updating, and "
            "performing batch operations on devices, as well as fetching specific details like "
            "operational ranges. Authentication is required to ensure secure access. "
            "There are two types of devices, patient monitors (PM) and sensors. They can "
            "be tell apart by checking the `gatewayId` property. If it's `null` is a PM if "
            "not it's a sensors."
        ),
    },
    {
        "name": CONFIG_TAG,
        "description": (
            "This tag encompasses endpoints for retrieving and updating configuration settings "
            "within the system. Configurations may define system-wide parameters, operational "
            "preferences, or entity-specific settings. These APIs provide a centralized way to "
            "manage configurations, ensuring consistency and control. Authentication is required "
            "to secure access."
        ),
    },
    {
        "name": AUTHENTICATION_TAG,
        "description": (
            "This tag includes all endpoints related to user authentication and session "
            "management. These APIs provide tools for secure login, token management, "
            "and password updates, ensuring robust access control within the system. "
            "They are essential for managing user sessions and enforcing security protocols."
        ),
    },
]


@asynccontextmanager
async def app_lifespan(_: FastAPI):  # pylint: disable=W0621,W0613
    loop = asyncio.get_running_loop()
    producer_client = await KafkaProducerFactory()()
    consumer_client = await KafkaConsumerFactory()()
    await KafkaHealthcheckService().start()
    task = loop.create_task(KafkaHealthcheckService().watchdog(event_consumer, consumer_client))
    yield
    task.cancel()
    await producer_client.stop()
    await consumer_client.stop()


async def validation_error_handler(_: Request, exc: BaseValidationException):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder(ErrorsSchema(detail=[exc.error])),
    )


async def http_exception_handler(_: Request, exc: httpx.HTTPStatusError):
    if exc.response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=exc.response.json(),
        )
    if exc.response.status_code in [
        status.HTTP_401_UNAUTHORIZED,
        status.HTTP_403_FORBIDDEN,
    ]:
        return PlainTextResponse(status_code=exc.response.status_code)
    raise exc


def create_app() -> FastAPI:
    base_app = FastAPI(
        debug=settings.DEBUG,
        openapi_url=f"{settings.BASE_PATH}/openapi.json",
        docs_url=f"{settings.BASE_PATH}/docs",
        redoc_url=f"{settings.BASE_PATH}/redoc",
        swagger_ui_oauth2_redirect_url=f"{settings.BASE_PATH}/docs/oauth2-redirect",
        lifespan=app_lifespan,
        openapi_tags=tags_metadata,
    )
    base_app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_headers=["*"],
        allow_methods=["*"],
    )
    base_app.add_middleware(CorrelationIDMiddleware)
    base_app.add_exception_handler(BaseValidationException, validation_error_handler)
    base_app.add_exception_handler(httpx.HTTPStatusError, http_exception_handler)
    base_app.include_router(health_check_api, tags=["System"])
    base_app.include_router(health_check_api, prefix=settings.BASE_PATH, tags=["System"])
    base_app.include_router(version_api, prefix=settings.BASE_PATH, tags=["System"])
    base_app.include_router(auth_api, prefix=settings.BASE_PATH, tags=[AUTHENTICATION_TAG])
    base_app.include_router(
        patient_api,
        prefix=settings.BASE_PATH,
        dependencies=[Depends(InternalAuthRequired())],
        tags=[PATIENT_TAG],
    )
    base_app.include_router(
        bed_api,
        prefix=settings.BASE_PATH,
        dependencies=[Depends(InternalAuthRequired())],
        tags=[BED_TAG],
    )
    base_app.include_router(
        bed_group_api,
        prefix=settings.BASE_PATH,
        dependencies=[Depends(InternalAuthRequired())],
        tags=[BED_GROUP_TAG],
    )
    base_app.include_router(
        audit_trail_api,
        prefix=settings.BASE_PATH,
        dependencies=[Depends(InternalAuthRequired())],
        tags=[AUDIT_TRAIL_TAG],
    )
    base_app.include_router(
        device_api,
        prefix=settings.BASE_PATH,
        dependencies=[Depends(InternalAuthRequired())],
        tags=[DEVICE_TAG],
    )
    base_app.include_router(
        config_api,
        prefix=settings.BASE_PATH,
        dependencies=[Depends(InternalAuthRequired())],
        tags=[CONFIG_TAG],
    )
    return base_app


app = create_app()
