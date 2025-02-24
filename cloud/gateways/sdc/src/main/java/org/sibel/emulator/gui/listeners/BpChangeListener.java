package org.sibel.emulator.gui.listeners;

import java.math.BigDecimal;
import java.time.Instant;

public interface BpChangeListener {
    void onBpChange(BigDecimal pr, BigDecimal sys, BigDecimal dia, BigDecimal map, Instant determinationTime);
}
