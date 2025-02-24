<div align="center">
<h1>SDC Gateway</h1>
<h2> ⚜️ Detailed Design </h2>
</div>

### SDC Authentication

The SDC Gateway (SDC GW) authentication is implemented using certificates. The root certificate of the certificate chain is issued by Sibel and expedited by ssl.com. Each hospital will have its own x.509 certificate, which is a child of Sibel’s root certificate. The hospital certificate is securely stored in the Central Server's Kubernetes (K8s) cluster.

#### Authentication Process


1. **Certificate Chain**:
   - **Sibel’s Root Certificate**: The root certificate of the certificate chain issued by Sibel and expedited by ssl.com.
   - **Hospital Certificate**: Each hospital has its own certificate, which is a child of Sibel’s root certificate. This certificate is securely stored in the Central Server's K8s cluster.


2. **Connection Establishment**:
   - When a SDC Provider with a certificate that is a child of the hospital's root certificate attempts to establish a connection with the SDC GW, the gateway verifies whether this certificate is a direct child of the hospital's root certificate.
   - If the verification is successful, the connection is established. If not, the connection attempt is rejected.

#### Handling Compromised Certificates

In the event that a SDC Provider's certificate is compromised, that certificate can be blacklisted. This ensures that other SDC Providers are not impacted and continue to operate securely.

```mermaid
graph TD
    A[Sibel's Root Certificate] --> B[Hospital Certificate]
    B --> C[SDC Provider Certificate]
    C --> D[SDC Gateway]
    D --> E{Verify Certificate}
    E -- Valid --> F[Establish Connection]
    E -- Invalid --> G[Reject Connection]
    H[Blacklist Compromised Certificate]
```

### Component Class Diagram

```mermaid
%% Class Diagram
classDiagram
    class CoordinatorTaskImpl {
        +coordinateRoles()
        +determineLeadership()
    }
    class LeaderTask {
        +discoverDevices()
        +assignResources()
    }
    class FollowerTask {
        +handleDevices()
        +cleanupTasks()
    }
    class PatientMonitor {
        +manageConnection()
        +processEvents()
    }
    class ConsumerReportProcessor {
        +processReports()
        +observeChanges()
    }

    CoordinatorTaskImpl --> LeaderTask
    CoordinatorTaskImpl --> FollowerTask
    PatientMonitor --> ConsumerReportProcessor
```
### Device Discovery Process

The following diagram provides a detailed illustration of the device discovery process and the interactions between the leader and follower services.

```mermaid
sequenceDiagram
    autonumber
    Leader->>SDC Provider: probe
    SDC Provider-->>Leader: device found with EPR addr: d1
    Leader->>Redis: GET sdc/device/d1
    Redis-->>Leader: assignedFollower
    alt assignedFollower == NULL
        Leader->>Redis: KEYS sdc/follower/claim/*
        Redis-->>Leader: followers
        loop For each follower fx in followers
            Leader->>Redis: SREM sdc/follower/devices/fx d1
            Redis-->>Leader: OK
            Leader->>Redis: SCARD sdc/follower/devices/fx
            Redis-->>Leader: followerCount
        end
        opt follower with lowest count -> f1
            Leader->>Redis: PUBLISH sdc/follower/channel/f1 <DeviceData>
            Redis-->>f1-Follower: <DeviceData>
            f1-Follower->>Redis: SET sdc/device/d1 f1
            Redis-->>f1-Follower: OK
            f1-Follower->>Redis: SADD sdc/follower/devices/f1 d1
            Redis-->>f1-Follower: OK
        end
    end
    Leader->>Redis: SADD sdc/follower/devices/f1 d1
    Redis-->>Leader: OK
```

*   Device Discovery and Queue Processing:
    
    -   Upon completion of the scan, the SDC service shall dispatch the discovered devices to a processing queue.
    -   This queue shall be consumed by a set of threads responsible for checking the monitoring status of each device.
    -   If the device is not being monitored, the service shall initiate device monitoring.
    -   If the device is already being monitored, the service shall disregard the device.

*   Device Monitoring and Event Subscription:
    -   As part of the device monitoring process, the service shall subscribe to events incoming from the device using the IEEE 11073 protocol.
    -   Upon successful subscription, the service shall receive HTTPS calls for each new event.
    -   The report processor shall define the handling of incoming messages.
    -   The service shall manage subscriptions to the following data types:
        1.  Waveform data
        2.  Technical metrics
        3.  Physiological metrics
        4.  Corresponding alerts

*   Data Transmission to Kafka:
    -   All incoming data shall be transmitted to Kafka, enabling the Realtime gateway to consume it.

###  Patient Admission Process

*   **Patient Search**: 

    Using the patient's identifiers, or demographic information such as the patient name, date of birth, or sex to search for a patient. The Central Server would filter through the database of patients to produce the relevant patient and their associated details.

_Patient Search from SDC Provider_

![alt text](../images/SDC_Flow-Patient%20Search%20-%20Anne%20View.drawio.png)

_Patient Search from SDC Consumer_

![alt text](../images/SDC_Flow-Patient%20Search%20-%20Central%20Hub.drawio.png)

*   Quick Admission: 

    A user-driven process that commences a session for an unidentified patient, by assigning a generated patient ID.

_Quick Admission from SDC Provider_

![alt text](../images/SDC_Flow-Quick%20Admit%20-%20Anne%20View.drawio.png)

_Quick Admission from SDC Consumer_

![alt text](../images/SDC_Flow-Quick%20Admit%20-%20CMS%20.drawio.png)


### SDC Event Processing flow

```mermaid
graph TD
    A[ConsumerReportProcessor Receives Request] --> B[Fetch Monitor Data from PatientMonitor]
    B --> C{Monitor Data Found?}
    C -- Yes --> D[Process Data]
    D --> E[Send Message to Kafka]
    C -- No --> M[Log Error: Monitor Data Not Found]
```

####   **Event Handlers**
The class uses the EventBus framework for subscribing to different types of state modifications.
-   Key subscribed events include:
    -   onComponentChange: Handles changes in component states (e.g., battery status).
    -   onMetricChange: Processes changes in device metrics.
	-   onWaveformChange: Responds to waveform state changes.
	-   onContextChange: Handles context modifications (e.g., patient assignments).
	-   onAlertChange: Processes alerts (e.g., physiological or configuration-related).

The following sequence diagram illustrates the flow for the Metrics change event. This flow is consistent across all other events.
```mermaid
sequenceDiagram
    participant ComponentStateModificationMessage
    participant ConsumerReportProcessor
    participant ProcessorFactory
    participant KafkaMessageProducer

    ComponentStateModificationMessage->>ConsumerReportProcessor: onMetricChange
    ConsumerReportProcessor->>ProcessorFactory: createMetricChangeProcessor(mdibAccess, state, patientId)
    ProcessorFactory-->>ConsumerReportProcessor: MetricChangeProcessor
    ConsumerReportProcessor->>KafkaMessageProducer: notify(brokerMessage, MESSAGE_BROKER_VITALS_TOPIC, patientId)
    KafkaMessageProducer-->>ConsumerReportProcessor: Ack/Exception
  ```