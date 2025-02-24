package org.sibel.emulator.gui.dialogs;

import java.awt.*;
import java.util.Map;
import javax.swing.*;
import org.sibel.emulator.gui.listeners.PhysiologicalAlertActivationChangeListener;
import org.sibel.emulator.gui.listeners.PhysiologicalAlertPresenceChangeListener;
import org.sibel.emulator.gui.listeners.TechnicalAlertActivationChangeListener;
import org.sibel.emulator.gui.listeners.TechnicalAlertPresenceChangeListener;
import org.somda.sdc.biceps.model.participant.AlertActivation;
import org.somda.sdc.biceps.model.participant.AlertSignalPresence;

public class AlertManagementDialog extends JDialog {
    private final AlertListPanel alertListPanel = new AlertListPanel();

    public AlertManagementDialog(
            Frame owner,
            PhysiologicalAlertPresenceChangeListener physiologicalAlertPresenceChangeListener,
            PhysiologicalAlertActivationChangeListener physiologicalAlertActivationChangeListener,
            TechnicalAlertPresenceChangeListener technicalAlertPresenceChangeListener,
            TechnicalAlertActivationChangeListener technicalAlertActivationChangeListener) {
        super(owner, "Alert Management");

        var alertModificationPanel = new AlertModificationPanel(
                physiologicalAlertPresenceChangeListener,
                physiologicalAlertActivationChangeListener,
                technicalAlertPresenceChangeListener,
                technicalAlertActivationChangeListener);
        alertModificationPanel.setAlignmentX(LEFT_ALIGNMENT);
        alertModificationPanel.setMaximumSize(new Dimension(Integer.MAX_VALUE, 100));

        alertListPanel.setAlignmentX(LEFT_ALIGNMENT);
        alertListPanel.setMaximumSize(new Dimension(Integer.MAX_VALUE, Integer.MAX_VALUE));

        var mainPanel = new JPanel();
        mainPanel.add(alertModificationPanel);
        mainPanel.add(Box.createVerticalStrut(5));
        mainPanel.add(alertListPanel);
        mainPanel.setLayout(new BoxLayout(mainPanel, BoxLayout.Y_AXIS));
        mainPanel.setBorder(BorderFactory.createEmptyBorder(5, 5, 5, 5));

        setContentPane(mainPanel);
        setMinimumSize(new Dimension(750, 400));
    }

    public void setAlertSettings(
            Map<String, AlertSignalPresence> alertSignalPresenceByHandle,
            Map<String, AlertActivation> alertConditionActivationByHandle) {
        alertListPanel.setAlertSettings(alertSignalPresenceByHandle, alertConditionActivationByHandle);
    }
}
