import abc
import enum
from datetime import UTC, datetime, timedelta
from typing import Literal

from pydantic import AliasChoices, BaseModel, Field, computed_field


class RoleNames(str, enum.Enum):
    ADMIN = "admin"
    TECH = "tech"
    CLINICAL = "clinical"
    ORGANIZATION = "organization"


class JWTClaims(BaseModel, abc.ABC):
    # default fields
    sub: str
    nbf: float
    exp: float
    iat: float
    jti: str
    aud: str
    iss: str

    # custom fields
    username: str = Field(validation_alias=AliasChoices("username", "user_id"))
    roles: list[RoleNames] = Field(
        default_factory=list, validation_alias=AliasChoices("roles", "groups")
    )

    @computed_field
    @property
    def user_id(self) -> str:
        """Kept for backward compatibility"""
        return self.username

    def has_expired(self) -> bool:
        return datetime.now(tz=UTC) >= datetime.fromtimestamp(self.exp, tz=UTC)

    def remaining_duration(self) -> timedelta:
        return datetime.fromtimestamp(self.exp, tz=UTC) - datetime.now(tz=UTC)


class AccessTokenClaims(JWTClaims):
    token_type: Literal["access"] = "access"


class RefreshTokenClaims(JWTClaims):
    token_type: Literal["refresh"] = "refresh"
