package org.sibel.emulator.gui.listeners;

import org.sibel.constants.SensorType;
import org.sibel.constants.TechnicalAlertSignal;
import org.somda.sdc.biceps.model.participant.AlertSignalPresence;

public interface TechnicalAlertPresenceChangeListener {
    void onAlertPresenceChanged(SensorType device, TechnicalAlertSignal alert, AlertSignalPresence presence);
}
