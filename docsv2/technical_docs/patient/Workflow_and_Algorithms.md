# 1. Workflow and algorithms

In the following section all the non-trivial workflows of the patient microservice are displayed as activity diagrams. The workflows for "get" endpoints are not shown here since the algorithm is trivial, only obtaining and filtering the information returned.

In all cases the diagrams only display validations related to the business logic, it does not include validations related to input sanitization, authentication/authorization or database integrity errors. This is done to improve the readability of the diagrams, as all those validations are expected to be done for each endpoint or event since they are basic errors.

## 1.1. API workflows

All this workflows are activated via a request done by the web microservice.

### 1.1.1. Add beds to bed groups

![Add beds to bed groups](<../images/activity_diagrams/patient/api/Add beds to bedgroup.svg>)

### 1.1.2. Batch assign beds to devices

![Batch assign beds to devices](<../images/activity_diagrams/patient/api/Batch assign beds to device.svg>)

### 1.1.3. Batch assign beds to groups

![Batch assign beds to groups](<../images/activity_diagrams/patient/api/Batch assing beds to groups.svg>)

### 1.1.4. Batch create bed groups

![Batch create bed groups](<../images/activity_diagrams/patient/api/Batch create bed groups.svg>)

### 1.1.5. Batch create beds 

![Batch create beds](<../images/activity_diagrams/patient/api/Batch create beds.svg>)

### 1.1.6. Batch delete bed grops

![Batch delete bed grops](<../images/activity_diagrams/patient/api/Batch delete bed grops.svg>)

### 1.1.7. Batch delete bed

![Batch delete bed](<../images/activity_diagrams/patient/api/Batch delete bed.svg>)

### 1.1.8. Batch unassign device from all beds

![Batch unassign device from all beds](<../images/activity_diagrams/patient/api/Batch unassign device from all beds.svg>)

### 1.1.9. Batch update bed groups

![Batch update bed groups](<../images/activity_diagrams/patient/api/Batch update bed groups.svg>)

### 1.1.10. Batch update beds

![Batch update beds](<../images/activity_diagrams/patient/api/Batch update beds.svg>)

### 1.1.11. Create bed group

![Create bed group](<../images/activity_diagrams/patient/api/Create bed group.svg>)

### 1.1.12. Create bed

![Create bed](<../images/activity_diagrams/patient/api/Create bed.svg>)

### 1.1.13. Create device

![Create device](<../images/activity_diagrams/patient/api/Create device.svg>)

### 1.1.14. Create patient

![Create patient](<../images/activity_diagrams/patient/api/Create patient.svg>)

### 1.1.15. Delete bed group

![Delete bed group](<../images/activity_diagrams/patient/api/Delete bed group.svg>)

### 1.1.16. Delete bed

![Delete bed](<../images/activity_diagrams/patient/api/Delete bed.svg>)

### 1.1.17. Delete device

![Delete device](<../images/activity_diagrams/patient/api/Delete device.svg>)

### 1.1.18. Delete patient

![Delete patient](<../images/activity_diagrams/patient/api/Delete patient.svg>)

### 1.1.19. Dismiss patient admission

This event is triggered when a patient is assigned to a PM but not confirmed yet. Before it can be confirmed a user can dismiss the admission and remove it from the device.

![Dismiss patient admission](<../images/activity_diagrams/patient/api/Dismiss patient admission.svg>)

### 1.1.20. Remove bed from group

![Remove bed from group](<../images/activity_diagrams/patient/api/Remove bed from group.svg>)

### 1.1.21. Start patient admission

This event is triggered when a patient is assigned to a device pending the confirmation via the PM.

![Start patient admission](<../images/activity_diagrams/patient/api/Start patient admission.svg>)

### 1.1.22. Update device

![Update device](<../images/activity_diagrams/patient/api/Update device.svg>)

### 1.1.23. Trivial workflows (Get workflows)

As mentioned before there is a list of workflows that are trivial and do not have a diagram since it would be a single node. They still have validation and parsing done by the framework used, but have no business logic other than retrieving the data from the database.

Here is the list of workflows:

- Get admission
- Get bed groups
- Get beds
- Get beds in group
- Get device by identifier
- Get device list
- Get device vital ranges
- Get patient by
- Get patient by identifier
- Get patient count
- Get patient list
- Get patient observations
- Get patient physiological alerts

Since all this workflows retrieve information they are triggered by the user when displaying anything on the frontend.

## 1.2. Event workflows

This worflows are triggered when an event incomming from the PM arrives containing new information regarding the device or patient state.

### 1.2.1. Alert observation received

This flow is triggered when an alert is either activated, deactivated or set to latching. This flow simultaneously runs 3 procedures, one to check the status of physiological alerts, other for technical alerts and the final one to store the alert logs.

![Alert observation received](<../images/activity_diagrams/patient/events/Alert observation received.svg>)

### 1.2.2. Device discovered event received

This flow is triggered when a device is first connected to the Central Server. For simple sensors the flow is simple, but for PMs it needs to update all the data related to the device in case this message is sent due to a network issue to avoid losing information.

![Device discovered event received](<../images/activity_diagrams/patient/events/Device discovered event received.svg>)

### 1.2.3. New vital ranges event received

This is triggered when one or more vital ranges are modified for a device.

![New vital ranges event received](<../images/activity_diagrams/patient/events/New vital ranges event received.svg>)

### 1.2.4. Patient admission rejected event received

This event is triggered by the user when rejecting a patient on the PM side.

![Patient admission rejected event received](<../images/activity_diagrams/patient/events/Patient admission rejected event received.svg>)

### 1.2.5. Patient session closed event received

This event is triggered when a patient session is closed from the PM side.

![Patient session closed event received](<../images/activity_diagrams/patient/events/Patient session closed event received.svg>)

### 1.2.6. Patient session started event received

This event is triggered when a patient session starts on the PM, which can happen in 2 ways: When a patient is sent from the Central Server to the PM and the patient is accepted, or when a PM enters a patient as quick admit.

![Patient session started event received](<../images/activity_diagrams/patient/events/Patient session started event received.svg>)

### 1.2.7. PM configuration updated event received

This event is received when whe PM configuration is changes, which happens when the audio settings change to on, off or paused.

![PM configuration updated event received](<../images/activity_diagrams/patient/events/PM configuration updated event received.svg>)

### 1.2.8. Sensor removed event received

This event is triggered when a sensor is unattached from a PM.

![Sensor removed event received](<../images/activity_diagrams/patient/events/Sensor removed event received.svg>)
