@WEB @SMOKE
Feature: [WEB] Emulated Sensors - Nonin 3150 Physiological Alarms inside bed details information

  @EMULATED_SENSORS @PHYSIOLOGICAL @NONIN 
  @SR-1.4.1.1 @SR-1.4.1.6 @SR-1.4.1.7 @SR-1.4.1.8 @SR-1.4.1.9 @SR-1.4.1.10 @SR-1.4.1.11 @SR-1.4.1.12 @SR-1.4.1.13 @SR-1.4.1.14 @SR-1.4.1.15 @SR-1.4.1.16
  @SR-1.3.11.1 @SR-1.3.11.1 @SR-1.3.11.2 @SR-1.3.11.3 @SR-1.3.11.4 @SR-1.3.11.5 @SR-1.3.11.6 @SR-1.3.11.7 @SR-1.3.11.8 @SR-1.3.11.9
  Scenario Outline: Nonin 3150 alarms - "<Alarm Position>" Alarms
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
    device_code: Nonin 3150
    primary_identifier: SEN-QA-X001
    name: Nonin 3150
    """
    And Tom goes to "Tucana" Web APP login page
    And Tom logs in with his credentials
    And Tom sees the dashboard
    And Tom sees the Bed Group and the bed created and clicks on it
    And Tom sees the "<Sensor Type>" icon, name and ID "<Sensor ID>" present
    And Tom triggers all "<Alarms Type>" alarms and checks "<Alarm Position>" colors, of "<Sensor Type>", id "<Sensor ID>" with different priorities
      | Priority |
      | HI       |
      | ME       |
      | LO       |
    And Tom disconnects the sensor "<Sensor ID>"
    And Tom closes a session for the Patient Monitor "<PM>"
    And Tom disconnects the Patient Monitor "<PM>"
    And Tom deletes a Patient Monitor "<PM>"
    And Tom deletes all the created scenario data

    Examples:
      | PM         | Sensor ID   | Sensor Type   | Alarms Type   | Alarm Position |
      | PM-QA-X001 | SEN-QA-X001 | Nonin 3150    | Physiological | Card           |
      | PM-QA-X001 | SEN-QA-X001 | Nonin 3150    | Physiological | Top/Left       |