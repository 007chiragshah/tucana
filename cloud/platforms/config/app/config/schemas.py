import uuid
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from app.common.schemas import BaseSchema

MIN_KAFKA_RETENTION_MINUTES = 60
MIN_KAFKA_RETENTION_MS = MIN_KAFKA_RETENTION_MINUTES * 60 * 1000


class SystemSettingsPayload(BaseModel):
    patient_vitals_retention_period_ms: Optional[int] = Field(
        default=None, ge=MIN_KAFKA_RETENTION_MS
    )

    def patient_vitals_retention_time_changed(self, current_retention_time_ms: int) -> bool:
        if not self.patient_vitals_retention_period_ms:
            return False
        return self.patient_vitals_retention_period_ms != current_retention_time_ms


class SystemSettingsSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    patient_vitals_retention_period_ms: Optional[int]


class CreateOrUpdateAppSettingSchema(BaseSchema):
    key: str
    value: str


class AppSettingSchema(CreateOrUpdateAppSettingSchema):
    id: uuid.UUID


class BatchCreateOrUpdateAppSettingsSchema(BaseSchema):
    settings: List[CreateOrUpdateAppSettingSchema]


class AppSettingResources(BaseSchema):
    resources: List[AppSettingSchema]
