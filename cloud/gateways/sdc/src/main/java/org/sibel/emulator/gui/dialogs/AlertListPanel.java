package org.sibel.emulator.gui.dialogs;

import java.awt.*;
import java.util.HashMap;
import java.util.Map;
import javax.swing.*;
import org.somda.sdc.biceps.model.participant.AlertActivation;
import org.somda.sdc.biceps.model.participant.AlertSignalPresence;

public class AlertListPanel extends JPanel {
    private final JPanel signalList = new JPanel();
    private final JPanel conditionList = new JPanel();

    private final Map<String, AlertListItemPanel> signalListItemsByHandle = new HashMap<>();
    private final Map<String, AlertListItemPanel> conditionListItemsByHandle = new HashMap<>();

    public AlertListPanel() {
        setLayout(new BoxLayout(this, BoxLayout.X_AXIS));
        setBorder(BorderFactory.createLineBorder(Color.GRAY));

        var alertSignalsTitle = new JLabel("Alert signals: ");
        alertSignalsTitle.setAlignmentX(LEFT_ALIGNMENT);

        signalList.setLayout(new BoxLayout(signalList, BoxLayout.Y_AXIS));
        signalList.setBackground(Color.WHITE);

        var signalListScrollPane = new JScrollPane(signalList);
        signalListScrollPane.setMaximumSize(new Dimension(Integer.MAX_VALUE, Integer.MAX_VALUE));
        signalListScrollPane.setAlignmentX(LEFT_ALIGNMENT);

        var signalContainer = new JPanel();
        signalContainer.setLayout(new BoxLayout(signalContainer, BoxLayout.Y_AXIS));
        signalContainer.setBorder(BorderFactory.createEmptyBorder(5, 5, 5, 5));
        signalContainer.setMaximumSize(new Dimension(Integer.MAX_VALUE, Integer.MAX_VALUE));
        signalContainer.add(alertSignalsTitle);
        signalContainer.add(Box.createVerticalStrut(5));
        signalContainer.add(signalListScrollPane);

        var alertConditionTitle = new JLabel("Alert conditions: ");
        alertConditionTitle.setAlignmentX(LEFT_ALIGNMENT);

        conditionList.setLayout(new BoxLayout(conditionList, BoxLayout.Y_AXIS));
        conditionList.setBackground(Color.WHITE);

        var conditionListScrollPane = new JScrollPane(conditionList);
        conditionListScrollPane.setMaximumSize(new Dimension(Integer.MAX_VALUE, Integer.MAX_VALUE));
        conditionListScrollPane.setAlignmentX(LEFT_ALIGNMENT);

        var conditionContainer = new JPanel();
        conditionContainer.setLayout(new BoxLayout(conditionContainer, BoxLayout.Y_AXIS));
        conditionContainer.setBorder(BorderFactory.createEmptyBorder(5, 5, 5, 5));
        conditionContainer.setMaximumSize(new Dimension(Integer.MAX_VALUE, Integer.MAX_VALUE));
        conditionContainer.add(alertConditionTitle);
        conditionContainer.add(Box.createVerticalStrut(5));
        conditionContainer.add(conditionListScrollPane);

        add(signalContainer);
        add(conditionContainer);
    }

    public void setAlertSettings(
            Map<String, AlertSignalPresence> alertSignalPresenceByHandle,
            Map<String, AlertActivation> alertConditionActivationByHandle) {
        for (var entry : alertSignalPresenceByHandle.entrySet().stream()
                .sorted(Map.Entry.comparingByKey())
                .toList()) {
            var handle = entry.getKey();
            var presence = entry.getValue();
            var listItem = signalListItemsByHandle.getOrDefault(handle, null);

            if (listItem == null) {
                listItem = new AlertListItemPanel(handle, presence);
                signalListItemsByHandle.put(handle, listItem);
                signalList.add(listItem);
            } else {
                listItem.setValues(handle, presence);
            }
        }

        for (var entry : alertConditionActivationByHandle.entrySet().stream()
                .sorted(Map.Entry.comparingByKey())
                .toList()) {
            var handle = entry.getKey();
            var activation = entry.getValue();
            var listItem = conditionListItemsByHandle.getOrDefault(handle, null);

            if (listItem == null) {
                listItem = new AlertListItemPanel(handle, activation);
                conditionListItemsByHandle.put(handle, listItem);
                conditionList.add(listItem);
            } else {
                listItem.setValues(handle, activation);
            }
        }
    }
}
