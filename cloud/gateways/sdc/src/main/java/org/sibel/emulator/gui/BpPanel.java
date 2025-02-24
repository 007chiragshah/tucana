package org.sibel.emulator.gui;

import java.awt.*;
import java.math.BigDecimal;
import java.time.Instant;
import javax.swing.*;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.sibel.emulator.gui.listeners.BpChangeListener;

public class BpPanel extends JPanel {
    protected static final Logger LOG = LogManager.getLogger();

    private final BpChangeListener listener;
    private final JTextField prField = new JTextField();
    private final JTextField sysField = new JTextField();
    private final JTextField diaField = new JTextField();
    private final JTextField mapField = new JTextField();
    private final JLabel determinationTimeLabel = new JLabel("Last determination time: N/A");

    public BpPanel(BpChangeListener listener) {
        this.listener = listener;

        setLayout(new BoxLayout(this, BoxLayout.Y_AXIS));

        add(new JLabel("BP monitor"));
        add(getContentPanel());
        add(determinationTimeLabel);

        setBorder(BorderFactory.createLineBorder(Color.GRAY));
    }

    private JPanel getContentPanel() {
        var panel = new JPanel();
        panel.setLayout(new FlowLayout(FlowLayout.CENTER));
        panel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));

        panel.add(new JLabel("PR "));
        prField.setColumns(5);
        panel.add(prField);

        panel.add(new JLabel(" DIA "));
        diaField.setColumns(5);
        panel.add(diaField);

        panel.add(new JLabel(" SYS "));
        sysField.setColumns(5);
        panel.add(sysField);

        panel.add(new JLabel(" MAP "));
        mapField.setColumns(5);
        panel.add(mapField);

        panel.add(getConfirmButton(listener));

        return panel;
    }

    private JButton getConfirmButton(BpChangeListener listener) {
        var button = new JButton("Confirm");
        button.addActionListener((event) -> {
            try {
                var pr = BigDecimal.valueOf(Double.parseDouble(prField.getText()));
                var sys = BigDecimal.valueOf(Double.parseDouble(sysField.getText()));
                var dia = BigDecimal.valueOf(Double.parseDouble(diaField.getText()));
                var map = BigDecimal.valueOf(Double.parseDouble(mapField.getText()));
                var determinationTime = Instant.now();
                listener.onBpChange(pr, sys, dia, map, determinationTime);

                determinationTimeLabel.setText("Last determination time: %s".formatted(determinationTime));
            } catch (Exception e) {
                LOG.error("Failed to set BP values", e);
            }
        });
        return button;
    }
}
