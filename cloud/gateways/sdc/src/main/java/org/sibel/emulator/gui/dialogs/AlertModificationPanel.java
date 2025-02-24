package org.sibel.emulator.gui.dialogs;

import java.awt.*;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Stream;
import javax.swing.*;
import org.apache.commons.lang3.tuple.Pair;
import org.sibel.constants.MdibHandles;
import org.sibel.constants.PhysiologicalAlertSignal;
import org.sibel.constants.SensorType;
import org.sibel.constants.TechnicalAlertSignal;
import org.sibel.emulator.gui.listeners.PhysiologicalAlertActivationChangeListener;
import org.sibel.emulator.gui.listeners.PhysiologicalAlertPresenceChangeListener;
import org.sibel.emulator.gui.listeners.TechnicalAlertActivationChangeListener;
import org.sibel.emulator.gui.listeners.TechnicalAlertPresenceChangeListener;
import org.somda.sdc.biceps.model.participant.AlertActivation;
import org.somda.sdc.biceps.model.participant.AlertSignalPresence;

public class AlertModificationPanel extends JPanel {
    private final Map<String, PhysiologicalAlertSignal> physiologicalAlertsBySignalHandle = new HashMap<>();
    private final Map<String, PhysiologicalAlertSignal> physiologicalAlertsByConditionHandle = new HashMap<>();
    private final Map<String, Pair<SensorType, TechnicalAlertSignal>> technicalAlertsBySignalHandle = new HashMap<>();
    private final Map<String, Pair<SensorType, TechnicalAlertSignal>> technicalAlertsByConditionHandle =
            new HashMap<>();

    private final JComboBox<String> alertsSignalsComboBox;
    private final JComboBox<String> alertConditionsComboBox;

    private final PhysiologicalAlertPresenceChangeListener physiologicalAlertPresenceChangeListener;
    private final PhysiologicalAlertActivationChangeListener physiologicalAlertActivationChangeListener;
    private final TechnicalAlertPresenceChangeListener technicalAlertPresenceChangeListener;
    private final TechnicalAlertActivationChangeListener technicalAlertActivationChangeListener;

    public AlertModificationPanel(
            PhysiologicalAlertPresenceChangeListener physiologicalAlertPresenceChangeListener,
            PhysiologicalAlertActivationChangeListener physiologicalAlertActivationChangeListener,
            TechnicalAlertPresenceChangeListener technicalAlertPresenceChangeListener,
            TechnicalAlertActivationChangeListener technicalAlertActivationChangeListener) {
        this.physiologicalAlertPresenceChangeListener = physiologicalAlertPresenceChangeListener;
        this.physiologicalAlertActivationChangeListener = physiologicalAlertActivationChangeListener;
        this.technicalAlertPresenceChangeListener = technicalAlertPresenceChangeListener;
        this.technicalAlertActivationChangeListener = technicalAlertActivationChangeListener;

        initPhysiologicalAlertsBySignalHandle();
        initPhysiologicalAlertsByConditionHandle();
        initTechnicalAlertsBySignalHandle();
        initTechnicalAlertsByConditionHandle();

        alertsSignalsComboBox = getAlertsComboBox(Stream.concat(
                        physiologicalAlertsBySignalHandle.keySet().stream(),
                        technicalAlertsBySignalHandle.keySet().stream())
                .sorted()
                .toArray(String[]::new));
        alertConditionsComboBox = getAlertsComboBox(Stream.concat(
                        physiologicalAlertsByConditionHandle.keySet().stream(),
                        technicalAlertsByConditionHandle.keySet().stream())
                .sorted()
                .toArray(String[]::new));

        setLayout(new BoxLayout(this, BoxLayout.Y_AXIS));
        setBorder(BorderFactory.createLineBorder(Color.GRAY));
        add(getContentPane());
    }

    private JComboBox<String> getAlertsComboBox(String[] alertHandles) {
        var alertComboBox = new JComboBox<>(alertHandles);
        alertComboBox.setSelectedIndex(0);
        alertComboBox.setMaximumSize(new Dimension(Integer.MAX_VALUE, 50));
        return alertComboBox;
    }

    private JPanel getContentPane() {
        var contentPane = new JPanel();
        contentPane.setLayout(new BoxLayout(contentPane, BoxLayout.Y_AXIS));
        contentPane.setBorder(BorderFactory.createEmptyBorder(5, 5, 5, 5));
        contentPane.add(new JLabel("Modify alerts:"));
        contentPane.add(Box.createVerticalStrut(5));
        contentPane.add(getAlertSignalsControls());
        contentPane.add(Box.createVerticalStrut(5));
        contentPane.add(getAlertConditionsControls());
        return contentPane;
    }

    private JPanel getAlertSignalsControls() {
        var panel = new JPanel();

        panel.setLayout(new BoxLayout(panel, BoxLayout.X_AXIS));

        panel.add(alertsSignalsComboBox);
        panel.add(Box.createHorizontalStrut(10));
        panel.add(getAlertSignalButton("On", AlertSignalPresence.ON));
        panel.add(Box.createHorizontalStrut(5));
        panel.add(getAlertSignalButton("Latch", AlertSignalPresence.LATCH));
        panel.add(Box.createHorizontalStrut(5));
        panel.add(getAlertSignalButton("Off", AlertSignalPresence.OFF));

        return panel;
    }

    private JButton getAlertSignalButton(String title, final AlertSignalPresence presence) {
        var button = new JButton(title);
        button.addActionListener(e -> handleAlertSignalPresenceChanged(presence));
        return button;
    }

    private void handleAlertSignalPresenceChanged(AlertSignalPresence presence) {
        var selectedHandle = (String) alertsSignalsComboBox.getSelectedItem();
        var physiologicalAlert = physiologicalAlertsBySignalHandle.getOrDefault(selectedHandle, null);
        var technicalAlertPair = technicalAlertsBySignalHandle.getOrDefault(selectedHandle, null);

        if (physiologicalAlert != null) {
            physiologicalAlertPresenceChangeListener.onAlertPresenceChanged(physiologicalAlert, presence);
        }
        if (technicalAlertPair != null) {
            technicalAlertPresenceChangeListener.onAlertPresenceChanged(
                    technicalAlertPair.getLeft(), technicalAlertPair.getRight(), presence);
        }
    }

    private JPanel getAlertConditionsControls() {
        var panel = new JPanel();

        panel.setLayout(new BoxLayout(panel, BoxLayout.X_AXIS));

        panel.add(alertConditionsComboBox);
        panel.add(Box.createHorizontalStrut(10));
        panel.add(getAlertConditionButton("Enable", AlertActivation.ON));
        panel.add(Box.createHorizontalStrut(5));
        panel.add(getAlertConditionButton("Pause", AlertActivation.PSD));
        panel.add(Box.createHorizontalStrut(5));
        panel.add(getAlertConditionButton("Disable", AlertActivation.OFF));

        return panel;
    }

    private JButton getAlertConditionButton(String title, AlertActivation activation) {
        var button = new JButton(title);
        button.addActionListener(e -> handleAlertConditionActivationChanged(activation));
        return button;
    }

    private void handleAlertConditionActivationChanged(AlertActivation activation) {
        var selectedHandle = (String) alertConditionsComboBox.getSelectedItem();
        var physiologicalAlert = physiologicalAlertsByConditionHandle.getOrDefault(selectedHandle, null);
        var technicalAlertPair = technicalAlertsByConditionHandle.getOrDefault(selectedHandle, null);

        if (physiologicalAlert != null) {
            physiologicalAlertActivationChangeListener.onAlertPresenceChanged(physiologicalAlert, activation);
        }
        if (technicalAlertPair != null) {
            technicalAlertActivationChangeListener.onAlertPresenceChanged(
                    technicalAlertPair.getLeft(), technicalAlertPair.getRight(), activation);
        }
    }

    private void initPhysiologicalAlertsBySignalHandle() {
        for (var alert : PhysiologicalAlertSignal.values()) {
            physiologicalAlertsBySignalHandle.put(MdibHandles.getAlertSignalHandle(alert), alert);
        }
    }

    private void initPhysiologicalAlertsByConditionHandle() {
        for (var alert : PhysiologicalAlertSignal.values()) {
            physiologicalAlertsByConditionHandle.put(MdibHandles.getAlertConditionHandle(alert.condition), alert);
        }
    }

    private void initTechnicalAlertsBySignalHandle() {
        for (var alert : TechnicalAlertSignal.values()) {
            for (var sensorType : SensorType.values()) {
                technicalAlertsBySignalHandle.put(
                        MdibHandles.getAlertSignalHandle(sensorType, alert), Pair.of(sensorType, alert));
            }
        }
    }

    private void initTechnicalAlertsByConditionHandle() {
        for (var alert : TechnicalAlertSignal.values()) {
            for (var sensorType : SensorType.values()) {
                technicalAlertsByConditionHandle.put(
                        MdibHandles.getAlertConditionHandle(sensorType, alert.condition), Pair.of(sensorType, alert));
            }
        }
    }
}
