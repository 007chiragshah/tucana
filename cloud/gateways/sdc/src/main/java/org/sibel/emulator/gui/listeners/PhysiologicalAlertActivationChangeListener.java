package org.sibel.emulator.gui.listeners;

import org.sibel.constants.PhysiologicalAlertSignal;
import org.somda.sdc.biceps.model.participant.AlertActivation;

public interface PhysiologicalAlertActivationChangeListener {
    void onAlertPresenceChanged(PhysiologicalAlertSignal alert, AlertActivation activation);
}
