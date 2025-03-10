@WEB @SMOKE
Feature: [WEB] Log in into Tucana's Web Page

  @SR-1.1.1 @SR-1.1.2 @SR-1.1.3 @SR-1.1.5 @SR-1.1.7 @SR-7.4.2 @SR-7.4.1 @SR-1.3.30 @SR-1.6.10 @SR-1.1.3.1 @SR-1.1.3.2 @SR-1.1.3.3 @SR-1.1.3.4 @SR-1.1.3.5 @SR-1.1.3.6 @SR-1.1.3.7 @SR-1.1.3.8 @SR-1.1.3.9  @SR-1.1.3.13
  Scenario: Log in with correct credentials
    Given Tom goes to "Tucana" Web APP login page
    Then Tom should see the Login button disabled
    And Tom inputs his password
    Then Tom should see the Login button enabled
    And Tom clicks on the Log in button
    Then Tom sees the dashboard
    And Tom sees the "Multi-Patient View"

  @SR-1.1.6 @SR-1.6.16 @SR-1.6.10
  Scenario: Log in with incorrect credentials
    Given Tom goes to "Tucana" Web APP login page
    When Tom logs in with incorrect credentials
    Then Tom should see the incorrect password message

  @SR-1.1.2.1 @SR-1.1.2.2 @SR-1.1.2.3 
  Scenario: Password placeholder & button disabled check 
    Given Tom goes to "Tucana" Web APP login page
    Then Tom should see the Login button disabled
    And Tom should see the password placeholder