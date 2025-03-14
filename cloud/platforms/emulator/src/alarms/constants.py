import enum

from src.emulator.constants import AlarmCodes


class TechnicalAlarmCodes(str, enum.Enum):
    OUT_OF_RANGE_ALERT = AlarmCodes.OUT_OF_RANGE_ALERT.value
    LOW_SIGNAL_ALERT = AlarmCodes.LOW_SIGNAL_ALERT.value
    CRITICAL_BATTERY_ALERT = AlarmCodes.CRITICAL_BATTERY_ALERT.value
    LOW_BATTERY_ALERT = AlarmCodes.LOW_BATTERY_ALERT.value
    SENSOR_FAILURE_ALERT = AlarmCodes.SENSOR_FAILURE_ALERT.value
    LEAD_OFF_ALERT = AlarmCodes.LEAD_OFF_ALERT.value
    POOR_SKIN_CONTACT_ALERT = AlarmCodes.POOR_SKIN_CONTACT_ALERT.value
    LOOSE_SLEEVE_ALERT = AlarmCodes.LOOSE_SLEEVE_ALERT.value
    WEAK_PULSE_ALERT = AlarmCodes.WEAK_PULSE_ALERT.value
    MOVEMENT_DETECTED_ALERT = AlarmCodes.MOVEMENT_DETECTED_ALERT.value
    FINGER_NOT_DETECTED_ALERT = AlarmCodes.FINGER_NOT_DETECTED_ALERT.value
    SENSOR_ERROR_ALERT = AlarmCodes.SENSOR_ERROR_ALERT.value
    SYSTEM_ERROR_ALERT = AlarmCodes.SYSTEM_ERROR_ALERT.value
    MODULE_FAILURE_ALERT = AlarmCodes.MODULE_FAILURE_ALERT.value
