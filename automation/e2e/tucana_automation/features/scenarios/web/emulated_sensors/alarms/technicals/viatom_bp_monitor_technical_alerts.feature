@WEB @SMOKE
Feature: [WEB] Emulated Sensors - Viatom BP monitor Technical Alerts inside bed details information

  @EMULATED_SENSORS @TECHNICAL @VIATOM @SR-1.3.10.1 @SR-1.3.10.2 @SR-1.3.10.3 @SR-1.3.10.4 @SR-1.3.10.6 @SR-1.3.10.7
  @SR-1.3.15.76 @SR-1.3.15.77 @SR-1.3.15.78 @SR-1.3.15.79 @SR-1.3.15.80
  @SR-1.3.15.81 @SR-1.3.15.82 @SR-1.3.15.83 @SR-1.3.15.84 @SR-1.3.15.85 @SR-1.3.15.86 @SR-1.3.15.87 @SR-1.3.15.88 @SR-1.3.15.89 @SR-1.3.15.90
  @SR-1.3.15.91  
  Scenario Outline: Viatom BP monitor "<Alarms Type>" alerts, messages, colors and icons test
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
    device_code: Viatom BP monitor
    primary_identifier: SEN-QA-X001
    name: Viatom BP monitor
    """
    And Tom goes to "Tucana" Web APP login page
    And Tom logs in with his credentials
    And Tom sees the dashboard
    And Tom sees the Bed Group and the bed created and clicks on it
    And Tom sees the "<Sensor Type>" icon, name and ID "<Sensor ID>" present
    And Tom triggers all "<Alarms Type>" alarms and checks "<Alarm Position>" colors, of "<Sensor Type>", id "<Sensor ID>", alert messages and warning icon with different priorities
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
      | PM         | Sensor ID   | Sensor Type         | Alarms Type   | Alarm Position |
      | PM-QA-X001 | SEN-QA-X001 | Viatom BP monitor   | Technical     | Top/Left       |