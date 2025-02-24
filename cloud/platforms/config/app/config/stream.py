from app.common.event_sourcing.stream import BaseEventStream
from app.config.models import AppSetting
from app.config.schemas import SystemSettingsPayload


class SystemSettingsEventStream(BaseEventStream[SystemSettingsPayload]):
    pass


class AppSettingsEventStream(BaseEventStream[AppSetting]):
    pass
