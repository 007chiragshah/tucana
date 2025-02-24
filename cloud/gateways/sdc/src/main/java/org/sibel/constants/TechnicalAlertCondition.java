package org.sibel.constants;

import java.math.BigDecimal;
import org.somda.sdc.biceps.model.participant.AlertConditionPriority;

public enum TechnicalAlertCondition {
    LEAD_OFF("196880", AlertConditionPriority.LO, Metric.DEVICE_LEAD, null, null, "leadoff"),
    LOW_BATTERY("196802", AlertConditionPriority.LO, Metric.BATTERY, null, null, "lowbattery"),
    CRITICAL_BATTERY("197336", AlertConditionPriority.HI, Metric.BATTERY, null, null, "critbattery");

    public final String code;
    public final AlertConditionPriority priority;
    public final Metric metric;
    public final BigDecimal upperLimit;
    public final BigDecimal lowerLimit;
    public final String handle;

    TechnicalAlertCondition(
            String code,
            AlertConditionPriority priority,
            Metric metric,
            BigDecimal upperLimit,
            BigDecimal lowerLimit,
            String handle) {
        this.code = code;
        this.priority = priority;
        this.metric = metric;
        this.upperLimit = upperLimit;
        this.lowerLimit = lowerLimit;
        this.handle = handle;
    }
}
