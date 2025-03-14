@WEB @ALERTS @SMOKE
Feature: [WEB] Multiple Technicals alarms in MultiPatient View

  @MULTIPLE @TECHNICALS 
  @SR-1.3.15.1 @SR-1.3.15.2 @SR-1.3.15.16 @SR-1.3.15.25 @SR-1.3.15.32 @SR-1.3.15.36 @SR-1.3.15.39 @SR-1.3.15.54 @SR-1.3.15.58 @SR-1.3.15.64
  @SR-1.3.15.70 @SR-1.3.15.76 @SR-1.3.15.80 @SR-1.3.15.84 @SR-1.3.15.88 
  Scenario Outline: Multiple "<Alarm Type>" alerts and alarms HIGH priority
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
    And Tom sees the Bed Group created and clicks on it
    When Multiple "<Alarm Type>" "<Alarm Code>" alarms with "<Priority>" priority, "<Sensor Type>", "<Sensor ID>" are triggered
    And Tom sees the top level indicator showing the last "<Alarm Type>" alarm name triggered and the total
    Then Tom deactivate all the triggered alarms
    And Tom should not see the top level indicators activated
    And Tom disconnects the sensor "<Sensor ID>"
    And Tom closes a session for the Patient Monitor "<PM>"
    And Tom disconnects the Patient Monitor "<PM>"
    And Tom deletes a Patient Monitor "<PM>"
    And Tom deletes all the created scenario data


  Examples:
    | Alarm Code                                               | Alarm Type    | Priority    | PM         | Sensor ID   | Sensor Type |
    | SENSOR_OUT_OF_RANGE, LOW_SENSOR_BATTERY, SENSOR_FAILURE  | Technical     | HI, HI, HI  | PM-QA-X001 | SEN-QA-X001 | ANNE Chest  |

  @MULTIPLE @TECHNICALS 
  @SR-1.3.15.1 @SR-1.3.15.2 @SR-1.3.15.16 @SR-1.3.15.25 @SR-1.3.15.32 @SR-1.3.15.36 @SR-1.3.15.39 @SR-1.3.15.54 @SR-1.3.15.58 @SR-1.3.15.64
  @SR-1.3.15.70 @SR-1.3.15.76 @SR-1.3.15.80 @SR-1.3.15.84 @SR-1.3.15.88 
  Scenario Outline: Multiple "<Alarm Type>" alerts with Different priorities, highest priority descending order
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
    And Tom sees the Bed Group created and clicks on it
    When Multiple "<Alarm Type>" "<Alarm Code>" alarms with "<Priority>" priority, "<Sensor Type>", "<Sensor ID>" are triggered
    And Tom sees the top level indicator showing the "<Alarm Type>" alarm name triggered with highest priority and the total
    And Tom clicks on the alerts and sees them ordered by highest priority
    Then Tom deactivate all the triggered alarms
    And Tom should not see the top level indicators activated
    And Tom disconnects the sensor "<Sensor ID>"
    And Tom closes a session for the Patient Monitor "<PM>"
    And Tom disconnects the Patient Monitor "<PM>"
    And Tom deletes a Patient Monitor "<PM>"
    And Tom deletes all the created scenario data


  Examples:
    | Alarm Code                                               | Alarm Type    | Priority     | PM         | Sensor ID   | Sensor Type |
    | SENSOR_OUT_OF_RANGE, LOW_SENSOR_BATTERY, SENSOR_FAILURE  | Technical     | HI, ME, LO   | PM-QA-X001 | SEN-QA-X001 | ANNE Chest  |