# Workflow and algorithms

## Automatic Redirection

This is an automatic flow that is triggered by a user accessing the root page of CMS. CMS checks locally stored data about which type of user was the last session for (either clinical or technical) and redirects the user to the appropriate section of the app depending if there are valid credentials stored.

![Automatic Redirection - Sequence Diagram](../images/sequence_diagrams/central_monitoring_site/Automatic%20Redirection.svg)

## Technical Login

This is the authentication flow for a technical user. It uses the information provided by the user to try and get a valid token that allows the user to utilize the rest of the technical module functionalities.

For this case CMS communicates with the Web Gateway which is in charge of validating the users credentials and generating the token

![Technical Login - Sequence Diagram](../images/sequence_diagrams/central_monitoring_site/Technical%20Login.svg)

## Technical Logout

This is the de-authentication flow for a technical user. It requires the password to be entered by the technical user to fully logout from the Central System

For this case CMS communicates with the Web Gateway which is in charge of validating the users credentials and revoking the token

![Technical Logout - Sequence Diagram](../images/sequence_diagrams/central_monitoring_site/Technical%20Logout.svg)

## EHR Integration

This flow allows a technical user to configure EHR Integration with new host, port and interval values.

For this case CMS communicates with the Web Gateway which is in charge of storing the new values and communicate them with the appropriate parts of the Central Server to impact those changes in the system as a whole

![EHR Integration - Sequence Diagram](../images/sequence_diagrams/central_monitoring_site/EHR%20Integration.svg)

## Clinical User Login

This is the authentication flow for a clinical user. It uses the information provided by the user to try and get a valid token that allows the user to utilize the rest of the clinical module functionalities.

For this case CMS communicates with the Web Gateway which is in charge of validating the users credentials and generating the token

![Clinical Login - Sequence Diagram](../images/sequence_diagrams/central_monitoring_site/Clinical%20Login.svg)

## Clinical User Logout

This is the de-authentication flow for a clinical user. It requires the password to be entered by the clinical user to fully logout from the Central System

For this case CMS communicates with the Web Gateway which is in charge of validating the users credentials and revoking the token

![Clinical Logout - Sequence Diagram](../images/sequence_diagrams/central_monitoring_site/Clinical%20Logout.svg)

## Clinical User Change Password

This is the password change flow for a clinical user. It prompts the user to re-enter their password and provide a new one to be changed to.

For this case CMS communicates with the Web Gateway which is in charge of updating the users credentials

![Clinical User Change Password - Sequence Diagram](../images/sequence_diagrams/central_monitoring_site/Clinical%20Change%20Password.svg)

## Update Beds

This flow allows a clinical user to add/remove/update beds stored in the system. There are several conditions CMS controls to ensure Central Hub + Central Server works as expected. These conditions are:

1. At least 1 bed created
2. No two beds with the same id
3. No beds with empty id
4. No beds with id longer than 50 characters
5. Number of beds is equal or less than the configured MAX_NUMBER_BEDS (default 64)

For this case CMS communicates with the Web Gateway which will communicate with the rest of the Central System to ensure data for beds is correctly stored and accesible where needed

![Update Beds - Sequence Diagram](../images/sequence_diagrams/central_monitoring_site/Update%20beds.svg)

## Update Beds

This flow allows a clinical user to add/remove/update beds stored in the system. There are several conditions CMS controls to ensure Central Hub + Central Server works as expected. These conditions are:

1. At least 1 bed created
2. No two beds with the same id
3. No beds with empty id
4. No beds with id longer than 50 characters
5. Number of beds is equal or less than the configured MAX_NUMBER_BEDS (default 64)

For this case CMS communicates with the Web Gateway which will communicate with the rest of the Central System to ensure data for beds is correctly stored and accesible where needed

![Update Beds - Sequence Diagram](../images/sequence_diagrams/central_monitoring_site/Update%20beds.svg)

## Assign PMs to Beds

This flow allows a clinical user to assign PMs to Beds in a 1 to 1 relationship structure. After finishing assigning PMs to Beds the new relations will only be saved if there is at least one relationship between a PM and a bed. It will also prompt the user for confirmation if there are PMs that have no beds assigned.

For this case CMS communicates with the Web Gateway which will communicate with the rest of the Central System to ensure data for beds and PMs is correctly stored and accesible where needed

![Assign PMs to Beds - Sequence Diagram](../images/sequence_diagrams/central_monitoring_site/Assign%20PMs%20to%20beds.svg)

## Update Groups

This flow allows a clinical user to add/remove/update groups stored in the system. There are several conditions CMS controls to ensure Central Hub + Central Server works as expected. These conditions are:

1. At least 1 group created
2. No two groups have the same name
3. No groups with empty name
4. No group has 0 beds assigned

For this case CMS communicates with the Web Gateway which will communicate with the rest of the Central System to ensure data for groups is correctly stored and accesible where needed

![Update Groups - Sequence Diagram](../images/sequence_diagrams/central_monitoring_site/Update%20groups.svg)

## Update Selected Group

This flow allows a clinical user to select a new bed group for display. The clinical user can select any current group to select as the new active group.

For this case CMS communicates with the Web Gateway to retrieve the information of the current groups

![Update Selected Group - Sequence Diagram](../images/sequence_diagrams/central_monitoring_site/Update%20selected%20group.svg)

## Pause/Unpause Audio Alarms

This flow allows a clinical user to momentarily pause audio alerts so no alerts sounds will be emitted for 120 seconds

![Pause/Unpause Audio Alarms - Sequence Diagram](../images/sequence_diagrams/central_monitoring_site/Pause%20unpause%20audio%20alarms.svg)

## Disable/Enable Audio Alarms

This flow allows a clinical user to pause audio alerts so no alerts sounds will be emitted until manually re-enabled

For this case CMS communicates with the Web Gateway to validate the credentials for the clinical user before modifying the audio alarms setting

![Disable/Enable Audio Alarms - Sequence Diagram](../images/sequence_diagrams/central_monitoring_site/Disable%20enable%20audio%20alarms.svg)

## Display Realtime Vitals

This is one of the core flows of the application, and it allows the user to see realtime vitals of the monitored patients in the currently selected group in the application.

For this case case the Central Monitoring Site first communicates with the Web Gateway to get the groups/patients data it needs. After that, CMS utilizes the Web Worker to commuicate with the Realtime Gateway to continuously get up to date vitals information of all patients in the group.

![Display Realtime Vitals - Sequence Diagram](../images/sequence_diagrams/central_monitoring_site/Display%20Realtime%20Vitals.svg)

## Display Realtime Alerts

This is one of the core flows of the application, and it allows the user to see realtime alerts of the monitored patients in the currently selected group in the application.

For this case case the Central Monitoring Site first communicates with the Web Gateway to get the groups/patients data it needs. After that, CMS utilizes the Web Worker to commuicate with the Realtime Gateway to continuously get new alerts events. When a new alert event is received, CMS communicates with the Web Gateway once again to get the new alerts.

![Display Realtime Alerts - Sequence Diagram](../images/sequence_diagrams/central_monitoring_site/Display%20Realtime%20Alerts.svg)

## Display Patient Info

This flow allows a clinical user to check information about a patient currently in an ongoing session with a linked PM.

For this case case the Central Monitoring Site communicates with the Web Gateway to get the beds/patient data it needs. After it displays the patient info when the clinical user requests the information by accessing the patient info details tab.

![Display Patient Info - Sequence Diagram](../images/sequence_diagrams/central_monitoring_site/Display%20Patient%20Info.svg)

## Display Alarm Limits

This flow allows a clinical user to check the current alarm limits in an ongoing session with a linked PM.

For this case case the Central Monitoring Site first communicates with the Web Gateway to get the groups/beds data it needs. After this data is obtained, two processes are run in parallel:

1. A connection to the Realtime Gateway is established through the Web Worker. Through this CMS receives realtime vitals data which includes the units for both each metric as well as its limits
2. Patient monitors data is requested from CMS to the Web Gateway to get pre-established limits information. This flow is also triggered when receiving any event that requires a re-fetch of PMs data

While these processes are running, a Clinical User can access the Alarm Limits tab to see all limits information.

![Display Alarm Limits - Sequence Diagram](../images/sequence_diagrams/central_monitoring_site/Display%20Alarm%20Limits.svg)

## Display Alarm History

This flow allows a clinical user to check the alarm history of an ongoing session with a linked PM.

For this case case the Central Monitoring Site first communicates with the Web Gateway to get the beds/patients data it needs. After this it communicates to the Web Gateway again to retrieve the session alerts.

After this, whenever an alert deactivated event is received from an ongoing Web Worker Websocket communication, CMS will retrieve the new session alerts from the Web Gateway again.

A Clinical User can access the Alarm History tab to see all alarms history information.

![Display Alarm History - Sequence Diagram](../images/sequence_diagrams/central_monitoring_site/Display%20Alarm%20History.svg)

## EHR Quick Admit Patient

This flow allows a clinical user to request a new patient session for a new patient to be started on an idle PM.

For this flow, the Clinical User acceses the Quick Admit form of a Bed that is connected to an idle PM. After this the User enters the data for the new patient to be created. After all information is entered CMS communicates with the Web gateway to request the start of the new session.

Afterwards, Realtime Gateway will send an event through the Web Worker when the request has been submitted, and CMS will show this to the Clinical User.

![EHR Quick Admit Patient - Sequence Diagram](../images/sequence_diagrams/central_monitoring_site/EHR%20Quick%20Admit%20Patient.svg)

## EHR Search Admit Patient

This flow allows a clinical user to request a new patient session for a pre-existing patient to be started on an idle PM.

For this flow, the Clinical User acceses the Search form of a Bed that is connected to an idle PM. After this the User enters the data for the patient to be searched. Once submitted, CMS communicates with Web Gateway to get all patients matching their info.

CMS displays all found patients and the Clinical User selects their desired patient and confirms this request. CMS communicates again with Web Gateway to send the data for patient assignation.

Afterwards, Realtime Gateway will send an event through the Web Worker when the request has been submitted, and CMS will show this to the Clinical User.

![EHR Search Admit Patient - Sequence Diagram](../images/sequence_diagrams/central_monitoring_site/EHR%20Search%20Admit%20Patient.svg)

## EHR Patient Admission Rejected

This flow allows a clinical user to see when a patient admission request has been rejected, and acknowledge this information to potentially allow the EHR Quick Admit Patient or EHR Search Admit Patient sequences to start again.

For this flow, CMS requests beds data from the Web Gateway and find there is a bed with a rejected admission. Once the Clinical User selected the bed with rejected admission, CMS will display the modal informing them this. From here the Clinical User is able to acknowledge this information.

Afterwards, Realtime Gateway will send an event through the Web Worker when the admission rejected acknowledgment has been processed, and CMS will show a bed with an idle PM screen again.

![EHR Patient Admission Rejected - Sequence Diagram](../images/sequence_diagrams/central_monitoring_site/EHR%20Patient%20Admission%20Rejected.svg)
