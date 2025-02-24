Feature: Batch create app settings

  Scenario: Happy path
    Given the application is running
    And a request to add multiple app settings
      | key       | value   |
      | SETTING_1 | VALUE_1 |
      | SETTING_2 | VALUE_2 |
    And valid credentials are provided
    When the request is made
    Then the user is told the request was successful
    And app settings are updated
      | key       | value   |
      | SETTING_1 | VALUE_1 |
      | SETTING_2 | VALUE_2 |

  Scenario: Setting already exists
    Given the application is running
    And a request to add multiple app settings
      | key       | value   |
      | SETTING_1 | VALUE_1 |
      | SETTING_2 | VALUE_2 |
    And an app setting with key "SETTING_1" and value "OLD_VAR" exists
    And valid credentials are provided
    When the request is made
    Then the user is told the request was successful
    And app settings are updated
      | key       | value   |
      | SETTING_1 | VALUE_1 |
      | SETTING_2 | VALUE_2 |

  Scenario: Invalid credentials
    Given the application is running
    And a request to add multiple app settings
      | key       | value   |
      | SETTING_1 | VALUE_1 |
      | SETTING_2 | VALUE_2 |
    And invalid credentials are provided
    When the request is made
    Then the user is told the request was unauthorized
