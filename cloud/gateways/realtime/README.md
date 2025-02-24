<div align="center">
  <br>
  <img alt="tucana" src="https://user-images.githubusercontent.com/108890369/223312587-5c6326cc-5cf8-457d-9bb0-0a90f12190e5.png" height="100">
  <h1>R E A L   T I M E</h1>
  </br>
</div>

# Documentation

- [Introduction](../../../docsv2/technical_docs/realtime/Introduction.md)
- [Component Design Description](../../../docsv2/technical_docs/realtime/Component_Design_Description.md)
- [Workflow and Algorithms](../../../docsv2/technical_docs/realtime/Workflows_and_Algorithms.md)

# Run project locally

poetry run uvicorn src.main:app --port 8001

# Connecting to the realtime socket

The realtime microservice uses the Secure WebSockets (WSS) protocol. Secure WebSockets provide a bidirectional, real-time communication protocol that ensures data integrity and confidentiality through encryption, which is used for sending all the events received from the PM to the Central Hub frontend.

In order to connect to the realtime gateway it is necessary to follow these instructions:

First it is needed to connect to the server via websocket using the following URL:

`"/realtime/vitals?token=<token>"`

Where `<token>` is the access token received when logging in to the application, which can be done using the [web](../web) microservice.

Then after connecting successfully connecting to the websocket it is necessary to configure it, for which an initial message must be sent to the server containing the following data:

```json
{
  // Filters all received messages to be from the selected patients
  "patientIdentifiers": ["<Patient ID #1>", "<Patient ID #2>", "<Patient ID #3>"],
  "filters": {
    // List of code allowed for all messages received
    "codes": ["<Metric code #1>", "<Metric code #2>", "<Metric code #3>"],
    // List of codes filtered by a specific patient ID
    "patientFilters": {
      "identifier": "<Patient ID>",
      "codes": ["<Metric code #1>", "<Metric code #2>", "<Metric code #3>"]
    }
  },
  // If true, the first messages sent through the socket will be the cached metrics,
  // which are the latest values for each metric for the selected patients/codes.
  "sendCache": true
}
```

These are the parameters used for the filtering of messages that will be received through the websocket based on the patient and metric codes.

## List of message types

All messages sent through the websocket have different formats, but they all share a single attribute used for identifying the kind of message being sent, which is the `"event_type"`. The full list of possible message types is as follows:

| Event type                     | Message type | Description                                                                                                                                                                               |
|--------------------------------|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NEW_METRICS                    | Unprocessed  | Sent when a new metric value is received from the PM                                                                                                                                      |
| NEW_WAVEFORM_VITALS            | Unprocessed  | Sent when a new set of points of a waveform graph is received from the PM                                                                                                                 |
| NEW_ALERT_OBSERVATION          | Unprocessed  | Sent when a new alert is triggered by the PM. This is the earliest we can receive an alert.                                                                                               |
| DEVICE_DISCOVERED              | Unprocessed  | Sent when a PM is discovered, or when a sensor is added to an already connected PM.                                                                                                       |
| DEVICE_NEW_VITALS_RANGES       | Unprocessed  | Sent when the vital ranges change for any of the physiological alerts on the PM.                                                                                                          |
| PATIENT_ADMISSION_REJECTED     | Unprocessed  | Sent when the user rejects a patient admission on the PM.                                                                                                                                 |
| PATIENT_SESSION_CLOSED_EVENT   | Unprocessed  | Sent when the user logs out the PM                                                                                                                                                        |
| PATIENT_SESSION_STARTED        | Unprocessed  | Sent when a patient is accepted on the PM, either by accepting a patient sent by the CMS or by quick admitting a patient.                                                                 |
| PM_CONFIGURATION_UPDATED       | Unprocessed  | Sent when the config of a PM changes, i.e. when the audio is disable, paused or resumed.                                                                                                  |
| PM_CONNECTION_STATUS_REPORT    | Unprocessed  | Sent every few seconds as a health check to know when a PM disconnects.                                                                                                                   |
| SENSOR_REMOVED_EVENT           | Unprocessed  | Sent when a sensor is disconnected from a PM.                                                                                                                                             |
| BED_CREATED_EVENT              | Processed    | Sent after a bed is created                                                                                                                                                               |
| BED_UPDATED_EVENT              | Processed    | Sent after a bed is updated                                                                                                                                                               |
| BED_DELETED_EVENT              | Processed    | Sent after a bed is deleted                                                                                                                                                               |
| BED_GROUP_CREATED_EVENT        | Processed    | Sent after a bed group is created                                                                                                                                                         |
| BED_GROUP_UPDATED_EVENT        | Processed    | Sent after a bed group is updated                                                                                                                                                         |
| BED_GROUP_DELETED_EVENT        | Processed    | Sent after a bed group is deleted                                                                                                                                                         |
| BED_ASSIGNED_TO_GROUP_EVENT    | Processed    | Sent after a bed is assigned to a group                                                                                                                                                   |
| BED_REMOVED_FROM_GROUP_EVENT   | Processed    | Sent after a bed is removed from a group                                                                                                                                                  |
| DEVICE_CREATED_EVENT           | Processed    | Sent after a device is created, which happens the first time a device is connected to the Central Hub.                                                                                    |
| DEVICE_DELETED_EVENT           | Processed    | Sent after a sensor is removed from a PM, or manually removed using the API.                                                                                                              |
| DEVICE_UPDATED_EVENT           | Processed    | Sent after a PM reconnects with different information.                                                                                                                                    |
| ASSIGN_DEVICE_LOCATION_EVENT   | Processed    | Sent after a PM is assigned to a bed.                                                                                                                                                     |
| UNASSIGN_DEVICE_LOCATION_EVENT | Processed    | Sent after a PM is removed from a bed.                                                                                                                                                    |
| VITAL_RANGE_CREATED_EVENT      | Processed    | Sent after a vital range is created. This happens upon PM connection.                                                                                                                     |
| VITAL_RANGE_DELETED_EVENT      | Processed    | Sent after a vital range is deleted. This happens upon PM connection.                                                                                                                     |
| DEVICE_ALERT_CREATED           | Processed    | Sent after a device alert is created. Triggered when an alert becomes active.                                                                                                             |
| DEVICE_ALERT_UPDATED           | Processed    | Sent after a device alert is updated. Triggered when another alert is received while the initial alert was already active.                                                                |
| DEVICE_ALERT_DELETED           | Processed    | Sent after a device alert is deleted. Triggered when an alert becomes inactive (and is not latching).                                                                                     |
| MULTIPLE_DEVICE_ALERTS_UPDATED | Processed    | Sent after multiple alerts have been updated for a single device, for example when device is connected and receives all current alert statuses.                                           |
| PATIENT_CREATED_EVENT          | Processed    | Sent after a patient is created. Triggered when a patient is sent from either the PM or CentralHub for the first time (Either accepted or not, as the patient must exist to be assigned). |
| UPDATE_PATIENT_INFO_EVENT      | Processed    | Sent after a patient is modified. Triggered when a patient is added to the Central Hub or PM with a preexisting primary identifier (Given that is not connected to another PM).           |
| PATIENT_DELETED_EVENT          | Processed    | Sent after a patient is deleted (Only through the API).                                                                                                                                   |
| OBSERVATION_CREATED_EVENT      | Processed    | Sent after a physiological alert is created. Triggered when an alert becomes active.                                                                                                      |
| OBSERVATION_DELETED_EVENT      | Processed    | Sent after a physiological alert is deleted. Triggered when an alert becomes inactive (and is not latching).                                                                              |
| MULTIPLE_OBSERVATIONS_UPDATED  | Processed    | Sent after multiple alerts have been updated for a single device, for example when device is connected and receives all current alert statuses.                                           |
| ALERT_ACTIVATED_EVENT          | Processed    | Sent after an alert log is created for an alert activation.                                                                                                                               |
| ALERT_DEACTIVATED_EVENT        | Processed    | Sent after an alert log is created for an alert deactivation.                                                                                                                             |
| PATIENT_ENCOUNTER_PLANNED      | Processed    | Sent after a patient is assigned to a PM from the Central Hub, pending approval by the PM.                                                                                                |
| PATIENT_ENCOUNTER_STARTED      | Processed    | Sent after a patient session starts, either by accepting a pending patient on the PM or by quick admit.                                                                                   |
| PATIENT_ENCOUNTER_CANCELLED    | Processed    | Sent after a pending patient assignment is cancelled by the PM.                                                                                                                           |
| PATIENT_ENCOUNTER_COMPLETED    | Processed    | Sent after a patient session ends via PM logout.                                                                                                                                          |


The messages here are classified in 2 types, unprocessed, which are the messages as are received from the PM, and processed, which are the messages sent by the Central Hub backend after processing the unprocessed messages.

In general the processed messages are the ones that should be used, as that means the values were read and stored on the Central Hub backend, but in some cases it may be necessary to read unprocessed messages. For example the metrics and waveforms, which are never processed to make sure they arrive on time to the frontend.

## Unprocessed message events

The messages sent here are not processed by the backend, they come directly from the PM. From the list of messages the most important ones are the ones that carry metric and waveform information, as this are never processed by the backend to avoid delays. For the rest of the events is better to listen to the list of [Processed messages](#processed-messages).

### Formatting

All unprocessed messages sent by the SDC have a similar format for easier parsing. The messages have common attributes to all SDC messages and a variable payload which depends on the type of the event being sent. The base formatting of unprocessed messages are as follows:

```json
{
  // The type of event that is being sent. Used to determine the payload formatting.
  "event_type": "<Type>",
  // Human readable event type.
  "event_name": "<Type name>",
  // Unique UUID defined for each message
  "message_id": "<UUID>",
  // Time that the message was sent
  "timestamp": "<ISO format timestamp>",
  // Object containing the specific payload of each message type.
  // The formatting of this is determined by the "event_type" field.
  "payload": {
  }
}
```

### Metrics and waveforms

**Metrics**

```json
{
  "event_type": "NEW_METRICS",
  "event_name": "New metrics found",
  "message_id": "<UUID>",
  "timestamp": "<ISO format timestamp>",
  "payload": {
    // The patient primary identifier (The one displayed to the user)
    "patient_primary_identifier": "<Patient ID>",
    // The code of the metric data sent
    "code": "<Metric code>",
    // Contains the list of values for the metric sent, with the current implementation it sends a singular value 
    "samples":  [0.0],
    // The code that identifies the units of the value send (i.e. if the value is degrees, mV, etc.)
    "unit_code":  "<Unit code>",
    // Id of the sensor that the metric belongs to
    "device_primary_identifier": "<Device ID>",
    // Type of device that is sending the metric (i.e. ANNE Chest, ANNE Limb, etc.)
    "device_code": "<Device code>",
    // Timestamp of when the measurement was done
    "determination_time": "<ISO format timestamp>"
  }
}
```

**Waveforms**

```json
{
  "event_type": "NEW_WAVEFORM_VITALS",
  "event_name": "New waveform vitals",
  "message_id": "<UUID>",
  "timestamp": "<ISO format timestamp>",
  "payload": {
    // The patient primary identifier (The one displayed to the user)
    "patient_primary_identifier": "<Patient ID>",
    // The code of the waveform metric data sent
    "code": "<Waveform metric code>",
    // List of values for the waveform metric sent
    "samples":  [0.0, 0.1, 0.3],
    // The code that identifies the units of the value send (i.e. if the value is degrees, mV, etc.)
    "unit_code":  "<Unit code>",
    // Id of the sensor that the metric belongs to
    "device_primary_identifier": "<Device ID>",
    // Type of device that is sending the metric (i.e. ANNE Chest, ANNE Limb, etc.)
    "device_code": "<Device code>",
    // The time interval between each sample
    "sample_period":  "<Duration format: PnYnMnDTnHnMnS>",
    // The maximum time interval between two measurements (The full array of sample, not between each sample)
    "determination_period": "<Duration format: PnYnMnDTnHnMnS>",
    // Timestamp of when the measurement was done
    "determination_time": "<ISO format timestamp>"
  }
}
```

### Other messages

**Alerts**

All physiological and technical alerts are sent using the same format. The way to tell one from another is by using the alert code.

```json
{
  "event_type": "NEW_ALERT_OBSERVATION",
  "event_name": "Alert update",
  "message_id": "<UUID>",
  "timestamp": "<ISO format timestamp>",
  "payload": {
    // The patient primary identifier (The one displayed to the user)
    "patient_primary_identifier": "<Patient ID>",
    // Code of the alert sent
    "code": "<Alert code>",
    // Id of the sensor that sent the alert
    "device_primary_identifier": "<Device ID>",
    // Type of device that is sending the alert (i.e. ANNE Chest, ANNE Limb, etc.)
    "device_code": "<Device code>",
    // Determines if the alert should be displayed to the user
    "active": true,
    // Determines if the alert is latching (i.e. the alert is no longer active, but it was not dismissed by the user)
    "latching": false,
    // Priority of the alert, which can be "HI", "ME", "LO" 
    "priority": "HI",
    // Timestamp of when the current alert event was sent
    "determination_time": "<ISO format timestamp>",
    // Vital range that relates to the alert, needed to know which values were the ones that triggered the alert
    "vital_range": {
      // Code of the vital range
      "code": "<Vital range code>",
      // Upper limit of the range (i.e. max value allowed before triggering an alarm)
      "upper_limit": 1.0,
      // Lower limit of the range
      "lower_limit": 2.0,
      // Determines if the alerts for the specified range are enabled or not.
      // When false, no alarms are triggered for this range.
      "alert_condition_enabled": false
    }
  }
}
```

**Device discovered**

This message is sent when either a PM is being connected to the SDC gateway, or a sensor is being added to an already connected PM

```json
{
  "event_name": "Device discovered",
  "event_type": "DEVICE_DISCOVERED",
  "message_id": "<UUID>",
  "timestamp": "<ISO format timestamp>",
  "payload": {
    // Contains all the information related to the device being connected
    "device": {
      // ID of the device being connected
      "primary_identifier": "<Device ID>",
      // Name of the device connected (Currently it uses the same value as device_code)
      "name": "<Device name>",
      // Type of device connected (i.e. Patient Monitor, ANNE Chest, ANNE Limb, etc.)
      "device_code": "<Device type>",
      // If the connected device is a sensor it contains the ID of the patient monitor that is connected to, otherwise this value is null
      "gateway_id": "<Patient monitor ID>",
      // List of previously connected sensors, only applicable for patient monitors.
      // If a sensor is being connected this list is empty.
      "connected_sensors": [
        {
          // ID of the sensor connected
          "primary_identifier": "<Sensor ID>",
          // Name of the sensor (Currently it uses the device code)
          "name": "<Sensor name>",
          // Type of device (i.e. ANNE Chest, ANNE Limb, etc.)
          "device_code": "<Sensor type>"
        }
      ],
      // List of device alerts for the current device (both active and inactive)
      "alerts": [],
      // Device configuration flags
      "config": {
        // Determines if the audio is enabled for the device
        "audio_enabled": true,
        // Determines if the audio is paused for the device
        "audio_pause_enabled": false
      }
    },
    // The patient assigned to the device. Only applicable for patient monitors.
    // The format can be seen on the "Patient session started" section
    "patient": {
      // ID of the patient (The one displayed to the user)
      "primary_identifier": "<Patient ID>",
      // Name of the patient
      "given_name": "<Patient Name>",
      // Last name of the patient
      "family_name": "<Patient Last name>",
      // Gender of the patient displayed as an HL7 gender value (https://terminology.hl7.org/5.1.0/CodeSystem-v2-0001.html)
      "gender": "<HL7 gender>",
      // DOB of the patient
      "birth_date": "<Date>",
      // List of physiological alerts for the patient (Both active and inactive)
      // Uses the same formatting as described on the "Alerts" section.
      "alerts": []
    }
  }
}
```

**Vital ranges updated**

```json
{
  "event_type": "DEVICE_NEW_VITALS_RANGES",
  "event_name": "Device new vitals ranges added",
  "message_id": "<UUID>",
  "timestamp": "<ISO format timestamp>",
  "payload": {
    // ID of the device being connected
    "primary_identifier": "<Patient monitor ID>",
    // List of updated device vital ranges
    "ranges": [
      {
        // Code of the vital range
        "code": "<Vital range code>",
        // Upper limit of the range (i.e. max value allowed before triggering an alarm)
        "upper_limit": 1.0,
        // Lower limit of the range
        "lower_limit": 2.0,
        // Determines if the alerts for the specified range are enabled or not.
        // When false, no alarms are triggered for this range.
        "alert_condition_enabled": false
      }
    ]
  }
}
```

**Patient admission rejected**

```json
{
  "event_type": "PATIENT_ADMISSION_REJECTED",
  "event_name": "Patient admission rejected",
  "message_id": "<UUID>",
  "timestamp": "<ISO format timestamp>",
  "payload": {
    // ID of the patient monitor where the patient was rejected
    "device_primary_identifier": "<Patient monitor ID>",
    // ID of the patient rejected
    "patient_primary_identifier": "<Patient ID>"
  }
}
```

**Patient session closed**

```json
{
  "event_type": "PATIENT_SESSION_CLOSED_EVENT",
  "event_name": "Patient session closed",
  "message_id": "<UUID>",
  "timestamp": "<ISO format timestamp>",
  "payload": {
    // ID of the patient monitor where the patient session was closed
    "device_primary_identifier": "<Patient monitor ID>",
    // ID of the patient whose session ended
    "patient_primary_identifier": "<Patient ID>"
  }
}
```

**Patient session started**

```json
{
  "event_type": "PATIENT_SESSION_STARTED",
  "event_name": "Patient session started",
  "message_id": "<UUID>",
  "timestamp": "<ISO format timestamp>",
  "payload": {
    // ID of the patient monitor where the patient session was started
    "patient_monitor_identifier": "<Patient monitor ID>",
    "patient": {
      // ID of the patient (The one displayed to the user)
      "primary_identifier": "<Patient ID>",
      // Name of the patient
      "given_name": "<Patient Name>",
      // Last name of the patient
      "family_name": "<Patient Last name>",
      // Gender of the patient displayed as an HL7 gender value (https://terminology.hl7.org/5.1.0/CodeSystem-v2-0001.html)
      "gender": "<HL7 gender>",
      // DOB of the patient
      "birth_date": "<Date>",
      // List of physiological alerts for the patient (Both active and inactive)
      // Uses the same formatting as described on the "Alerts" section.
      "alerts": []
    }
  }
}
```

**Patient monitor configuration updated**

```json
{
  "event_type": "PM_CONFIGURATION_UPDATED",
  "event_name": "PM configuration updated",
  "message_id": "<UUID>",
  "timestamp": "<ISO format timestamp>",
  "payload": {
    // ID of the patient monitor whose configuration is updated
    "device_primary_identifier": "<Patient monitor ID>",
    // Determines if the audio is enabled for the patient monitor
    "audio_enabled": true,
    // Determines if the audio is paused for the patient monitor
    "audio_pause_enabled": false
  }
}
```

**Health check**

```json
{
  "event_type": "PM_CONNECTION_STATUS_REPORT",
  "event_name": "PM connection status",
  "message_id": "<UUID>",
  "timestamp": "<ISO format timestamp>",
  "payload": {
    // Patient monitor whose the health check belongs to
    "device_primary_identifier": "<Patient monitor ID>",
    // Connection status is true while the monitor is connected.
    // If the PM gets disconnected it will be false and no more messages will be sent
    "connection_status": true
  }
}
```

**Sensor removed**

```json
{
  "event_type": "SENSOR_REMOVED_EVENT",
  "event_name": "Sensor removed",
  "message_id": "<UUID>",
  "timestamp": "<ISO format timestamp>",
  "payload": {
    // ID of the sensor being removed
    "device_primary_identifier": "<Device ID>",
    // ID of the patient assigned to the PM from which the sensor was removed
    "patient_primary_identifier": "<Patient ID>",
    // Timestamp of the device disconnection
    "determination_time": "<ISO format timestamp>"
  }
}
```

## Processed messages

These messages are triggered after the ANNE view events are processed by the backend (the `patient` microservice), meaning that the changes are already impacted to the backend API. Therefore, these are the messages that should be listened to when refreshing data through the API.

### Formatting

All processed events have this same format except for the `"event_state"`, `"previous_state"` and `"event_data"` which vary depending on the type of the event sent, identified by the `"event_type"` property.

```json
{
  // Type of the event being triggered. 
  // This determines the format of the "event_state", "previous_state", "event_data" fields.
  "event_type": "<Event type>",
  // Human readable event type
  "event_name": "<Event name>",
  // Internal ID of the entity being modified used by the backend, 
  // this will depend on the type of the event being sent.
  "entity_id": "<Entity ID>",
  // Time at which the event was sent
  "performed_on": "<ISO format date>",
  // User whose input triggered the event. 
  // In case of automatic events they are identified by the "system" user
  "performed_by": "<Username>",
  "event_state": {
    // Variable content depending on the event. 
    // This contains the new information of the modified object if any was modified.
  },
  "previous_state": {
    // Variable content depending on the event. 
    // This contains the previous information of the modified object if any was modified.
  },
  // TODO: THIS IS ALWAYS PATIENT, WHY?
  "entity_name": "patient",
  // TODO: THIS IS ALWAYS PATIENT, WHY?
  "emitted_by": "patient",
  // Unique ID identifying the current event
  "message_id": "<UUID>",
  "event_data": {
    // Variable content depending on the event. 
    // This contains the input payload of the event that was triggered, 
    // which comes from either a user input or an ANNE view event.
  }
}
```

### Beds

**Bed created event**

```json
{
  "event_type": "BED_CREATED_EVENT",
  "event_name": "Bed created",
  // Internal ID of the newly created bed
  "entity_id": "<Bed ID>",
  "performed_on": "<ISO format date>",
  "performed_by": "<Username>",
  // Data of the created bed
  "event_state": {
    // Internal ID of the newly created bed
    "id": "<Bed ID>",
    // Name of the bed displayed to the user
    "name": "<Bed name>"
  },
  // No previous state, as the bed was created.
  "previous_state": {},
  "entity_name": "patient",
  "emitted_by": "patient",
  "message_id": "<UUID>",
  // Input payload of the event.
  "event_data": {
    // Internal ID of the newly created bed
    "id": "<Bed ID>",
    // Name of the bed displayed to the user
    "name": "<Bed name>"
  }
}
```

**Bed updated event**

```json
{
  "event_type": "BED_UPDATED_EVENT",
  "event_name": "Bed updated",
  // Internal ID of the updated bed
  "entity_id": "<Bed ID>",
  "performed_on": "<ISO format date>",
  "performed_by": "<Username>",
  // Updated data of the bed
  "event_state": {
    // Internal ID of the bed
    "id": "<Bed ID>",
    // Name of the bed displayed to the user
    "name": "<Bed name>"
  },
  // Previous data of the bed.
  "previous_state": {
    // Internal ID of the bed
    "id": "<Bed ID>",
    // Previous name of the bed
    "name": "<Old Bed name>"
  },
  "entity_name": "patient",
  "emitted_by": "patient",
  "message_id": "<UUID>",
  // Input payload of the event.
  "event_data": {
    // Name of the bed displayed to the user
    "name": "<Bed name>"
  }
}
```

**Bed deleted event**

```json
{
  "event_type": "BED_DELETED_EVENT",
  "event_name": "Bed deleted",
  // Internal ID of the deleted bed
  "entity_id": "<Bed ID>",
  "performed_on": "<ISO format date>",
  "performed_by": "<Username>",
  // Data of the bed deleted
  "event_state": {
    // Internal ID of the bed
    "id": "<Bed ID>",
    // Name of the bed displayed to the user
    "name": "<Bed name>"
  },
  // Data of the bed deleted
  "previous_state": {
    // Internal ID of the bed
    "id": "<Bed ID>",
    // Name of the bed displayed to the user
    "name": "<Bed name>"
  },
  "entity_name": "patient",
  "emitted_by": "patient",
  "message_id": "<UUID>",
  // Input payload of the event.
  "event_data": {}
}
```

### Bed groups

**Bed group created event**

```json
{
  "event_type": "BED_GROUP_CREATED_EVENT",
  "event_name": "Bed group created",
  // Internal ID of the newly created bed group
  "entity_id": "<Bed group ID>",
  "performed_on": "<ISO format date>",
  "performed_by": "<Username>",
  // Data of the created bed group
  "event_state": {
    // Internal ID of the newly created bed group
    "id":  "<Bed group ID>",
    // Name of the bed group displayed to the user 
    "name": "<Bed group name>",
    // Description of the bed group (Unused)
    "description":  "<Bed group description>",
    // List of internal IDs of the beds assigned to the created bed group.
    // On creation the list is always empty.
    "beds": []
  },
  // No previous state, as the bed group was created.
  "previous_state": {},
  "entity_name": "patient",
  "emitted_by": "patient",
  "message_id": "<UUID>",
  // Input payload of the event.
  "event_data": {
    // Internal ID of the newly created bed group
    "id":  "<Bed group ID>",
    // Name of the bed group displayed to the user 
    "name": "<Bed group name>",
    // Description of the bed group (Unused)
    "description":  "<Bed group description>",
    // List of internal IDs of the beds assigned to the created bed group.
    // On creation the list is always empty.
    "beds": []
  }
}
```

**Bed group updated event**

```json
{
  "event_type": "BED_GROUP_UPDATED_EVENT",
  "event_name": "Bed group updated",
  // Internal ID of the bed group
  "entity_id": "<Bed group ID>",
  "performed_on": "<ISO format date>",
  "performed_by": "<Username>",
  // Data of the updated bed group
  "event_state": {
    // Internal ID of the bed group
    "id":  "<Bed group ID>",
    // Name of the bed group displayed to the user 
    "name": "<Bed group name>",
    // Description of the bed group (Unused)
    "description":  "<Bed group description>",
    // List of internal IDs of the beds assigned to the bed group.
    "beds": ["<Bed ID #1>", "<Bed ID #2>"]
  },
  // Previous data of the updated bed group
  "previous_state": {
    // Internal ID of the bed group
    "id":  "<Bed group ID>",
    // Name of the bed group displayed to the user 
    "name": "<Old bed group name>",
    // Description of the bed group (Unused)
    "description":  "<Old bed group description>",
    // List of internal IDs of the beds assigned to the bed group.
    "beds": ["<Bed ID #1>", "<Bed ID #1>"]
  },
  "entity_name": "patient",
  "emitted_by": "patient",
  "message_id": "<UUID>",
  // Input payload of the event.
  "event_data": {
    // Name of the bed group displayed to the user 
    "name": "<Bed group name>",
    // Description of the bed group (Unused)
    "description":  "<Bed group description>",
    // This field is always empty, as updating the bed group does not update the assigned beds.
    "beds": []
  }
}
```

**Bed group deleted event**

```json
{
  "event_type": "BED_GROUP_DELETED_EVENT",
  "event_name": "Bed group deleted",
  // Internal ID of the bed group
  "entity_id": "<Bed group ID>",
  "performed_on": "<ISO format date>",
  "performed_by": "<Username>",
  // Data of the deleted bed group
  "event_state": {
    // Internal ID of the bed group
    "id":  "<Bed group ID>",
    // Name of the bed group displayed to the user 
    "name": "<Bed group name>",
    // Description of the bed group (Unused)
    "description":  "<Bed group description>",
    // List of internal IDs of the beds assigned to the bed group.
    "beds": ["<Bed ID #1>", "<Bed ID #1>"]
  },
  // Data of the deleted bed group
  "previous_state": {
    // Internal ID of the bed group
    "id":  "<Bed group ID>",
    // Name of the bed group displayed to the user 
    "name": "<Bed group name>",
    // Description of the bed group (Unused)
    "description":  "<Bed group description>",
    // List of internal IDs of the beds assigned to the bed group.
    "beds": ["<Bed ID #1>", "<Bed ID #2>"]
  },
  "entity_name": "patient",
  "emitted_by": "patient",
  "message_id": "<UUID>",
  // Input payload of the event.
  "event_data": {}
}
```

**Bed assigned to group event**

```json
{
  "event_type": "BED_ASSIGNED_TO_GROUP_EVENT",
  "event_name": "Bed added to group",
  // Internal ID of the bed group
  "entity_id": "<Bed group ID>",
  "performed_on": "<ISO format date>",
  "performed_by": "<Username>",
  // Data of the bed group where the bed was added
  "event_state": {
    // Internal ID of the bed group
    "id":  "<Bed group ID>",
    // Name of the bed group displayed to the user 
    "name": "<Bed group name>",
    // Description of the bed group (Unused)
    "description":  "<Bed group description>",
    // List of internal IDs of the beds assigned to the bed group.
    "beds": ["<Bed ID #1>", "<Bed ID #2>", "<New Bed ID>"]
  },
  // Data of the bed group before the bed was added
  "previous_state": {
    // Internal ID of the bed group
    "id":  "<Bed group ID>",
    // Name of the bed group displayed to the user 
    "name": "<Bed group name>",
    // Description of the bed group (Unused)
    "description":  "<Bed group description>",
    // List of internal IDs of the beds assigned to the bed group.
    "beds": ["<Bed ID #1>", "<Bed ID #2>"]
  },
  "entity_name": "patient",
  "emitted_by": "patient",
  "message_id": "<UUID>",
  // Input payload of the event.
  "event_data": {
    // Bed being added to the bed group
    "bed": {
      // Internal ID of the bed
      "id": "<New Bed ID>",
      // Name of the bed displayed to the user
      "name": "<Bed name>"
    }
  }
}
```

**Bed removed from group event**

```json
{
  "event_type": "BED_REMOVED_FROM_GROUP_EVENT",
  "event_name": "Bed removed from group",
  // Internal ID of the bed group
  "entity_id": "<Bed group ID>",
  "performed_on": "<ISO format date>",
  "performed_by": "<Username>",
  // Data of the bed group where the bed was removed
  "event_state": {
    // Internal ID of the bed group
    "id":  "<Bed group ID>",
    // Name of the bed group displayed to the user 
    "name": "<Bed group name>",
    // Description of the bed group (Unused)
    "description":  "<Bed group description>",
    // List of internal IDs of the beds assigned to the bed group.
    "beds": ["<Bed ID #1>", "<Bed ID #2>"]
  },
  // Data of the bed group before the bed was removed
  "previous_state": {
    // Internal ID of the bed group
    "id":  "<Bed group ID>",
    // Name of the bed group displayed to the user 
    "name": "<Bed group name>",
    // Description of the bed group (Unused)
    "description":  "<Bed group description>",
    // List of internal IDs of the beds assigned to the bed group.
    "beds": ["<Bed ID #1>", "<Bed ID #2>", "<Bed ID removed>"]
  },
  "entity_name": "patient",
  "emitted_by": "patient",
  "message_id": "<UUID>",
  // Input payload of the event.
  "event_data": {
    // Bed being removed from the bed group
    "bed": {
      // Internal ID of the bed
      "id": "<Bed ID removed>",
      // Name of the bed displayed to the user
      "name": "<Bed name>"
    }
  }
}
```

### Devices

All device events create, update or delete devices, meaning all `event_state` and `previous_state` objects have the following format:

```json
{
  // Internal ID of the device.
  "id": "<Device ID>",
  // ID of the device displayed to the user.
  "primary_identifier": "<Device primary identifier>",
  // Type of device (Patient Monitor, ANNE Chest, etc.).
  "model_number": "<Device type>",
  // Name of the device (Currently using the same as device type).
  "name": "<Device name>",
  // ID of the bed where the device is assigned to.
  "location_id": "<Bed ID>",
  // If the device is a sensor, this field contains the ID of the PM that this sensor is attached to.
  // If the device is a PM, this field is null.
  "gateway_id": "<Another device ID>",
  // Boolean flag indicating if the audio alarms are paused for the device.
  "audio_pause_enabled": false,
  // Boolean flag indicating if the audio alarms are disabled for the device.
  "audio_enabled": true
}
```


**Device created event**

```json
{
  "event_type": "DEVICE_CREATED_EVENT",
  "event_name": "Device Created",
  // Internal ID of the device
  "entity_id": "<Device ID>",
  "performed_on": "<ISO format date>",
  "performed_by": "<Username>",
  // Data of the created device
  "event_state": {
    "id": "<Device ID>",
    "primary_identifier": "<Device primary identifier>",
    "model_number": "<Device type>",
    "name": "<Device name>",
    "location_id": "<Bed ID>",
    "gateway_id": "<Another device ID>",
    "audio_pause_enabled": false,
    "audio_enabled": true
  },
  // No previous state, as the device was created.
  "previous_state": {},
  "entity_name": "patient",
  "emitted_by": "patient",
  "message_id": "<UUID>",
  "event_data": {}
}
```

**Device deleted event**

```json
{
  "event_type": "DEVICE_DELETED_EVENT",
  "event_name": "Device deleted",
  // TODO: WHY IS THIS FIELD LIKE THIS?
  // Internal ID of the patient assigned to the device if assigned, 
  // otherwise it contains the internal ID of the device
  "entity_id": "<Patient ID | Device ID>",
  "performed_on": "<ISO format date>",
  "performed_by": "<Username>",
  // Data of the deleted device
  "event_state": {
    "id": "<Device ID>",
    "primary_identifier": "<Device primary identifier>",
    "model_number": "<Device type>",
    "name": "<Device name>",
    "location_id": "<Bed ID>",
    "gateway_id": "<Another device ID>",
    "audio_pause_enabled": false,
    "audio_enabled": true
  },
  // Data of the deleted device
  "previous_state": {
    "id": "<Device ID>",
    "primary_identifier": "<Device primary identifier>",
    "model_number": "<Device type>",
    "name": "<Device name>",
    "location_id": "<Bed ID>",
    "gateway_id": "<Another device ID>",
    "audio_pause_enabled": false,
    "audio_enabled": true
  },
  "entity_name": "patient",
  "emitted_by": "patient",
  "message_id": "<UUID>",
  "event_data": {}
}
```

**Device updated event**

```json
{
  "event_type": "DEVICE_UPDATED_EVENT",
  "event_name": "Device information updated",
  // Internal ID of the device
  "entity_id": "<Device ID>",
  "performed_on": "<ISO format date>",
  "performed_by": "<Username>",
  // Data of the updated device
  "event_state": {
    "id": "<Device ID>",
    "primary_identifier": "<Device primary identifier>",
    "model_number": "<Device type>",
    "name": "<Device name>",
    "location_id": "<Bed ID>",
    "gateway_id": "<Another device ID>",
    "audio_pause_enabled": false,
    "audio_enabled": true
  },
  // Previous device data
  "previous_state": {
    "id": "<Device ID>",
    "primary_identifier": "<Device primary identifier>",
    "model_number": "<Device type>",
    "name": "<Device name>",
    "location_id": "<Bed ID>",
    "gateway_id": "<Another device ID>",
    "audio_pause_enabled": false,
    "audio_enabled": true
  },
  "entity_name": "patient",
  "emitted_by": "patient",
  "message_id": "<UUID>",
  "event_data": {}
}
```

**Device config updated event**

This event is triggered when modifying the `audio_pause_enabled` and `audio_enabled` flags only, when any other value is modified it triggers the `DEVICE_UPDATED_EVENT`.

```json
{
  "event_type": "DEVICE_CONFIG_UPDATED_EVENT",
  "event_name": "Device configuration updated",
  // Internal ID of the device
  "entity_id": "<Device ID>",
  "performed_on": "<ISO format date>",
  "performed_by": "<Username>",
  // Data of the updated device
  "event_state": {
    "id": "<Device ID>",
    "primary_identifier": "<Device primary identifier>",
    "model_number": "<Device type>",
    "name": "<Device name>",
    "location_id": "<Bed ID>",
    "gateway_id": "<Another device ID>",
    "audio_pause_enabled": false,
    "audio_enabled": true
  },
  // Previous device data
  "previous_state": {
    "id": "<Device ID>",
    "primary_identifier": "<Device primary identifier>",
    "model_number": "<Device type>",
    "name": "<Device name>",
    "location_id": "<Bed ID>",
    "gateway_id": "<Another device ID>",
    "audio_pause_enabled": false,
    "audio_enabled": true
  },
  "entity_name": "patient",
  "emitted_by": "patient",
  "message_id": "<UUID>",
  "event_data": {}
}
```

**Assign device location**

```json
{
  "event_type": "ASSIGN_DEVICE_LOCATION_EVENT",
  "event_name": "Assign location to device",
  // Internal ID of the device
  "entity_id": "<Device ID>",
  "performed_on": "<ISO format date>",
  "performed_by": "<Username>",
  // Data of the updated device
  "event_state": {
    "id": "<Device ID>",
    "primary_identifier": "<Device primary identifier>",
    "model_number": "<Device type>",
    "name": "<Device name>",
    "location_id": "<Bed ID>",
    "gateway_id": "<Another device ID>",
    "audio_pause_enabled": false,
    "audio_enabled": true
  },
  // Previous device data
  "previous_state": {
    "id": "<Device ID>",
    "primary_identifier": "<Device primary identifier>",
    "model_number": "<Device type>",
    "name": "<Device name>",
    "location_id": "<Bed ID>",
    "gateway_id": "<Another device ID>",
    "audio_pause_enabled": false,
    "audio_enabled": true
  },
  "entity_name": "patient",
  "emitted_by": "patient",
  "message_id": "<UUID>",
  "event_data": {}
}
```

**Unassign device location**

```json
{
  "event_type": "UNASSIGN_DEVICE_LOCATION_EVENT",
  "event_name": "Unassign location",
  // Internal ID of the device
  "entity_id": "<Device ID>",
  "performed_on": "<ISO format date>",
  "performed_by": "<Username>",
  // Data of the updated device
  "event_state": {
    "id": "<Device ID>",
    "primary_identifier": "<Device primary identifier>",
    "model_number": "<Device type>",
    "name": "<Device name>",
    "location_id": "<Bed ID>",
    "gateway_id": "<Another device ID>",
    "audio_pause_enabled": false,
    "audio_enabled": true
  },
  // Previous device data
  "previous_state": {
    "id": "<Device ID>",
    "primary_identifier": "<Device primary identifier>",
    "model_number": "<Device type>",
    "name": "<Device name>",
    "location_id": "<Bed ID>",
    "gateway_id": "<Another device ID>",
    "audio_pause_enabled": false,
    "audio_enabled": true
  },
  "entity_name": "patient",
  "emitted_by": "patient",
  "message_id": "<UUID>",
  "event_data": {}
}
```

### Vital ranges

These events modify vital ranges objects, therefore all `event_state` and `previous_state` objects have the same format, which is described here:

```json
{
  // Internal ID of the vital range
  "id": "<Vital range ID>",
  // Code identifying the vital range
  "code": "<Vital range code>",
  // Upper limit
  "upper_limit": 1.0,
  // Lower limit
  "lower_limit": 0.0,
  // Internal ID of the device that this vital range belongs to
  "device_id": "<Device ID>"
}
```

**Create vital ranges**

```json
{
  "event_type": "VITAL_RANGE_CREATED_EVENT",
  "event_name": "Vital Range Created",
  // Internal ID of the vital range.
  "entity_id": "<Vital range ID>",
  "performed_on": "<ISO format date>",
  "performed_by": "<Username>",
  // Data of the created vital range.
  "event_state": {
    "id": "<Vital range ID>",
    "code": "<Vital range code>",
    "upper_limit": 1.0,
    "lower_limit": 0.0,
    "device_id": "<Device ID>"
  },
  // No previous state, as the vital range was just created.
  "previous_state": {},
  "entity_name": "patient",
  "emitted_by": "patient",
  "message_id": "<UUID>",
  "event_data": {}
}
```

**Delete vital ranges**

```json
{
  "event_type": "VITAL_RANGE_DELETED_EVENT",
  "event_name": "Device information updated",
  // Internal ID of the vital range.
  "entity_id": "<Vital range ID>",
  "performed_on": "<ISO format date>",
  "performed_by": "<Username>",
  // Data of the created vital range.
  "event_state": {
    "id": "<Vital range ID>",
    "code": "<Vital range code>",
    "upper_limit": 1.0,
    "lower_limit": 0.0,
    "device_id": "<Device ID>"
  },
  // Previous vital range data.
  "previous_state": {
    "id": "<Vital range ID>",
    "code": "<Vital range code>",
    "upper_limit": 1.0,
    "lower_limit": 0.0,
    "device_id": "<Device ID>"
  },
  "entity_name": "patient",
  "emitted_by": "patient",
  "message_id": "<UUID>",
  "event_data": {}
}
```

### Device alerts

These events modify device alert objects, therefore all `event_state` and `previous_state` objects have the same format, which is described here:

```json
{
  // Internal ID of the alert
  "id": "<Device alert ID>",
  // Code identifying the type of alert
  "code": "<Device alert code>",
  // Device that this alert belongs to
  "device_id": "<Device ID>",
  // Priority of the alert
  "priority": "<HI | ME | LO>"
}
```

**Create device alert**

```json
{
  "event_type": "DEVICE_ALERT_CREATED",
  "event_name": "Device Alert Created",
  // Internal ID of the device alert.
  "entity_id": "<Device alert ID>",
  "performed_on": "<ISO format date>",
  "performed_by": "<Username>",
  // Data of the created device alert.
  "event_state": {
    "id": "<Device alert ID>",
    "code": "<Device alert code>",
    "device_id": "<Device ID>",
    "priority": "<HI | ME | LO>"
  },
  // No previous state, as the device alert was just created.
  "previous_state": {},
  "entity_name": "patient",
  "emitted_by": "patient",
  "message_id": "<UUID>",
  "event_data": {}
}
```

**Update device alert**

```json
{
  "event_type": "DEVICE_ALERT_UPDATED",
  "event_name": "Device Alert Updated",
  // Internal ID of the device alert.
  "entity_id": "<Device alert ID>",
  "performed_on": "<ISO format date>",
  "performed_by": "<Username>",
  // Data of the device alert.
  "event_state": {
    "id": "<Device alert ID>",
    "code": "<Device alert code>",
    "device_id": "<Device ID>",
    "priority": "<HI | ME | LO>"
  },
  // Previous data of the device alert.
  "previous_state": {
    "id": "<Device alert ID>",
    "code": "<Device alert code>",
    "device_id": "<Device ID>",
    "priority": "<HI | ME | LO>"
  },
  "entity_name": "patient",
  "emitted_by": "patient",
  "message_id": "<UUID>",
  "event_data": {}
}
```

**Delete device alert**

```json
{
  "event_type": "DEVICE_ALERT_DELETED",
  "event_name": "Device Alert Deleted",
  // Internal ID of the device alert.
  "entity_id": "<Device alert ID>",
  "performed_on": "<ISO format date>",
  "performed_by": "<Username>",
  // Data of the device alert.
  "event_state": {
    "id": "<Device alert ID>",
    "code": "<Device alert code>",
    "device_id": "<Device ID>",
    "priority": "<HI | ME | LO>"
  },
  // Previous data of the device alert.
  "previous_state": {
    "id": "<Device alert ID>",
    "code": "<Device alert code>",
    "device_id": "<Device ID>",
    "priority": "<HI | ME | LO>"
  },
  "entity_name": "patient",
  "emitted_by": "patient",
  "message_id": "<UUID>",
  "event_data": {}
}
```

**Multiple device alerts triggered**

This message is triggered when multiple alerts are modified in a single transaction. This is the case when a PM is connected and all alerts are retrieved

```json
{
  "event_type": "MULTIPLE_DEVICE_ALERTS_UPDATED",
  "event_name": "Multiple Device Alerts Updated",
  // Internal ID of the device that the alerts belong to.
  "entity_id": "<Device ID>",
  "performed_on": "<ISO format date>",
  "performed_by": "<Username>",
  // No data sent here as this event modifies multiple objects.
  "event_state": {},
  // No data sent here as this event modifies multiple objects.
  "previous_state": {},
  "entity_name": "patient",
  "emitted_by": "patient",
  "message_id": "<UUID>",
  "event_data": {}
}
```

### Patients

These events modify patient objects, therefore all `event_state` and `previous_state` objects have the same format, which is described here:

```json
{
  // Internal ID of the patient
  "id": "<Patient ID>",
  // ID of the patient displayed to the user
  "primary_identifier": "<Patient primary identifier>",
  // Patient's name
  "given_name": "<Patient name>",
  // Patient's last name
  "family_name": "<Patient last name>",
  // Patient's gender as an HL7 gender value (https://terminology.hl7.org/5.1.0/CodeSystem-v2-0001.html)
  "gender": "<Patient gender>",
  // Patient's birth date in ISO format
  "birth_date": "<ISO format date>",
  // Flag to determine if the patient is active
  "active": true
}
```

**Patient created event**

```json
{
  "event_type": "PATIENT_CREATED_EVENT",
  "event_name": "Patient Created",
  // Internal ID of the patient.
  "entity_id": "<Patient ID>",
  "performed_on": "<ISO format date>",
  "performed_by": "<Username>",
  // Data of the created patient.
  "event_state": {
    "id": "<Patient ID>",
    "primary_identifier": "<Patient primary identifier>",
    "given_name": "<Patient name>",
    "family_name": "<Patient last name>",
    "gender": "<Patient gender>",
    "birth_date": "<ISO format date>",
    "active": true
  },
  // No previous state, as the patient was just created.
  "previous_state": {},
  "entity_name": "patient",
  "emitted_by": "patient",
  "message_id": "<UUID>",
  // Input of the event.
  "event_data": {
    "id": "<Patient ID>",
    "primary_identifier": "<Patient primary identifier>",
    "given_name": "<Patient name>",
    "family_name": "<Patient last name>",
    "gender": "<Patient gender>",
    "birth_date": "<ISO format date>",
    "active": true
  }
}
```

**Patient updated event**

```json
{
  "event_type": "UPDATE_PATIENT_INFO_EVENT",
  "event_name": "Patient personal information updated",
  // Internal ID of the patient.
  "entity_id": "<Patient ID>",
  "performed_on": "<ISO format date>",
  "performed_by": "<Username>",
  // Data of the updated patient.
  "event_state": {
    "id": "<Patient ID>",
    "primary_identifier": "<Patient primary identifier>",
    "given_name": "<Patient name>",
    "family_name": "<Patient last name>",
    "gender": "<Patient gender>",
    "birth_date": "<ISO format date>",
    "active": true
  },
  // Previous patient's data.
  "previous_state": {
    "id": "<Patient ID>",
    "primary_identifier": "<Patient primary identifier>",
    "given_name": "<Patient name>",
    "family_name": "<Patient last name>",
    "gender": "<Patient gender>",
    "birth_date": "<ISO format date>",
    "active": true
  },
  "entity_name": "patient",
  "emitted_by": "patient",
  "message_id": "<UUID>",
  // Input of the event.
  "event_data": {
    "id": "<Patient ID>",
    "primary_identifier": "<Patient primary identifier>",
    "given_name": "<Patient name>",
    "family_name": "<Patient last name>",
    "gender": "<Patient gender>",
    "birth_date": "<ISO format date>",
    "active": true
  }
}
```

**Delete patient event**

```json
{
  "event_type": "PATIENT_DELETED_EVENT",
  "event_name": "Patient Deleted",
  // Internal ID of the patient.
  "entity_id": "<Patient ID>",
  "performed_on": "<ISO format date>",
  "performed_by": "<Username>",
  // Data of the deleted patient.
  "event_state": {
    "id": "<Patient ID>",
    "primary_identifier": "<Patient primary identifier>",
    "given_name": "<Patient name>",
    "family_name": "<Patient last name>",
    "gender": "<Patient gender>",
    "birth_date": "<ISO format date>",
    "active": true
  },
  // Previous patient's data.
  "previous_state": {
    "id": "<Patient ID>",
    "primary_identifier": "<Patient primary identifier>",
    "given_name": "<Patient name>",
    "family_name": "<Patient last name>",
    "gender": "<Patient gender>",
    "birth_date": "<ISO format date>",
    "active": true
  },
  "entity_name": "patient",
  "emitted_by": "patient",
  "message_id": "<UUID>",
  // Input of the event.
  "event_data": {}
}
```

### Physiological alerts

These events modify physiological alert objects, therefore all `event_state` and `previous_state` params have the same format, which is described here:

```json
{
  // Internal ID of the alert
  "id": "<Physiological alert ID>",
  // Code identifying the type of alert
  "code": "<Physiological alert code>",
  // Time that the alert was triggered for the first time
  "effective_dt": "<ISO format date>",
  // ID of the patient that the alert belongs to
  "subject_id": "<Patient ID>",
  // Priority of the alert
  "value_text": "<Alert priority>",
  // Indicates if the observation is an alert. At the moment the only observations triggered are physiological alerts, so it is always true.
  "is_alert": true,
  // TODO: WHY DO WE STILL HAVE THIS VALUES?
  // Unused attribute
  "category": "vital-signs",
  // Unused attribute
  "value_number": null
}
```

**Physiological alert created event**

```json
{
  "event_type": "OBSERVATION_CREATED_EVENT",
  "event_name": "Observation Created",
  // Internal ID of the alert.
  "entity_id": "<Observation ID>",
  "performed_on": "<ISO format date>",
  "performed_by": "<Username>",
  // Data of the created alert.
  "event_state": {
    "id": "<Physiological alert ID>",
    "code": "<Physiological alert code>",
    "effective_dt": "<ISO format date>",
    "subject_id": "<Patient ID>",
    "value_text": "<Alert priority>",
    "is_alert": true,
    "category": "vital-signs",
    "value_number": null
  },
  // No previous state, as the alert was just created.
  "previous_state": {},
  "entity_name": "patient",
  "emitted_by": "patient",
  "message_id": "<UUID>",
  // Input of the event.
  "event_data": {
    "id": "<Patient ID>",
    "primary_identifier": "<Patient primary identifier>",
    "given_name": "<Patient name>",
    "family_name": "<Patient last name>",
    "gender": "<Patient gender>",
    "birth_date": "<ISO format date>",
    "active": true
  }
}
```

**Physiological alert deleted event**

```json
{
  "event_type": "OBSERVATION_DELETED_EVENT",
  "event_name": "Observation Deleted",
  // Internal ID of the alert.
  "entity_id": "<Observation ID>",
  "performed_on": "<ISO format date>",
  "performed_by": "<Username>",
  // Data of the deleted alert.
  "event_state": {
    "id": "<Physiological alert ID>",
    "code": "<Physiological alert code>",
    "effective_dt": "<ISO format date>",
    "subject_id": "<Patient ID>",
    "value_text": "<Alert priority>",
    "is_alert": true,
    "category": "vital-signs",
    "value_number": null
  },
  // Previous data of the deleted alert.
  "previous_state": {
    "id": "<Physiological alert ID>",
    "code": "<Physiological alert code>",
    "effective_dt": "<ISO format date>",
    "subject_id": "<Patient ID>",
    "value_text": "<Alert priority>",
    "is_alert": true,
    "category": "vital-signs",
    "value_number": null
  },
  "entity_name": "patient",
  "emitted_by": "patient",
  "message_id": "<UUID>",
  // Input of the event.
  "event_data": {}
}
```

**Multiple Physiological alerts modified event**

```json
{
  "event_type": "MULTIPLE_OBSERVATIONS_UPDATED",
  "event_name": "Multiple Observations Updated",
  // Internal ID of the device that the alerts belong to.
  "entity_id": "<Device ID>",
  "performed_on": "<ISO format date>",
  "performed_by": "<Username>",
  // No data sent here as this event modifies multiple objects.
  "event_state": {},
  // No data sent here as this event modifies multiple objects.
  "previous_state": {},
  "entity_name": "patient",
  "emitted_by": "patient",
  "message_id": "<UUID>",
  // Input of the event.
  "event_data": {}
}
```

### Alert logs

These events modify alert log objects, therefore all `event_state` and `previous_state` params have the same format, which is described here:

```json
{
  // Code that identifies the alert
  "code": "<Alert code>",
  // Indicates if this event is for the alert being activated or deactivated
  "active": true,
  // Alert's priority
  "value_text": "<Alert priority (HI | ME | LO)>",
  // Internal ID of the patient that the alert belongs to.
  "patient_id": "<Patient ID>",
  // Identifier shown to the user of the patient that the alert belongs to.
  "patient_primary_identifier": "<Patient primary identifier>",
  // Type of device that triggered the alert.
  "device_code": "<Device type>",
  // Time that the event occurred, if it is active it shows the time the alert started,
  // otherwise it shows the time the alert stopped
  "determination_time": "<ISO format date>",
  // Identifier shown to the user belonging to the device that triggered the alert.
  "device_primary_identifier": "<Device primary identifier>",
  // Value of the vital range upper limit at the time of the alert triggering. 
  "trigger_upper_limit": 2.0,
  // Value of the vital range lower limit at the time of the alert triggering.
  "trigger_lower_limit": 1.0
}
```

**Create active alert log event**

```json
{
  "event_type": "ALERT_ACTIVATED_EVENT",
  "event_name": "Alert activated",
  // Internal ID of the patient that triggered/disabled the alert.
  "entity_id": "<Patient ID>",
  "performed_on": "<ISO format date>",
  "performed_by": "<Username>",
  // Data of the created alert log.
  "event_state": {
    "code": "<Alert code>",
    "active": true,
    "value_text": "<Alert priority (HI | ME | LO)>",
    "patient_id": "<Patient ID>",
    "patient_primary_identifier": "<Patient primary identifier>",
    "device_code": "<Device type>",
    "determination_time": "<ISO format date>",
    "device_primary_identifier": "<Device primary identifier>",
    "trigger_upper_limit": 2.0,
    "trigger_lower_limit": 1.0
  },
  // No previous state, as the alert log was just created.
  "previous_state": {},
  "entity_name": "patient",
  "emitted_by": "patient",
  "message_id": "<UUID>",
  // Input of the event.
  "event_data": {
    "code": "<Alert code>",
    "active": true,
    "value_text": "<Alert priority (HI | ME | LO)>",
    "patient_id": "<Patient ID>",
    "patient_primary_identifier": "<Patient primary identifier>",
    "device_code": "<Device type>",
    "determination_time": "<ISO format date>",
    "device_primary_identifier": "<Device primary identifier>",
    "trigger_upper_limit": 2.0,
    "trigger_lower_limit": 1.0
  }
}
```

**Create inactive alert log event**

```json
{
  "event_type": "ALERT_DEACTIVATED_EVENT",
  "event_name": "Alert deactivated",
  // Internal ID of the patient that triggered/disabled the alert.
  "entity_id": "<Patient ID>",
  "performed_on": "<ISO format date>",
  "performed_by": "<Username>",
  // Data of the created alert log.
  "event_state": {
    "code": "<Alert code>",
    "active": false,
    "value_text": "<Alert priority (HI | ME | LO)>",
    "patient_id": "<Patient ID>",
    "patient_primary_identifier": "<Patient primary identifier>",
    "device_code": "<Device type>",
    "determination_time": "<ISO format date>",
    "device_primary_identifier": "<Device primary identifier>",
    "trigger_upper_limit": 2.0,
    "trigger_lower_limit": 1.0
  },
  // No previous state, as the alert log was just created.
  "previous_state": {},
  "entity_name": "patient",
  "emitted_by": "patient",
  "message_id": "<UUID>",
  // Input of the event.
  "event_data": {
    "code": "<Alert code>",
    "active": false,
    "value_text": "<Alert priority (HI | ME | LO)>",
    "patient_id": "<Patient ID>",
    "patient_primary_identifier": "<Patient primary identifier>",
    "device_code": "<Device type>",
    "determination_time": "<ISO format date>",
    "device_primary_identifier": "<Device primary identifier>",
    "trigger_upper_limit": 2.0,
    "trigger_lower_limit": 1.0
  }
}
```

### Encounters

These events modify encounter objects, therefore all `event_state` and `previous_state` params have the same format, which is described here:

```json
{
  // Internal ID of the encounter
  "id": "<Encounter ID>",
  // Status of the encounter
  "status": "<Encounter status (planned | in-progress | completed | cancelled)>",
  // Time of creation of the encounter (Not to be confused with the start time, 
  //   as it can be earlier depending on the delay of the network)
  "created_at": "<ISO format date>",
  // Time that the encounter started
  "start_time": "<ISO format date>",
  // Time that the encounter transition to either completed or cancelled
  "end_time": "<ISO format date>",
  // Device assigned to the encounter. Uses the same format as processed devices events.
  "device": {
    "id": "<Device ID>",
    "primary_identifier": "<Device primary identifier>",
    "model_number": "<Device type>",
    "name": "<Device name>",
    "location_id": "<Bed ID>",
    "gateway_id": "<Another device ID>",
    "audio_pause_enabled": false,
    "audio_enabled": true
  },
  // Patient assigned to the encounter. Uses the same format as processed patient events.
  "patient": {
    "id": "<Patient ID>",
    "primary_identifier": "<Patient primary identifier>",
    "given_name": "<Patient name>",
    "family_name": "<Patient last name>",
    "gender": "<Patient gender>",
    "birth_date": "<ISO format date>",
    "active": true
  }
}
```

**Patient encounter planned event**

```json
{
  "event_type": "PATIENT_ENCOUNTER_PLANNED",
  "event_name": "Patient admission planned",
  // Internal ID of the patient assigned to the encounter.
  "entity_id": "<Patient ID>",
  "performed_on": "<ISO format date>",
  "performed_by": "<Username>",
  // Data of the encounter.
  "event_state": {
    "id": "<Encounter ID>",
    "status": "planned",
    "created_at": "<ISO format date>",
    "start_time": "<ISO format date>",
    "end_time": "<ISO format date>",
    "device": {
      "id": "<Device ID>",
      "primary_identifier": "<Device primary identifier>",
      "model_number": "<Device type>",
      "name": "<Device name>",
      "location_id": "<Bed ID>",
      "gateway_id": "<Another device ID>",
      "audio_pause_enabled": false,
      "audio_enabled": true
    },
    "patient": {
      "id": "<Patient ID>",
      "primary_identifier": "<Patient primary identifier>",
      "given_name": "<Patient name>",
      "family_name": "<Patient last name>",
      "gender": "<Patient gender>",
      "birth_date": "<ISO format date>",
      "active": true
    }
  },
  // No previous state, as the alert was just created.
  "previous_state": {},
  "entity_name": "patient",
  "emitted_by": "patient",
  "message_id": "<UUID>",
  // Input of the event.
  "event_data": {}
}
```

**Patient encounter started event**

```json
{
  "event_type": "PATIENT_ENCOUNTER_STARTED",
  "event_name": "Patient admitted",
  // Internal ID of the patient assigned to the encounter.
  "entity_id": "<Patient ID>",
  "performed_on": "<ISO format date>",
  "performed_by": "<Username>",
  // Data of the encounter.
  "event_state": {
    "id": "<Encounter ID>",
    "status": "in-progress",
    "created_at": "<ISO format date>",
    "start_time": "<ISO format date>",
    "end_time": "<ISO format date>",
    "device": {
      "id": "<Device ID>",
      "primary_identifier": "<Device primary identifier>",
      "model_number": "<Device type>",
      "name": "<Device name>",
      "location_id": "<Bed ID>",
      "gateway_id": "<Another device ID>",
      "audio_pause_enabled": false,
      "audio_enabled": true
    },
    "patient": {
      "id": "<Patient ID>",
      "primary_identifier": "<Patient primary identifier>",
      "given_name": "<Patient name>",
      "family_name": "<Patient last name>",
      "gender": "<Patient gender>",
      "birth_date": "<ISO format date>",
      "active": true
    }
  },
  // Previous data for the started encounter. 
  // It may be empty if the encounter was created as planned (ANNE view quick admit).
  "previous_state": {
    "id": "<Encounter ID>",
    "status": "planned",
    "created_at": "<ISO format date>",
    "start_time": "<ISO format date>",
    "end_time": "<ISO format date>",
    "device": {
      "id": "<Device ID>",
      "primary_identifier": "<Device primary identifier>",
      "model_number": "<Device type>",
      "name": "<Device name>",
      "location_id": "<Bed ID>",
      "gateway_id": "<Another device ID>",
      "audio_pause_enabled": false,
      "audio_enabled": true
    },
    "patient": {
      "id": "<Patient ID>",
      "primary_identifier": "<Patient primary identifier>",
      "given_name": "<Patient name>",
      "family_name": "<Patient last name>",
      "gender": "<Patient gender>",
      "birth_date": "<ISO format date>",
      "active": true
    }
  },
  "entity_name": "patient",
  "emitted_by": "patient",
  "message_id": "<UUID>",
  // Input of the event.
  "event_data": {}
}
```

**Patient encounter cancelled event**

```json
{
  "event_type": "PATIENT_ENCOUNTER_CANCELLED",
  "event_name": "Encounter cancelled",
  // Internal ID of the encounter.
  "entity_id": "<Encounter ID>",
  "performed_on": "<ISO format date>",
  "performed_by": "<Username>",
  // Data of the encounter.
  "event_state": {
    "id": "<Encounter ID>",
    "status": "cancelled",
    "created_at": "<ISO format date>",
    "start_time": "<ISO format date>",
    "end_time": "<ISO format date>",
    "device": {
      "id": "<Device ID>",
      "primary_identifier": "<Device primary identifier>",
      "model_number": "<Device type>",
      "name": "<Device name>",
      "location_id": "<Bed ID>",
      "gateway_id": "<Another device ID>",
      "audio_pause_enabled": false,
      "audio_enabled": true
    },
    "patient": {
      "id": "<Patient ID>",
      "primary_identifier": "<Patient primary identifier>",
      "given_name": "<Patient name>",
      "family_name": "<Patient last name>",
      "gender": "<Patient gender>",
      "birth_date": "<ISO format date>",
      "active": true
    }
  },
  // Previous data for the encounter.
  "previous_state": {
    "id": "<Encounter ID>",
    "status": "in-progress",
    "created_at": "<ISO format date>",
    "start_time": "<ISO format date>",
    "end_time": "<ISO format date>",
    "device": {
      "id": "<Device ID>",
      "primary_identifier": "<Device primary identifier>",
      "model_number": "<Device type>",
      "name": "<Device name>",
      "location_id": "<Bed ID>",
      "gateway_id": "<Another device ID>",
      "audio_pause_enabled": false,
      "audio_enabled": true
    },
    "patient": {
      "id": "<Patient ID>",
      "primary_identifier": "<Patient primary identifier>",
      "given_name": "<Patient name>",
      "family_name": "<Patient last name>",
      "gender": "<Patient gender>",
      "birth_date": "<ISO format date>",
      "active": true
    }
  },
  "entity_name": "patient",
  "emitted_by": "patient",
  "message_id": "<UUID>",
  // Input of the event.
  "event_data": {}
}
```

**Patient encounter completed event**

```json
{
  "event_type": "PATIENT_ENCOUNTER_COMPLETED",
  "event_name": "Encounter completed",
  // Internal ID of the patient assigned to the encounter.
  "entity_id": "<Patient ID>",
  "performed_on": "<ISO format date>",
  "performed_by": "<Username>",
  // Data of the encounter.
  "event_state": {
    "id": "<Encounter ID>",
    "status": "completed",
    "created_at": "<ISO format date>",
    "start_time": "<ISO format date>",
    "end_time": "<ISO format date>",
    "device": {
      "id": "<Device ID>",
      "primary_identifier": "<Device primary identifier>",
      "model_number": "<Device type>",
      "name": "<Device name>",
      "location_id": "<Bed ID>",
      "gateway_id": "<Another device ID>",
      "audio_pause_enabled": false,
      "audio_enabled": true
    },
    "patient": {
      "id": "<Patient ID>",
      "primary_identifier": "<Patient primary identifier>",
      "given_name": "<Patient name>",
      "family_name": "<Patient last name>",
      "gender": "<Patient gender>",
      "birth_date": "<ISO format date>",
      "active": true
    }
  },
  // Previous data for the encounter.
  "previous_state": {
    "id": "<Encounter ID>",
    "status": "in-progress",
    "created_at": "<ISO format date>",
    "start_time": "<ISO format date>",
    "end_time": "<ISO format date>",
    "device": {
      "id": "<Device ID>",
      "primary_identifier": "<Device primary identifier>",
      "model_number": "<Device type>",
      "name": "<Device name>",
      "location_id": "<Bed ID>",
      "gateway_id": "<Another device ID>",
      "audio_pause_enabled": false,
      "audio_enabled": true
    },
    "patient": {
      "id": "<Patient ID>",
      "primary_identifier": "<Patient primary identifier>",
      "given_name": "<Patient name>",
      "family_name": "<Patient last name>",
      "gender": "<Patient gender>",
      "birth_date": "<ISO format date>",
      "active": true
    }
  },
  "entity_name": "patient",
  "emitted_by": "patient",
  "message_id": "<UUID>",
  // Input of the event.
  "event_data": {}
}
```

**Patient encounter dismissed event**

```json
{
  "event_type": "PATIENT_ADMISSION_DISMISSED",
  "event_name":"Patient admission dismissed",
  // Internal ID of the encounter.
  "entity_id": "<Encounter ID>",
  "performed_on": "<ISO format date>",
  "performed_by": "<Username>",
  // Data of the encounter.
  "event_state": {
    "id": "<Encounter ID>",
    "status": "<Encounter status (planned | in-progress | completed | cancelled)>",
    "created_at": "<ISO format date>",
    "start_time": "<ISO format date>",
    "end_time": "<ISO format date>",
    "device": {
      "id": "<Device ID>",
      "primary_identifier": "<Device primary identifier>",
      "model_number": "<Device type>",
      "name": "<Device name>",
      "location_id": "<Bed ID>",
      "gateway_id": "<Another device ID>",
      "audio_pause_enabled": false,
      "audio_enabled": true
    },
    "patient": {
      "id": "<Patient ID>",
      "primary_identifier": "<Patient primary identifier>",
      "given_name": "<Patient name>",
      "family_name": "<Patient last name>",
      "gender": "<Patient gender>",
      "birth_date": "<ISO format date>",
      "active": true
    }
  },
  // Previous data for the encounter.
  "previous_state": {
    "id": "<Encounter ID>",
    "status": "<Encounter status (planned | in-progress | completed | cancelled)>",
    "created_at": "<ISO format date>",
    "start_time": "<ISO format date>",
    "end_time": "<ISO format date>",
    "device": {
      "id": "<Device ID>",
      "primary_identifier": "<Device primary identifier>",
      "model_number": "<Device type>",
      "name": "<Device name>",
      "location_id": "<Bed ID>",
      "gateway_id": "<Another device ID>",
      "audio_pause_enabled": false,
      "audio_enabled": true
    },
    "patient": {
      "id": "<Patient ID>",
      "primary_identifier": "<Patient primary identifier>",
      "given_name": "<Patient name>",
      "family_name": "<Patient last name>",
      "gender": "<Patient gender>",
      "birth_date": "<ISO format date>",
      "active": true
    }
  },
  "entity_name": "patient",
  "emitted_by": "patient",
  "message_id": "<UUID>",
  // Input of the event.
  "event_data": {}
}
```
