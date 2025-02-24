package org.sibel.emulator.gui;

import java.util.Map;
import org.sibel.emulator.gui.listeners.*;
import org.somda.sdc.biceps.model.participant.AlertActivation;
import org.somda.sdc.biceps.model.participant.AlertSignalPresence;

public interface ProviderGui {
    void open(String title);

    void setAudioChangeListener(AudioChangeListener listener);

    void setPatientChangeListener(PatientChangeListener listener);

    void setEmulationChangeListener(EmulationChangeListener listener);

    void setPhysiologicalAlertPresenceChangeListener(PhysiologicalAlertPresenceChangeListener listener);

    void setTechnicalAlertPresenceChangeListener(TechnicalAlertPresenceChangeListener listener);

    void setPhysiologicalAlertActivationChangeListener(PhysiologicalAlertActivationChangeListener listener);

    void setTechnicalAlertActivationChangeListener(TechnicalAlertActivationChangeListener listener);

    void setAlertSettings(
            Map<String, AlertSignalPresence> alertSignalPresenceByHandle,
            Map<String, AlertActivation> alertConditionActivationByHandle);

    void setBatteryChangeListener(BatteryChangeListener listener);

    void setBodyAngleChangeListener(BodyAngleChangeListener listener);

    void setBpChangeListener(BpChangeListener listener);

    void setPatientInfo(PatientInfo patientInfo);
}
