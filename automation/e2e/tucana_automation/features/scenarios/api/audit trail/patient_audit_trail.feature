@API @AUDIT_TRAIL @SR-7.5.3
Feature: [API] Get Patient Audit Trail

  Background:
    Given the user credentials are valid
    And the tucana application is running
    And A request to create a new patient through Tucana's API
    When the request is made to create a patient
    Then the user is told the request to create was successful

  @SR-1.7.1 @SR-1.7.2 @SR-1.7.3 @SR-1.7.4 @SR-1.7.5 @SR-1.7.6 @SR-1.7.7 @SR-1.7.8 @SR-1.7.9 @SR-1.7.10 @SR-1.7.24 @SR-1.7.25 @SR-1.7.26
  Scenario: Get patient audit trail
    When the user wants to get the audit trail for the recently created patient
    Then the user is told the get audit trail request was successful
    And the user verifies that all the patient audit trail information is correct
    And The patient is removed to keep the application clean