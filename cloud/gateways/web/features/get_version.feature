Feature: API Version Endpoint

  Scenario: Retrieve the current version
    Given the application is running
    When I send a GET request to "/version"
    Then the response status code should be 200
    And the response should contain the "version" field
    And the "version" field should be `local`
