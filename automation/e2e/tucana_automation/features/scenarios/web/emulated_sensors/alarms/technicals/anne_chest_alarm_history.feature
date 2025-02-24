@WEB @SMOKE
Feature: [WEB] Emulated Sensors - ANNE Chest TECHNICALS Alarms HISTORY inside bed details information

  @EMULATED_SENSORS @TECHNICALS @ANNE
  @SR-1.3.8.1 @SR-1.3.8.2 @SR-1.3.8.3 @SR-1.3.8.4 @SR-1.3.8.5 @SR-1.3.8.6 @SR-1.3.8.7 @SR-1.3.8.8 @SR-1.3.8.9 @SR-1.3.8.10 @SR-1.3.8.11 @SR-1.3.8.12
  @SR-1.3.15.1 @SR-1.3.15.2 @SR-1.3.15.3 @SR-1.3.15.4 @SR-1.3.15.5 @SR-1.3.15.6 @SR-1.3.15.7 @SR-1.3.15.8 @SR-1.3.15.9 @SR-1.3.15.10
  @SR-1.3.15.16 @SR-1.3.15.17 @SR-1.3.15.18 @SR-1.3.15.19 @SR-1.3.15.20 @SR-1.3.15.21 @SR-1.3.15.22 @SR-1.3.15.23 @SR-1.3.15.24 @SR-1.3.15.25 
  @SR-1.3.15.34 @SR-1.3.15.36 @SR-1.3.15.37 @SR-1.3.15.39 @SR-1.3.15.40
  @SR-1.3.15.41 @SR-1.3.15.42 @SR-1.3.15.43 @SR-1.3.15.44 @SR-1.3.15.45 @SR-1.3.15.46 @SR-1.3.15.47 @SR-1.3.15.54 @SR-1.3.15.55
  Scenario Outline: Anne Chest alarms - "<Alarm Position>" test
    Given Tom creates a Patient Monitor "<PM>"
    And the bed exists
    And Tom assigns a Patient Monitor to a bed
    And the bed group exists
    And the bed is assigned to the group
    And the information is saved
    And 1 Patient exists with the following data
    """
    patient:
      id: aabbccdd-2222-4444-0000-4a2b97021e34
      given_name: Bruce
      family_name: Wayne
      gender: male
      active: true
      primary_identifier: PT-QA-X001
      birthDate: "1970-07-06"
    """
    And Tom connects the Patient Monitor "<PM>" to the existent patient
    And Tom connects a sensor to the Patient Monitor "<PM>" with the following data
    """
    device_code: ANNE Chest
    primary_identifier: SEN-QA-X001
    name: ANNE Chest
    """
    And Tom goes to "Tucana" Web APP login page
    And Tom logs in with his credentials
    And Tom sees the dashboard
    And Tom sees the Bed Group and the bed created and clicks on it
    And Tom sees the "<Sensor Type>" icon, name and ID "<Sensor ID>" present
    And Tom triggers all "<Alarms Type>" alarms and checks "<Alarm Position>" colors, of "<Sensor Type>", id "<Sensor ID>" with different priorities, duration 3 seconds
      | Priority |
      | HI       |
      | ME       |
      | LO       |
    And Tom selects the "ALARM HISTORY" tab
    And Tom sees the alarm history is the expected one
    And Tom disconnects the sensor "<Sensor ID>"
    And Tom closes a session for the Patient Monitor "<PM>"
    And Tom disconnects the Patient Monitor "<PM>"
    And Tom deletes a Patient Monitor "<PM>"
    And Tom deletes all the created scenario data

    Examples:
      | PM         | Sensor ID   | Sensor Type | Alarms Type   | Alarm Position |
      | PM-QA-X001 | SEN-QA-X001 | ANNE Chest  | Technical     | Top/Left       |