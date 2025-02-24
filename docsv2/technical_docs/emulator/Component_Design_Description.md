<div align="center">
<h2>⚜️ Component Design Description</h2>
</div>

### **High Level System Architecture**

The Emulator Platform is a software tool designed to simulate virtual devices. The platform consists of several key modules like Alarms, Proxy, Sensors, Monitor, Admission and MLLP.

![Class Diagram](<Diagrams/Images/class_diagram.png>)

### **Core Services Explained**

| Service                        | Description                                                                                              | API Endpoints Involved |
|--------------------------------|----------------------------------------------------------------------------------------------------------|------------------------|
| **Alarm Management**           | Manages patient alarms, technical alerts, and device-specific alarm thresholds. Handles creation, activation, and configuration of alarms/alert ranges. | `PUT /emulator/alarm`, `PUT /emulator/technical_alert`, `PUT /emulator/device/range` |
| **Device Command Proxy**       | Proxies device-specific commands (e.g., deletion) to emulate. | `POST /emulator/proxy/device/command/DeleteDevice` |
| **Sensor Management**          | Controls the lifecycle of emulated sensors (e.g., connecting/disconnecting sensors, updating emulation modes). Manages sensor states and interactions with patient monitors. | `POST /emulator/sensor/ConnectSensor`, `POST /emulator/sensor/DisconnectSensor`, `POST /emulator/sensor/UpdateSensorMode` |
| **Patient Monitor Management** | Manages emulated patient monitors, including connectivity, sensor associations, patient sessions, and configuration (e.g., audio settings). Retrieves monitor status and emulation details. | `GET /emulator/monitor`, `POST /emulator/monitor/ConnectPatientMonitor`, `POST /emulator/monitor/DisconnectMonitor`, `POST /emulator/monitor/OpenPatientSession`, `POST /emulator/monitor/ClosePatientSession`, `POST /emulator/monitor/UpdatePatientMonitorConfig` |
| **Patient Admission Control**  | Handles patient admission workflows, including rejection of admission requests. | `POST /emulator/RejectAdmission` |
| **HL7/MLLP Integration**       | Manages logging and retrieval of HL7 messages sent via MLLP for health data exchange. Supports debugging and validation of HL7 interfaces. | `GET /emulator/mllp` |
| **System Health Monitoring**   | Monitors the operational status of the API and emulator components. Provides real-time health checks to ensure system availability. | `GET /health`, `GET /emulator/health` |

---

### **Environment Configuration**

The following .env file contains the necessary environment settings for development and deployment.
```
DEBUG=
LOG_LEVEL=
GUNICORN_WORKERS=
ENVIRONMENT=
APPLICATION_PORT=
BASE_PATH=
TOTAL_MONITORS=
TOTAL_SENSORS_PER_MONITOR=
ECG_MAXIMUM_DATAPOINTS_PER_SECOND=
ECG_MESSAGE_INTERVAL_IN_SECONDS=
PLETH_MAXIMUM_DATAPOINTS_PER_SECOND=
PLETH_MESSAGE_INTERVAL_IN_SECONDS=
RR_MAXIMUM_DATAPOINTS_PER_SECOND=
RR_MESSAGE_INTERVAL_IN_SECONDS=
KAFKA_HOST=
KAFKA_PORT=
KAFKA_PASSWORD=
KAFKA_CA_FILE_PATH=
KAFKA_CERT_FILE_PATH=
KAFKA_KEY_FILE_PATH=
KAFKA_VITALS_TOPIC=
KAFKA_ALERTS_TOPIC=
KAFKA_TECHNICAL_ALERTS_TOPIC=
KAFKA_DEVICE_TOPIC=
KAFKA_SDC_REALTIME_STATE_TOPIC=
CORS_ORIGINS=
SIBEL_VERSION=
WEB_GATEWAY_URL=
DEVICE_PLATFORM_URL=
ADMIN_USERNAME=
ADMIN_PASSWORD=
```