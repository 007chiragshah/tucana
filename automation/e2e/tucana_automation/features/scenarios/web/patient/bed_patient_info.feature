@WEB @BED
Feature: [WEB] Patient Tabs inside bed details

  @SMOKE 
  @SR-1.3.3.1 @SR-1.3.3.2 @SR-1.3.3.8 @SR-1.3.3.9
  @SR-1.3.4.1 @SR-1.3.4.2 @SR-1.3.4.3 @SR-1.3.4.4 @SR-1.3.4.5 @SR-1.3.4.6 @SR-1.3.4.7 @SR-1.3.4.8 @SR-1.3.4.9 @SR-1.3.4.10 @SR-1.3.4.11
  @SR-1.3.5.1 @SR-1.3.5.2
  @SR-1.3.6.1 @SR-1.3.6.2 @SR-1.3.6.3 @SR-1.3.6.4 @SR-1.3.6.5 @SR-1.3.6.6 
  @SR-1.3.10.1 @SR-1.3.10.2 @SR-1.3.10.3 @SR-1.3.10.4 @SR-1.3.10.6 @SR-1.3.10.7
  @SR-1.5.3.1 @SR-1.5.3.2 @SR-1.5.3.3 @SR-1.5.3.4 @SR-1.5.3.5
  @SR-1.7.18
  Scenario Outline: Patient Info tab
    Given Tom creates a Patient Monitor "<PM>"
    And the bed exists
    And Tom assigns a Patient Monitor to a bed
    And the bed group exists
    And the bed is assigned to the group
    And the information is saved
    And 1 Patient exists with the following data
    """
    patient:
      id: aabbccdd-5555-5555-0000-4a2b97021e34
      given_name: Steve
      family_name: Rogers
      gender: male
      active: true
      primary_identifier: PT-QA-X002
      birthDate: "1970-07-06"
    """
    And Tom connects the Patient Monitor "<PM>" to the existent patient
    And Tom connects a sensor to the Patient Monitor "<PM>" with the following data
    """
    device_code: ANNE Chest
    primary_identifier: SEN-QA-X002
    name: ANNE Chest
    """
    And Tom goes to "Tucana" Web APP login page
    Given the user credentials are valid
    And Tom goes to "Tucana" Web APP login page
    And Tom logs in with his credentials
    Then Tom sees the dashboard
    And Tom sees the Bed Group and the bed created and clicks on it
    And Tom closes the Bed detail popup and he sees the Multi-Patient view again
    Then Tom sees the Bed Group and the bed created and clicks on it
    When Tom selects the "Patient Info" tab
    Then Tom sees the ID "<PT>", First Name "<First Name>", Last Name "<Last Name>", Sex "<Sex>", DOB "<DOB>" listed
    Then Tom logs out

  Examples:
    | PM          | PT         | First Name  | Last Name   | Sex     | DOB         |
    | PM-QA-X002  | PT-QA-X002 | Steve       | Rogers      | Male    | 1970-07-06  |

  @SMOKE 
  @SR-1.3.3.3 @SR-1.3.3.4 @SR-1.3.3.5 @SR-1.3.3.6 @SR-1.3.3.7 @SR-1.3.3.12 @SR-1.3.3.24 @SR-1.3.3.27 @SR-1.3.3.28 @SR-1.3.3.32 @SR-1.3.3.33 @SR-1.3.3.37 @SR-1.3.3.40 @SR-1.3.3.43
  @SR-1.3.6.1 @SR-1.3.6.2 @SR-1.3.6.3 @SR-1.3.6.4 @SR-1.3.6.5 @SR-1.3.6.6
  @SR-1.3.5.1 @SR-1.3.5.2 @SR-1.3.5.3 @SR-1.3.5.4 @SR-1.3.5.5 @SR-1.3.5.6 @SR-1.3.5.7 @SR-1.3.5.8 @SR-1.3.5.9 @SR-1.3.5.10 @SR-1.3.5.11 
  @SR-1.3.5.12 @SR-1.3.5.13 @SR-1.3.5.14 @SR-1.3.5.15 @SR-1.3.5.16 @SR-1.3.5.17 @SR-1.3.5.18 @SR-1.3.5.19 @SR-1.3.5.20 @SR-1.3.5.21 
  @SR-1.3.5.22 @SR-1.3.5.23 @SR-1.3.5.24 @SR-1.3.5.25 @SR-1.3.5.26 @SR-1.3.5.27 @SR-1.3.5.28 @SR-1.3.5.29 @SR-1.3.5.30 @SR-1.3.5.31 
  @SR-1.3.5.32 @SR-1.3.5.33 @SR-1.3.5.34 @SR-1.3.5.35 @SR-1.3.5.36 @SR-1.3.5.37 @SR-1.3.5.38
  @SR-1.3.10.1 @SR-1.3.10.2 @SR-1.3.10.4 @SR-1.3.10.5
  @SR-1.3.14.1 @SR-1.3.14.2 @SR-1.3.14.3 @SR-1.3.14.4 @SR-1.3.14.5 @SR-1.3.14.6 @SR-1.3.14.7 @SR-1.3.14.8 @SR-1.3.14.9 @SR-1.3.14.10 @SR-1.3.14.11
  @SR-1.5.3.1 @SR-1.5.3.2 @SR-1.5.3.3 @SR-1.5.3.4 @SR-1.5.3.5
  Scenario Outline: Vital Management tab Alarms limits
    Given Tom creates a Patient Monitor "<PM>"
    And the bed exists
    And Tom assigns a Patient Monitor to a bed
    And the bed group exists
    And the bed is assigned to the group
    And the information is saved
    And 1 Patient exists with the following data
    """
    patient:
      id: aabbccdd-5555-5555-0000-4a2b97021e34
      given_name: Steve
      family_name: Rogers
      gender: male
      active: true
      primary_identifier: PT-QA-X002
      birthDate: "1970-07-06"
    """
    And Tom connects the Patient Monitor "<PM>" to the existent patient
    And Tom connects a sensor to the Patient Monitor "<PM>" with the following data
    """
    device_code: ANNE Chest
    primary_identifier: SEN-QA-X002
    name: ANNE Chest
    """
    And Tom goes to "Tucana" Web APP login page
    Given the user credentials are valid
    And Tom goes to "Tucana" Web APP login page
    And Tom logs in with his credentials
    Then Tom sees the dashboard
    And Tom sees the Bed Group and the bed created and clicks on it
    When Tom selects the "Alarm Limits" tab
    And Tom sees the following Alarms Names and limits
      | Alarm           | Unit  | Low Limit | High Limit     |
      | HR              | bpm   | 45        | 120            |
      | SpO2            | %     | 85        | 100            |
      | PR              | bpm   | 45        | 120            |
      | RR              | brpm  | 5         | 30             |
      | BODY TEMP       | °F    | 93.2      | 102.2          |
      | SKIN TEMP       | °F    | 93.2      | 102.2          |
      | SYS             | mmHg  | 90        | 160            |
      | DIA             | mmHg  | 50        | 110            |
    Then Tom logs out

  Examples:
    | PM          |
    | PM-QA-X002  |


  @SMOKE 
  @SR-1.3.3.25 @SR-1.3.3.26 @SR-1.3.3.29 @SR-1.3.3.30 @SR-1.3.3.31 @SR-1.3.3.32 @SR-1.3.3.34 @SR-1.3.3.35 @SR-1.3.3.36 @SR-1.3.3.39
  @SR-1.3.5.3 @SR-1.3.5.7 @SR-1.3.5.11 @SR-1.3.5.15 @SR-1.3.5.19 @SR-1.3.5.23 @SR-1.3.5.27 @SR-1.3.5.33
  @SR-1.3.6.1 @SR-1.3.6.2 @SR-1.3.6.3 @SR-1.3.6.4 @SR-1.3.6.5 @SR-1.3.6.6
  @SR-1.3.7.1 @SR-1.3.7.2 @SR-1.3.7.3 @SR-1.3.7.4 @SR-1.3.7.5 @SR-1.3.7.6 @SR-1.3.7.7 @SR-1.3.7.8  
  @SR-1.3.10.3 @SR-1.3.10.6 @SR-1.3.10.7
  @SR-1.5.3.1 @SR-1.5.3.2 @SR-1.5.3.3 @SR-1.5.3.4 @SR-1.5.3.5
  @SR-1.7.18 @SR-1.7.20 
  Scenario Outline: Patient's sensors, icons and name presence at bed details page
    Given Tom creates a Patient Monitor "<PM>"
    And the bed exists
    And Tom assigns a Patient Monitor to a bed
    And the bed group exists
    And the bed is assigned to the group
    And the information is saved
    And 1 Patient exists with the following data
    """
    patient:
      id: aabbccdd-5555-5555-0000-4a2b97021e34
      given_name: Steve
      family_name: Rogers
      gender: male
      active: true
      primary_identifier: PT-QA-X002
      birthDate: "1970-07-06"
    """
    And Tom connects the Patient Monitor "<PM>" to the existent patient
    And Tom connects a sensor to the Patient Monitor "<PM>" with the following data
    """
    device_code: ANNE Chest
    primary_identifier: SEN-QA-X002
    name: ANNE Chest
    """
    And Tom connects a sensor to the Patient Monitor "<PM>" with the following data
    """
    device_code: Nonin 3150
    primary_identifier: SEN-QA-X004
    name: Nonin 3150
    """
    And Tom connects a sensor to the Patient Monitor "<PM>" with the following data
    """
    device_code: Viatom BP monitor
    primary_identifier: SEN-QA-X005
    name: Viatom BP monitor
    """
    And Tom connects a sensor to the Patient Monitor "<PM>" with the following data
    """
    device_code: DMT Thermometer
    primary_identifier: SEN-QA-X006
    name: DMT Thermometer
    """
    And Tom goes to "Tucana" Web APP login page
    Given the user credentials are valid
    And Tom goes to "Tucana" Web APP login page
    And Tom logs in with his credentials
    Then Tom sees the dashboard
    And Tom sees the Bed Group and the bed created and clicks on it
    Then Tom should see the following Patient's sensors with their correspondant icons
        | Sensor            | Sensor ID   |
        | ANNE Chest        | SEN-QA-X002 |
        | ANNE Limb         | SEN-QA-X003 |
        | Nonin 3150        | SEN-QA-X004 |
        | Viatom BP monitor | SEN-QA-X005 |
        | DMT Thermometer   | SEN-QA-X006 |
    Then Tom logs out

    Examples:
      | PM          |
      | PM-QA-X002  |


  @SMOKE 
  @SR-1.3.2.1 @SR-1.3.2.2 @SR-1.3.2.3 @SR-1.3.2.4 @SR-1.3.2.5 @SR-1.3.2.6 @SR-1.3.2.7 @SR-1.3.2.8 @SR-1.3.2.9 @SR-1.3.2.10 @SR-1.3.2.11 
  @SR-1.3.3.10 @SR-1.3.3.11 @SR-1.3.3.12 @SR-1.3.3.13 @SR-1.3.3.14 @SR-1.3.3.15 @SR-1.3.3.16 @SR-1.3.3.17 @SR-1.3.3.18 @SR-1.3.3.19 
  @SR-1.3.3.20 @SR-1.3.3.21 @SR-1.3.3.22 @SR-1.3.3.23 @SR-1.3.3.25 @SR-1.3.3.26 @SR-1.3.3.28 @SR-1.3.3.29 
  @SR-1.3.3.30 @SR-1.3.3.33 @SR-1.3.3.37 @SR-1.3.3.38 @SR-1.3.3.39 @SR-1.3.3.40 @SR-1.3.3.41 @SR-1.3.3.42 @SR-1.3.3.43 @SR-1.3.3.44 @SR-1.3.3.45
  @SR-1.3.5.4 @SR-1.3.5.8 @SR-1.3.5.12 @SR-1.3.5.16 @SR-1.3.5.20 @SR-1.3.5.24 @SR-1.3.5.28 @SR-1.3.5.34
  @SR-1.3.6.1 @SR-1.3.6.2 @SR-1.3.6.3 @SR-1.3.6.4 @SR-1.3.6.5 @SR-1.3.6.6
  @SR-1.3.10.1 @SR-1.3.10.2 @SR-1.3.10.4 @SR-1.3.10.5 @SR-1.3.10.6 @SR-1.3.10.7
  @SR-1.5.3.1 @SR-1.5.3.2 @SR-1.5.3.3 @SR-1.5.3.4 @SR-1.5.3.5
  Scenario Outline: Patient's vitals information
    Given Tom creates a Patient Monitor "<PM>"
    And the bed exists
    And Tom assigns a Patient Monitor to a bed
    And the bed group exists
    And the bed is assigned to the group
    And the information is saved
    And 1 Patient exists with the following data
    """
    patient:
      id: aabbccdd-5555-5555-0000-4a2b97021e34
      given_name: Steve
      family_name: Rogers
      gender: male
      active: true
      primary_identifier: PT-QA-X002
      birthDate: "1970-07-06"
    """
    And Tom connects the Patient Monitor "<PM>" to the existent patient
    And Tom connects a sensor to the Patient Monitor "<PM>" with the following data
    """
    device_code: ANNE Chest
    primary_identifier: SEN-QA-X002
    name: ANNE Chest
    """
    And Tom connects a sensor to the Patient Monitor "<PM>" with the following data
    """
    device_code: Nonin 3150
    primary_identifier: SEN-QA-X004
    name: Nonin 3150
    """
    And Tom connects a sensor to the Patient Monitor "<PM>" with the following data
    """
    device_code: Viatom BP monitor
    primary_identifier: SEN-QA-X005
    name: Viatom BP monitor
    """
    And Tom connects a sensor to the Patient Monitor "<PM>" with the following data
    """
    device_code: DMT Thermometer
    primary_identifier: SEN-QA-X006
    name: DMT Thermometer
    """
    And Tom goes to "Tucana" Web APP login page
    Given the user credentials are valid
    And Tom goes to "Tucana" Web APP login page
    And Tom logs in with his credentials
    Then Tom sees the dashboard
    And Tom sees the Bed Group and the bed created and clicks on it
    Then Tom should see the following Patient's vitals information
      | Information       |
      | HR (bpm)          |
      | SPO2 (%)          |
      | PR (bpm)          |
      | PI (%)            |
      | RR (brpm)         |
      | FALL              |
      | BODY TEMP (°F)    |
      | SKIN TEMP (°F)    |
      | Position (HHMM)   |
      | NIBP (mmHg)       |
      | ECG               |
      | PLETH             |
      | RR                |
      | PULSE (bpm)       |

    Then Tom logs out

    Examples:
      | PM           |
      | PM-QA-X002   |
