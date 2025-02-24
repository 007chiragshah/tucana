@API @AUDIT_TRAIL @SMOKE @SR-7.5.3
Feature: [API] Get Bed Audit Trail

  Background:
    Given the user credentials are valid
    And the tucana application is running
    And A request to create a new bed through Tucana's API
    When the request is made to create a bed
    Then the user is told the request to create was successful
    And the bed is created

  @SR-1.7.1 @SR-1.7.2 @SR-1.7.3 @SR-1.7.4 @SR-1.7.5 @SR-1.7.6 @SR-1.7.7 @SR-1.7.8 @SR-1.7.9 @SR-1.7.10 @SR-1.7.24
  Scenario: Get bed audit trail
    When the user wants to get the audit trail for the recently created bed
    Then the user is told the get audit trail request was successful
    And the user verifies that all the bed audit trail information is correct
    And The bed is removed to keep the application clean