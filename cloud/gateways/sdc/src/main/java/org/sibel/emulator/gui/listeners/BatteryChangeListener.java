package org.sibel.emulator.gui.listeners;

import org.somda.sdc.biceps.model.participant.BatteryState;

public interface BatteryChangeListener {
    void onBatteryChange(int value, BatteryState.ChargeStatus status);
}
