Feature: List app settings

  Scenario: Happy path
    Given the application is running
    And multiple app settings exist
      | key       | value   |
      | SETTING_1 | VALUE_1 |
      | SETTING_2 | VALUE_2 |
    And a request to list all settings
    And valid credentials are provided
    When the request is made
    Then the user is told the request was successful
    And the list of all settings is returned
      | key       | value   |
      | SETTING_1 | VALUE_1 |
      | SETTING_2 | VALUE_2 |

  Scenario: Invalid credentials
    Given the application is running
    And multiple app settings exist
      | key       | value   |
      | SETTING_1 | VALUE_1 |
      | SETTING_2 | VALUE_2 |
    And a request to list all settings
    And invalid credentials are provided
    When the request is made
    Then the user is told the request was unauthorized
