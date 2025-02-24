package org.sibel.emulator.gui;

import java.util.Map;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.sibel.emulator.gui.listeners.*;
import org.somda.sdc.biceps.model.participant.AlertActivation;
import org.somda.sdc.biceps.model.participant.AlertSignalPresence;

public class NoGui implements ProviderGui {
    protected static final Logger LOG = LogManager.getLogger();

    @Override
    public void open(String title) {
        LOG.info("Opening GUI: %s".formatted(title));
    }

    @Override
    public void setAudioChangeListener(AudioChangeListener audioChangeListener) {}

    @Override
    public void setPatientChangeListener(PatientChangeListener patientChangeListener) {}

    @Override
    public void setEmulationChangeListener(EmulationChangeListener emulationChangeListener) {}

    @Override
    public void setPhysiologicalAlertPresenceChangeListener(
            PhysiologicalAlertPresenceChangeListener alertChangeListener) {}

    @Override
    public void setTechnicalAlertPresenceChangeListener(TechnicalAlertPresenceChangeListener alertChangeListener) {}

    @Override
    public void setPhysiologicalAlertActivationChangeListener(PhysiologicalAlertActivationChangeListener listener) {}

    @Override
    public void setTechnicalAlertActivationChangeListener(TechnicalAlertActivationChangeListener listener) {}

    @Override
    public void setAlertSettings(
            Map<String, AlertSignalPresence> alertSignalPresenceByHandle,
            Map<String, AlertActivation> alertConditionActivationByHandle) {}

    @Override
    public void setBatteryChangeListener(BatteryChangeListener batteryChangeListener) {}

    @Override
    public void setBodyAngleChangeListener(BodyAngleChangeListener bodyAngleChangeListener) {}

    @Override
    public void setBpChangeListener(BpChangeListener listener) {}

    @Override
    public void setPatientInfo(PatientInfo patientInfo) {
        LOG.info("Patient info: %s".formatted(patientInfo));
    }
}
