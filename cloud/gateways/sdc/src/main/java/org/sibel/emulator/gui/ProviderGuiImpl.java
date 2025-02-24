package org.sibel.emulator.gui;

import java.util.Map;
import javax.swing.*;
import org.sibel.emulator.gui.dialogs.AlertManagementDialog;
import org.sibel.emulator.gui.dialogs.PatientFormDialog;
import org.sibel.emulator.gui.listeners.*;
import org.somda.sdc.biceps.model.participant.AlertActivation;
import org.somda.sdc.biceps.model.participant.AlertSignalPresence;

public class ProviderGuiImpl implements ProviderGui {
    private final JFrame gui = new JFrame();
    private final PatientPanel patientPanel = new PatientPanel();
    private final PatientFormDialog patientFormDialog;
    private final AlertManagementDialog alertManagementDialog;

    private AudioChangeListener audioChangeListener = activation -> {};
    private PatientChangeListener patientChangeListener = patientInfo -> {};
    private EmulationChangeListener emulationChangeListener = running -> {};
    private PhysiologicalAlertPresenceChangeListener physiologicalAlertPresenceChangeListener = (alert, presence) -> {};
    private TechnicalAlertPresenceChangeListener technicalAlertPresenceChangeListener = (device, alert, presence) -> {};
    private PhysiologicalAlertActivationChangeListener physiologicalAlertActivationChangeListener =
            (alert, presence) -> {};
    private TechnicalAlertActivationChangeListener technicalAlertActivationChangeListener =
            (device, alert, presence) -> {};
    private BatteryChangeListener batteryChangeListener = (value, status) -> {};
    private BodyAngleChangeListener bodyAngleChangeListener = (angle, position) -> {};
    private BpChangeListener bpChangeListener = (pr, sys, dia, map, determinationTime) -> {};

    public ProviderGuiImpl() {
        gui.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        gui.setSize(700, 800);

        // Set margin and layout
        var contentPanel = new JPanel();
        contentPanel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        contentPanel.setLayout(new BoxLayout(contentPanel, BoxLayout.Y_AXIS));

        // Audio settings buttons
        var audioPanel = new AudioPanel((activation) -> audioChangeListener.onAudioChanged(activation));
        contentPanel.add(audioPanel);

        // Emulation settings buttons
        var emulationPanel =
                new EmulationPanel((running) -> emulationChangeListener.onEmulationRunningChanged(running));
        contentPanel.add(emulationPanel);

        // Battery panel
        var batteryPanel = new BatteryPanel((value, status) -> batteryChangeListener.onBatteryChange(value, status));
        contentPanel.add(batteryPanel);

        // BodyAngle panel
        var bodyAnglePanel =
                new BodyAnglePanel((angle, position) -> bodyAngleChangeListener.onBodyAngleChanged(angle, position));
        contentPanel.add(bodyAnglePanel);

        // BodyAngle panel
        var bpPanel = new BpPanel((pr, sys, dia, map, determinationTime) ->
                bpChangeListener.onBpChange(pr, sys, dia, map, determinationTime));
        contentPanel.add(bpPanel);

        // Patient data display
        contentPanel.add(patientPanel);

        // Set patient data button
        var setPatientButton = new JButton("Set Patient");
        patientFormDialog =
                new PatientFormDialog(gui, patientInfo -> patientChangeListener.onPatientChange(patientInfo));
        setPatientButton.addActionListener(e -> patientFormDialog.setVisible(true));

        // Alert management button
        var openAlertManagementButton = new JButton("Open Alert Management");
        alertManagementDialog = new AlertManagementDialog(
                gui,
                (alert, presence) -> physiologicalAlertPresenceChangeListener.onAlertPresenceChanged(alert, presence),
                (alert, activation) ->
                        physiologicalAlertActivationChangeListener.onAlertPresenceChanged(alert, activation),
                (sensorType, alert, presence) ->
                        technicalAlertPresenceChangeListener.onAlertPresenceChanged(sensorType, alert, presence),
                (sensorType, alert, activation) ->
                        technicalAlertActivationChangeListener.onAlertPresenceChanged(sensorType, alert, activation));
        openAlertManagementButton.addActionListener(e -> alertManagementDialog.setVisible(true));

        // Bottom buttons
        var buttons = new JPanel();
        buttons.add(setPatientButton);
        buttons.add(openAlertManagementButton);
        contentPanel.add(buttons);

        // Set main panel
        gui.setContentPane(contentPanel);
    }

    @Override
    public void open(String title) {
        gui.setTitle(title);
        gui.setVisible(true);
    }

    @Override
    public void setAudioChangeListener(AudioChangeListener audioChangeListener) {
        this.audioChangeListener = audioChangeListener;
    }

    @Override
    public void setPatientChangeListener(PatientChangeListener patientChangeListener) {
        this.patientChangeListener = patientChangeListener;
    }

    @Override
    public void setEmulationChangeListener(EmulationChangeListener emulationChangeListener) {
        this.emulationChangeListener = emulationChangeListener;
    }

    @Override
    public void setPhysiologicalAlertPresenceChangeListener(
            PhysiologicalAlertPresenceChangeListener alertChangeListener) {
        physiologicalAlertPresenceChangeListener = alertChangeListener;
    }

    @Override
    public void setTechnicalAlertPresenceChangeListener(TechnicalAlertPresenceChangeListener alertChangeListener) {
        technicalAlertPresenceChangeListener = alertChangeListener;
    }

    @Override
    public void setPhysiologicalAlertActivationChangeListener(PhysiologicalAlertActivationChangeListener listener) {
        physiologicalAlertActivationChangeListener = listener;
    }

    @Override
    public void setTechnicalAlertActivationChangeListener(TechnicalAlertActivationChangeListener listener) {
        technicalAlertActivationChangeListener = listener;
    }

    @Override
    public void setAlertSettings(
            Map<String, AlertSignalPresence> alertSignalPresenceByHandle,
            Map<String, AlertActivation> alertConditionActivationByHandle) {
        alertManagementDialog.setAlertSettings(alertSignalPresenceByHandle, alertConditionActivationByHandle);
    }

    @Override
    public void setBatteryChangeListener(BatteryChangeListener batteryChangeListener) {
        this.batteryChangeListener = batteryChangeListener;
    }

    @Override
    public void setBodyAngleChangeListener(BodyAngleChangeListener bodyAngleChangeListener) {
        this.bodyAngleChangeListener = bodyAngleChangeListener;
    }

    @Override
    public void setBpChangeListener(BpChangeListener listener) {
        bpChangeListener = listener;
    }

    @Override
    public void setPatientInfo(PatientInfo patientInfo) {
        patientPanel.setPatientInfo(patientInfo);
    }
}
