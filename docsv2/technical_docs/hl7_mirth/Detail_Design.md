<div align="center">
<h1>HL7 & Mirth Gateway</h1>
<h2> ⚜️ Detailed Design </h2>
</div>

### Channel Functionality

The Mirth Gateway serves as the communication interface between the Central Hub server and the EHR system of healthcare providers. This gateway facilitates interoperability, leveraging Mirth Connect for message routing, transformation, and data integration. The system processes HL7v2 messages and uses MLLP over TCP/IP to ensure seamless communication between systems. The integration also involves secure TLS encryption for data transmission.

#### Channel Components

1. **Source Connector**:

The source connector is responsible for receiving messages from a Central Hub.It could be a listener that waits for incoming messages (_e.g., HTTP Listener, TCP Listener_), or it could be a file reader that pulls data from files (_e.g., FTP, SFTP_).

2. **Transformer**:

The transformer is used to modify or transform the data before it is sent to the destination. Transformations could include mapping, field manipulation, or data conversion (_e.g., from JSON to HL7_).
It can also include filters (conditions for processing messages) and scripts (for more complex logic written in JavaScript).

3. **Destination Connector**:

The destination connector is responsible for sending the transformed data to the target system (such as an EHR, database, or external service). It supports multiple communication protocols.

#### Channel Configuration

1. **Channel Properties**:

Channels are configured with properties such as name, enabled/disabled state, and channel type (e.g., inbound or outbound).
Other settings include error handling mechanisms, retry logic, and timeout configurations.

2. **Filter & Routing Logic**:

Channels may include logic to filter messages based on specific criteria, such as message content or header values.

The routing decision could also be based on conditions defined within the channel (e.g., routing different types of messages to different destinations).


### Channel Design Description

#### Conf manager HTTP Polling

1. **Source**:

File Reader: This channel is configured to read from a specified file source every 5 seconds.

2. **Destination**:

*HTTP Sender*: The destination is an HTTP endpoint (http://authentication:8004/api/configuration/), which is configurable via the CONF_SERVICE_URL environment variable.
The HTTP method is GET, and the API response returns configuration values in JSON format, including:
    *   MLLP_PORT
    *   MLLP_HOST
    *   MLLP_EXPORT_INTERVAL_MINUTES

3. **Purpose**:

The response is managed by the Response Transformer, which updates environment variables (MLLP_PORT, MLLP_HOST, MLLP_EXPORT_INTERVAL_MINUTES) based on the API response.

#### Router
1.  **Source**:

*HTTP Listener*: 
Listens on port 6662 for incoming HTTP requests.

2. **Processing Logic**:

A JavaScript Writer Connector processes the request by checking the contextPath of the URL.

Based on the contextPath:
If the path is /query/patient:
Manage body parameters from the source request.
Routes the request to the PatientQuery channel.

If the path is /consume:
Routes the request to the HTTP Server channel.

For all other paths:
Returns a 404 status with the message "Unknown endpoint".

3. **Purpose**:

Acts as a router to direct incoming HTTP requests to appropriate channels based on the URL's contextPath.

#### PatientQuery

1. **Source**:

*HTTP Listener*: Listens on port 6663 with the contextPath /query/patient.

2. **Destination**:

TCP Sender: Sends data using MLLP (Minimal Lower Layer Protocol) transmission mode to the EHR system.

The destination configuration is managed via environment variables:
    *   Address: MLLP_HOST
    *   Port: MLLP_PORT

3. **Processing Logic**:

The Transformer converts incoming data to the HL7 v2.6 QBP^Q22 message type.

After the data transformation:
The data is sent to the destination.

The Response Transformer processes the response, determining success or failure and storing the outcome accordingly.

4. **Purpose**:

Facilitates querying the EHR system with HL7 v2.6 formatted messages.

#### HTTP Server

1.  **Source**:

_HTTP Listener_: Listens on port 6664 with the contextPath /consume.

2.  **Destination**:

A JavaScript Writer Connector processes incoming messages.
The messages are stored in a global messageList array object, which is later used by the Scheduler channel.

3.  **Purpose**:

Consumes incoming HTTP requests and temporarily stores the messages for scheduled processing.


####    Scheduler

1.  **Source**:

_Polling Channel_: Executes every 1 minute.

2.  **Processing Logic**:

A JavaScript Reader Connector checks the time since the last message was sent to the MLLP Sender channel.

If the time exceeds the interval defined by MLLP_EXPORT_INTERVAL_MINUTES (converted to milliseconds):
Sends all messages from the messageList global object to the MLLP Sender channel one by one.

3.  **Purpose**:

Ensures periodic processing of messages stored in the messageList object, based on the defined interval.


####    MLLP Sender

1.  **Source**:

_Channel Reader_: Accepts messages from other channels (e.g., Scheduler).

2.  **Destination**:

_TCP Sender_: Sends data using MLLP transmission mode to the EHR system.

Configuration values for the destination address and port are managed via environment variables:
    
    *   Address: MLLP_HOST
    *   Port: MLLP_PORT

3.  **Processing Logic**:

The Transformer converts incoming data to the HL7 v2.6 ORU^R01 message type.

After the transformation:
The data is sent to the destination.
The Response Transformer processes the response, determining success or failure.

4.  **Purpose**:
Transmits HL7 v2.6 formatted messages to the EHR system and manages the response.


### Supported HL7 messages

There are 3 set of messages that are currently supported by Central Server
*   QRY_A19
*   ADR_A19
*   ORU_R01


#### QRY_A19 - Patient Query

The **QRY^A19** message is a query used to request list of patients who have medical records in EHR and who are associated with Hospital organisation. The message is typically used in Patient Administration applications, enabling systems to request information about a specific patient or patients.

The operation sends the QRY A19 to an upstream system meaning here is EHR, which returns the ADR A19 message as its ACK.

1.  **Purpose**: To request patient demographic and visit information.
2.   **Segments**:
    *  	MSH (Message Header): Contains message-level metadata.
    *	QRD (Query Definition): Specifies query criteria, including patient details or search parameters.
    *   QRF (Query Filter): (Optional) Adds additional filtering criteria.


**Sample QRY^A19 Message**

```
MSH|^~\&|HIS|HOSPITAL|EHR|CLINIC|20250110101010||QRY^A19|123456|P|2.6
QRD|20250110101010|R|I|A19|123456789|||RES|100^RD||ALL
QRF||PATID123||
```

#### ADR^A19 - Patient Query acknowledgement 

The **ADR^A19** message is a response to a QRY^A19 query. It contains demographic and visit information about a patient or patients as requested by the query. This message is typically used in Patient Administration applications.


1. **Purpose**: To provide demographic and visit information in response to a QRY^A19 query.
2. **Segments**:
   - **MSH (Message Header)**: Contains message-level metadata.
   - **MSA (Message Acknowledgment)**: Confirms receipt and processing status of the query.
   - **PID (Patient Identification)**: Contains patient demographic information.
   - **PV1 (Patient Visit)**: Contains visit-specific information.


---

**Sample ADR^A19 Message**

```
MSH|^~\&|EHR|CLINIC|HIS|HOSPITAL|20250110101111||ADR^A19|654321|P|2.6
MSA|AA|123456
PID|1||PATID123^^^HOSPITAL^MR||DOE^JOHN^A||19800101|M|||123 MAIN ST^^CITY^ST^12345||555-555-1234|||M|C||123456789
PV1|1|I|ICU^1^1^HOSPITAL^^BED1||||1234^ATTENDING^PHYSICIAN^^^DR||SUR|||||||12345^REFERRING^PHYSICIAN^^^DR|IC||||||||||||||||||||||||20250105
```

####    ORU^R01 Message Overview

The **ORU^R01** message is a commonly used HL7 message for transmitting observational results. In Central Server component ORU messages are use to transfer patient vital infromation to the Hospital's EHR system 


1. **Purpose**: To transmit observational results to other systems.
2. **Segments**:
   - **MSH (Message Header)**: Contains message-level metadata.
   - **PID (Patient Identification)**: Provides patient demographic information.
   - **OBR (Observation Request)**: Contains order details for the observation.
   - **OBX (Observation/Result)**: Reports the observation results.

---

## Sample ORU^R01 Message

```
MSH|^~\&|LAB|HOSPITAL|EHR|CLINIC|20250110102020||ORU^R01|987654|P|2.6
PID|1||PATID456^^^HOSPITAL^MR||DOE^JANE^A||19900101|F|||456 MAIN ST^^CITY^ST^67890||555-555-6789|||S||987654321
OBR|1|ORD12345|ORD54321|COMPLETE BLOOD COUNT^CBC|||20250110|||||||1234^ATTENDING^PHYSICIAN^^^DR||||||||||||F
OBX|1|NM|WBC^White Blood Cell Count^L||5.8|x10^9/L|4.0-11.0|N|||F
OBX|2|NM|HGB^Hemoglobin^L||13.5|g/dL|12.0-15.5|N|||F
OBX|3|NM|PLT^Platelets^L||250|x10^9/L|150-400|N|||F
```

