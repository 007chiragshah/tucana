Feature: Login Session

  Scenario: Happy Path
    Given the application is running
    And a valid request to start a user session
    When the request to start a user session is made
    Then the user is told the request was successful
    And the response includes the new session
