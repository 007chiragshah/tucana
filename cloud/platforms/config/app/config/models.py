import uuid

from sqlalchemy import Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.common.models import Entity


class SystemSettings(Entity):
    __tablename__ = "system_settings"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    patient_vitals_retention_period_ms: Mapped[int] = mapped_column(Integer, nullable=False)

    def as_dict(self) -> dict:
        return {
            "id": str(self.id),
            "patient_vitals_retention_period_ms": self.patient_vitals_retention_period_ms,
        }


class AppSetting(Entity):
    __tablename__ = "app_settings"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    key: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)
    value: Mapped[str] = mapped_column(String(150), nullable=False)

    def as_dict(self) -> dict:
        return {
            "id": str(self.id),
            "key": str(self.key),
            "value": str(self.value),
        }
