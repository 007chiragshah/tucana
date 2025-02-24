package org.sibel.constants;

public enum SensorType {
    PM("Patient Monitor", "pm"),
    ANNE_CHEST("ANNE Chest", "annechest"),
    ANNE_LIMB("ANNE Limb", "annelimb"),
    NONIN("Nonin 3150", "nonin"),
    BP_MONITOR("Viatom BP monitor", "bp2monitor");

    public final String code;
    public final String handle;

    SensorType(String code, String handle) {
        this.code = code;
        this.handle = handle;
    }
}
