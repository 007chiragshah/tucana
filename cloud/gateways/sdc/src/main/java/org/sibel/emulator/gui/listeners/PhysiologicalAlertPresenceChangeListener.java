package org.sibel.emulator.gui.listeners;

import org.sibel.constants.PhysiologicalAlertSignal;
import org.somda.sdc.biceps.model.participant.AlertSignalPresence;

public interface PhysiologicalAlertPresenceChangeListener {
    void onAlertPresenceChanged(PhysiologicalAlertSignal alert, AlertSignalPresence presence);
}
