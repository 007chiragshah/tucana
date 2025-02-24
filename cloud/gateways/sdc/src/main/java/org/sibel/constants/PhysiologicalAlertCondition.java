package org.sibel.constants;

import java.math.BigDecimal;
import java.util.List;
import org.somda.sdc.biceps.model.participant.AlertConditionPriority;

public enum PhysiologicalAlertCondition {
    HR_ALL(
            "258418",
            AlertConditionPriority.ME,
            List.of(new Source(SensorType.ANNE_CHEST, Metric.HR)),
            BigDecimal.valueOf(120.0),
            BigDecimal.valueOf(45.0),
            "sibel.anneone.alertsystem.condition.hr.all"),
    HR_LOW(
            "199768",
            AlertConditionPriority.ME,
            List.of(new Source(SensorType.ANNE_CHEST, Metric.HR)),
            null,
            BigDecimal.valueOf(45.0),
            "sibel.anneone.alertsystem.condition.hr.low"),
    HR_HIGH(
            "199764",
            AlertConditionPriority.ME,
            List.of(new Source(SensorType.ANNE_CHEST, Metric.HR)),
            BigDecimal.valueOf(120.0),
            null,
            "sibel.anneone.alertsystem.condition.hr.high"),

    RR_ALL(
            "258419",
            AlertConditionPriority.ME,
            List.of(new Source(SensorType.ANNE_CHEST, Metric.RR_METRIC)),
            BigDecimal.valueOf(30.0),
            BigDecimal.valueOf(5.0),
            "sibel.anneone.alertsystem.condition.rr.all"),
    RR_LOW(
            "258556",
            AlertConditionPriority.ME,
            List.of(new Source(SensorType.ANNE_CHEST, Metric.RR_METRIC)),
            null,
            BigDecimal.valueOf(5.0),
            "sibel.anneone.alertsystem.condition.rr.low"),
    RR_HIGH(
            "258557",
            AlertConditionPriority.ME,
            List.of(new Source(SensorType.ANNE_CHEST, Metric.RR_METRIC)),
            BigDecimal.valueOf(30.0),
            null,
            "sibel.anneone.alertsystem.condition.rr.high"),

    PR_ALL(
            "258427",
            AlertConditionPriority.ME,
            List.of(new Source(SensorType.ANNE_CHEST, Metric.PR)),
            BigDecimal.valueOf(120.0),
            BigDecimal.valueOf(45.0),
            "sibel.anneone.alertsystem.condition.pr.all"),
    PR_LOW(
            "258560",
            AlertConditionPriority.ME,
            List.of(new Source(SensorType.ANNE_CHEST, Metric.PR)),
            null,
            BigDecimal.valueOf(45.0),
            "sibel.anneone.alertsystem.condition.pr.low"),
    PR_HIGH(
            "258563",
            AlertConditionPriority.ME,
            List.of(new Source(SensorType.ANNE_CHEST, Metric.PR)),
            BigDecimal.valueOf(120.0),
            null,
            "sibel.anneone.alertsystem.condition.pr.high"),

    SPO2_ALL(
            "258420",
            AlertConditionPriority.ME,
            List.of(new Source(SensorType.ANNE_CHEST, Metric.SPO2)),
            BigDecimal.valueOf(100.0),
            BigDecimal.valueOf(85.0),
            "sibel.anneone.alertsystem.condition.spo2.all"),
    SPO2_LOW(
            "258558",
            AlertConditionPriority.ME,
            List.of(new Source(SensorType.ANNE_CHEST, Metric.SPO2)),
            null,
            BigDecimal.valueOf(85.0),
            "sibel.anneone.alertsystem.condition.spo2.low"),
    SPO2_HIGH(
            "258559",
            AlertConditionPriority.ME,
            List.of(new Source(SensorType.ANNE_CHEST, Metric.SPO2)),
            BigDecimal.valueOf(100.0),
            null,
            "sibel.anneone.alertsystem.condition.spo2.high"),

    BODY_POSITION_HIGH(
            "258426",
            AlertConditionPriority.ME,
            List.of(new Source(SensorType.ANNE_CHEST, Metric.BODY_POSITION)),
            BigDecimal.valueOf(1.0),
            null,
            "sibel.anneone.alertsystem.condition.bodyposition.high"),

    BP_SYS_ALL(
            "258421",
            AlertConditionPriority.ME,
            List.of(new Source(SensorType.ANNE_CHEST, Metric.SYS)),
            BigDecimal.valueOf(160.0),
            BigDecimal.valueOf(90.0),
            "sibel.anneone.alertsystem.condition.bpsys.all"),
    BP_SYS_LOW(
            "258431",
            AlertConditionPriority.ME,
            List.of(new Source(SensorType.ANNE_CHEST, Metric.SYS)),
            null,
            BigDecimal.valueOf(90.0),
            "sibel.anneone.alertsystem.condition.bpsys.low"),
    BP_SYS_HIGH(
            "258432",
            AlertConditionPriority.ME,
            List.of(new Source(SensorType.ANNE_CHEST, Metric.SYS)),
            BigDecimal.valueOf(160.0),
            null,
            "sibel.anneone.alertsystem.condition.bpsys.high"),

    BP_DIA_ALL(
            "258422",
            AlertConditionPriority.ME,
            List.of(new Source(SensorType.ANNE_CHEST, Metric.DIA)),
            BigDecimal.valueOf(100.0),
            BigDecimal.valueOf(50.0),
            "sibel.anneone.alertsystem.condition.bpdia.all"),
    BP_DIA_LOW(
            "258433",
            AlertConditionPriority.ME,
            List.of(new Source(SensorType.ANNE_CHEST, Metric.DIA)),
            null,
            BigDecimal.valueOf(50.0),
            "sibel.anneone.alertsystem.condition.bpdia.low"),
    BP_DIA_HIGH(
            "258434",
            AlertConditionPriority.ME,
            List.of(new Source(SensorType.ANNE_CHEST, Metric.DIA)),
            BigDecimal.valueOf(100.0),
            null,
            "sibel.anneone.alertsystem.condition.bpdia.high"),

    BODY_TEMP_ALL(
            "258425",
            AlertConditionPriority.ME,
            List.of(new Source(SensorType.ANNE_CHEST, Metric.CHEST_TEMP)),
            BigDecimal.valueOf(38.0),
            BigDecimal.valueOf(34.0),
            "sibel.anneone.alertsystem.condition.bodytemp.all"),
    BODY_TEMP_LOW(
            "258435",
            AlertConditionPriority.ME,
            List.of(new Source(SensorType.ANNE_CHEST, Metric.CHEST_TEMP)),
            null,
            BigDecimal.valueOf(34.0),
            "sibel.anneone.alertsystem.condition.bodytemp.low"),
    BODY_TEMP_HIGH(
            "258436",
            AlertConditionPriority.ME,
            List.of(new Source(SensorType.ANNE_CHEST, Metric.CHEST_TEMP)),
            BigDecimal.valueOf(38.0),
            null,
            "sibel.anneone.alertsystem.condition.bodytemp.high"),

    CHEST_SKIN_TEMP_ALL(
            "258424",
            AlertConditionPriority.ME,
            List.of(new Source(SensorType.ANNE_CHEST, Metric.CHEST_TEMP)),
            BigDecimal.valueOf(38.0),
            BigDecimal.valueOf(34.0),
            "sibel.anneone.alertsystem.condition.chest.skintemp.all"),
    CHEST_SKIN_TEMP_LOW(
            "258429",
            AlertConditionPriority.ME,
            List.of(new Source(SensorType.ANNE_CHEST, Metric.CHEST_TEMP)),
            null,
            BigDecimal.valueOf(34.0),
            "sibel.anneone.alertsystem.condition.chest.skintemp.low"),
    CHEST_SKIN_TEMP_HIGH(
            "258430",
            AlertConditionPriority.ME,
            List.of(new Source(SensorType.ANNE_CHEST, Metric.CHEST_TEMP)),
            BigDecimal.valueOf(38.0),
            null,
            "sibel.anneone.alertsystem.condition.chest.skintemp.high"),

    LIMB_SKIN_TEMP_ALL(
            "258424",
            AlertConditionPriority.ME,
            List.of(new Source(SensorType.ANNE_CHEST, Metric.CHEST_TEMP)),
            BigDecimal.valueOf(38.0),
            BigDecimal.valueOf(34.0),
            "sibel.anneone.alertsystem.condition.limb.skintemp.all"),
    LIMB_SKIN_TEMP_LOW(
            "258429",
            AlertConditionPriority.ME,
            List.of(new Source(SensorType.ANNE_CHEST, Metric.CHEST_TEMP)),
            null,
            BigDecimal.valueOf(34.0),
            "sibel.anneone.alertsystem.condition.limb.skintemp.low"),
    LIMB_SKIN_TEMP_HIGH(
            "258430",
            AlertConditionPriority.ME,
            List.of(new Source(SensorType.ANNE_CHEST, Metric.CHEST_TEMP)),
            BigDecimal.valueOf(38.0),
            null,
            "sibel.anneone.alertsystem.condition.limb.skintemp.high");

    public final String code;
    public final AlertConditionPriority priority;
    public final List<Source> sources;
    public final BigDecimal upperLimit;
    public final BigDecimal lowerLimit;
    public final String handle;

    PhysiologicalAlertCondition(
            String code,
            AlertConditionPriority priority,
            List<Source> sources,
            BigDecimal upperLimit,
            BigDecimal lowerLimit,
            String handle) {
        this.priority = priority;
        this.handle = handle;
        this.sources = sources;
        this.code = code;
        this.upperLimit = upperLimit;
        this.lowerLimit = lowerLimit;
    }

    public record Source(SensorType sensorType, Metric metric) {}
}
