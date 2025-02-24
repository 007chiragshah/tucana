Feature: Create app settings

  Scenario: Happy path
    Given the application is running
    And a request to add an app setting with key "SETTING" and value "VAR"
    And valid credentials are provided
    When the request is made
    Then the user is told the request was successful
    And the app setting with key "SETTING" is updated to "VAR"

  Scenario: Setting already exists
    Given the application is running
    And a request to add an app setting with key "SETTING" and value "VAR"
    And an app setting with key "SETTING" and value "OLD_VAR" exists
    And valid credentials are provided
    When the request is made
    Then the user is told the request was successful
    And the app setting with key "SETTING" is updated to "VAR"

  Scenario: Invalid credentials
    Given the application is running
    And a request to add an app setting with key "SETTING" and value "VAR"
    And invalid credentials are provided
    When the request is made
    Then the user is told the request was unauthorized
