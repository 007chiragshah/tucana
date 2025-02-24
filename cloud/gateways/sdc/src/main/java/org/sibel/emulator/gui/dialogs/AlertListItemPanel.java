package org.sibel.emulator.gui.dialogs;

import java.awt.*;
import java.util.Map;
import javax.swing.*;
import org.somda.sdc.biceps.model.participant.AlertActivation;
import org.somda.sdc.biceps.model.participant.AlertSignalPresence;

public class AlertListItemPanel extends JPanel {
    private static final Map<AlertSignalPresence, Color> prefixColorByPresence = Map.of(
            AlertSignalPresence.ON, Color.GREEN,
            AlertSignalPresence.OFF, Color.RED,
            AlertSignalPresence.LATCH, Color.BLUE);
    private static final Map<AlertActivation, Color> prefixColorByActivation = Map.of(
            AlertActivation.ON, Color.GREEN,
            AlertActivation.OFF, Color.RED,
            AlertActivation.PSD, Color.BLUE);

    private final JLabel prefixLabel = new JLabel();
    private final JLabel handleLabel = new JLabel();

    public AlertListItemPanel(String handle, AlertSignalPresence presence) {
        initLabels(presence.value(), prefixColorByPresence.get(presence), handle);
    }

    public AlertListItemPanel(String handle, AlertActivation activation) {
        initLabels(activation.value(), prefixColorByActivation.get(activation), handle);
    }

    public void setValues(String handle, AlertSignalPresence presence) {
        setLabels(presence.value(), prefixColorByPresence.get(presence), handle);
    }

    public void setValues(String handle, AlertActivation activation) {
        setLabels(activation.value(), prefixColorByActivation.get(activation), handle);
    }

    private void initLabels(String prefix, Color prefixColor, String handle) {
        setBackground(Color.WHITE);
        setLayout(new BoxLayout(this, BoxLayout.X_AXIS));
        setMaximumSize(new Dimension(Integer.MAX_VALUE, 25));
        setBorder(BorderFactory.createEmptyBorder(5, 5, 5, 5));

        add(prefixLabel);
        add(Box.createHorizontalStrut(10));
        add(handleLabel);

        setLabels(prefix, prefixColor, handle);
    }

    private void setLabels(String prefix, Color prefixColor, String handle) {
        prefixLabel.setText(prefix);
        prefixLabel.setForeground(prefixColor);
        handleLabel.setText(handle);
    }
}
