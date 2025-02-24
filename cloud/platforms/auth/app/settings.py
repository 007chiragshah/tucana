from typing import Annotated

import argon2
from common_schemas import Base64String, SecretString
from common_schemas.jwt import RoleNames
from pydantic import AfterValidator
from pydantic_settings import BaseSettings, SettingsConfigDict

AvailableRoleNames = Annotated[
    str, AfterValidator(lambda v: [RoleNames(x.strip()) for x in v.split(",") if x])
]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Environment config
    DEBUG: bool = False
    LOGURU_LEVEL: str = "ERROR"
    GUNICORN_WORKERS: int = 3
    ENVIRONMENT: str
    APPLICATION_PORT: int = 80
    BASE_PATH: str
    PUBLISHER_BACKEND: str = "app.common.event_sourcing.publisher.KafkaPublisher"
    SIBEL_VERSION: str
    SYSTEM_USERNAME: str = "system"
    CONFIG_PUBLISHER_AUDIT_TRAIL_STREAM_NAME: str = "events-auth"

    # Sentry config
    SENTRY_DSN: str
    SENTRY_TRACE_SAMPLE_RATE: float = 0.1
    SENTRY_PROFILES_SAMPLE_RATE: float = 0.1

    # Database config
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USERNAME: SecretString
    DB_PASSWORD: SecretString

    # Kafka config
    KAFKA_HOST: str
    KAFKA_PORT: str
    KAFKA_PASSWORD: SecretString
    KAFKA_CLIENT_ID: str = "auth-ms"
    KAFKA_CA_FILE_PATH: str
    KAFKA_CERT_FILE_PATH: str
    KAFKA_KEY_FILE_PATH: str
    KAFKA_RETRY_BACKOFF: int = 2000
    KAFKA_METADATA_MAX_AGE: int = 300000

    # Redis config
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_USERNAME: SecretString
    REDIS_PASSWORD: SecretString
    REDIS_CACHE_TTL: int
    CACHE_ENABLED: bool = True
    PROJECT_NAME: str = "auth"

    # JWT
    JWT_ISSUER: str = "auth"
    JWT_SIGNING_KEY: Base64String
    JWT_VERIFYING_KEY: Base64String
    JWT_AUDIENCE: str = "tucana"
    JWT_ACCESS_TOKEN_DURATION_MINUTES: int = 10_080  # 1 week
    JWT_REFRESH_TOKEN_DURATION_MINUTES: int = 43_800  # 1 month
    JWT_ALGORITHM: str = "RS256"

    # Healthcheck
    KAFKA_HEALTHCHECK_TOPIC: str

    # User password requirements
    USER_PASSWORD_MINIMUM_LENGTH: int = 8
    USER_PASSWORD_REQUIRE_NUMBERS: bool = False
    USER_PASSWORD_REQUIRE_LOWERCASE: bool = False
    USER_PASSWORD_REQUIRE_UPPERCASE: bool = False
    USER_PASSWORD_REQUIRE_SPECIAL_CHARS: bool = False

    # password hashing params
    HASHING_ALGORITHM_RANDOM_SALT_LENGTH: int = argon2.DEFAULT_RANDOM_SALT_LENGTH
    HASHING_ALGORITHM_HASH_LENGTH: int = argon2.DEFAULT_HASH_LENGTH
    HASHING_ALGORITHM_TIME_COST: int = argon2.DEFAULT_TIME_COST
    HASHING_ALGORITHM_MEMORY_COST: int = argon2.DEFAULT_MEMORY_COST
    HASHING_ALGORITHM_PARALLELISM: int = argon2.DEFAULT_PARALLELISM

    # app config
    ROLES_REQUIRING_PASSWORD_FOR_LOGOUT: AvailableRoleNames = RoleNames.CLINICAL.value
    BRUTE_FORCE_PROTECTION_ENABLED: bool = True
    BRUTE_FORCE_ATTEMPT_TTL_SECONDS: int = 900
    AUTHENTICATION_ACCOUNT_LOCKOUT_IN_SECONDS: int = 900
    AUTHENTICATION_FAILURE_THRESHOLD: int = 5
    AUTHENTICATION_FAILURE_BACKOFF_ENABLED: bool = False
    JWT_TOKEN_BLACKLIST_ENABLED: bool = True


config = Settings()
