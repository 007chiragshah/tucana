package org.sibel.factories;

import org.sibel.PatientMonitor;
import org.somda.sdc.dpws.client.DiscoveredDevice;

public interface PatientMonitorFactory {
    PatientMonitor create(DiscoveredDevice discoveredDevice, PatientMonitor.DisconnectListener disconnectListener);
}
