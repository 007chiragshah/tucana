@API @AUDIT_TRAIL @SMOKE @SR-7.5.3
Feature: [API] Get Bed Group Audit Trail

  Background:
    Given the user credentials are valid
    And the tucana application is running
    And A request to create a new bed group through upsert endpoint
    When the request is made to create a bed group through upsert endpoint
    Then the user is told the request to create a new bed group through upsert endpoint was successful

  @SR-1.7.1 @SR-1.7.2 @SR-1.7.3 @SR-1.7.4 @SR-1.7.5 @SR-1.7.6 @SR-1.7.7 @SR-1.7.8 @SR-1.7.9 @SR-1.7.10 
  Scenario: Get bed group audit trail
    When the user wants to get the audit trail for the recently created bed group
    Then the user is told the get audit trail request was successful
    And the user verifies that all the bed group audit trail information is correct
    And The bed group is removed to keep the application clean