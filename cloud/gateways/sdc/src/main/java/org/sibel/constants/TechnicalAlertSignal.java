package org.sibel.constants;

public enum TechnicalAlertSignal {
    LEAD_OFF("258110", TechnicalAlertCondition.LEAD_OFF, "leadoff"),
    LOW_BATTERY("258102", TechnicalAlertCondition.LOW_BATTERY, "lowbattery"),
    CRITICAL_BATTERY("258106", TechnicalAlertCondition.CRITICAL_BATTERY, "critbattery");

    public final String code;
    public final TechnicalAlertCondition condition;
    public final String handle;

    TechnicalAlertSignal(String code, TechnicalAlertCondition condition, String handle) {
        this.code = code;
        this.condition = condition;
        this.handle = handle;
    }
}
