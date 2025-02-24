@skip @WEB @AUTHENTICATION @SMOKE @SECURITY
Feature: [WEB] User Account Timeout after Multiple Failed Attempts

  @SR-1.1.1.2 @skip
  Scenario: Timeout after 5 failed login attempts
    Given Tom goes to "Tucana" Web APP login page
    When Tom logs in with incorrect credentials
    Then Tom should see the incorrect password message
    Given Tom goes to "Tucana" Web APP login page
    When Tom logs in with incorrect credentials
    Then Tom should see the incorrect password message
    Given Tom goes to "Tucana" Web APP login page
    When Tom logs in with incorrect credentials
    Then Tom should see the incorrect password message
    Given Tom goes to "Tucana" Web APP login page
    When Tom logs in with incorrect credentials
    Then Tom should see the incorrect password message
    Given Tom goes to "Tucana" Web APP login page
    When Tom logs in with incorrect credentials
    Then Tom should see the incorrect password message
    Given Tom goes to "Tucana" Web APP login page
    When Tom logs in with incorrect credentials
    Then Tom sees a message stating that the account is locked due to too many failed attempts

  @SR-1.1.1.2 @skip
  Scenario: Timeout after 5 failed change password attempts
    Given Tom goes to "Tucana" Web APP login page
    And Tom logs in with his credentials
    Then Tom sees the dashboard
    
    Given Tom wants to update the password
    Then Tom sees the popup message requiring the admin password
    And Tom fills the password information with an incorrect admin password
    And Tom clicks on the confirm button
    And the application notifies him the password was incorrect
    Then Tom wants to dismiss th button
    Then Tom goes to settings

    Given Tom wants to update the password
    Then Tom sees the popup message requiring the admin password
    And Tom fills the password information with an incorrect admin password
    And Tom clicks on the confirm button
    And the application notifies him the password was incorrect
    Then Tom wants to dismiss th button
    Then Tom goes to settings

    Given Tom wants to update the password
    Then Tom sees the popup message requiring the admin password
    And Tom fills the password information with an incorrect admin password
    And Tom clicks on the confirm button
    And the application notifies him the password was incorrect
    Then Tom wants to dismiss th button
    Then Tom goes to settings

    Given Tom wants to update the password
    Then Tom sees the popup message requiring the admin password
    And Tom fills the password information with an incorrect admin password
    And Tom clicks on the confirm button
    And the application notifies him the password was incorrect
    Then Tom wants to dismiss th button
    Then Tom goes to settings

    Given Tom wants to update the password
    Then Tom sees the popup message requiring the admin password
    And Tom fills the password information with an incorrect admin password
    And Tom clicks on the confirm button
    And the application notifies him the password was incorrect
    Then Tom wants to dismiss th button
    Then Tom goes to settings

    Given Tom wants to update the password
    Then Tom sees the popup message requiring the admin password
    And Tom fills the password information with an incorrect admin password
    And Tom clicks on the confirm button
    And Tom sees a message stating that the account is locked due to too many failed attempts on change password

  @SR-1.1.1.2 @skip
  Scenario: Timeout after 5 failed logout attempts
    Given Tom goes to "Tucana" Web APP login page
    And Tom logs in with his credentials
    And Tom sees the dashboard
    And Tom goes to settings

    When Tom clicks on log out
    Then Tom fills the log out password with the incorrect information
    And Tom clicks on the confirm button
    Then Tom should not be able to logout
    Then Tom wants to dismiss th button

    When Tom clicks on log out
    Then Tom fills the log out password with the incorrect information
    And Tom clicks on the confirm button
    Then Tom should not be able to logout
    Then Tom wants to dismiss th button

    When Tom clicks on log out
    Then Tom fills the log out password with the incorrect information
    And Tom clicks on the confirm button
    Then Tom should not be able to logout
    Then Tom wants to dismiss th button

    When Tom clicks on log out
    Then Tom fills the log out password with the incorrect information
    And Tom clicks on the confirm button
    Then Tom should not be able to logout
    Then Tom wants to dismiss th button

    When Tom clicks on log out
    Then Tom fills the log out password with the incorrect information
    And Tom clicks on the confirm button
    Then Tom should not be able to logout
    Then Tom wants to dismiss th button

    When Tom clicks on log out
    Then Tom fills the log out password with the incorrect information
    And Tom clicks on the confirm button
    And Tom sees a message stating that the account is locked due to too many failed attempts on change password


  @SR-1.1.1.2 @skip
  Scenario: Timeout after 5 failed audio alarm management attempts
    Given the user credentials are valid
    And Tom goes to "Tucana" Web APP login page
    When Tom logs in with his credentials
    Then Tom sees the dashboard
    When Tom sees the actual alarm status

    Then Tom goes to settings
    When Tom clicks on Manage audio alarm
    Then Tom changes the alarm status
    Then Tom saves the alarm status
    Then Tom sees the popup message requiring the admin password
    And Tom sees the popup information about the audio silenced
    When Tom fills the alarm status password with the incorrect information
    And Tom clicks on the confirm button
    And Tom sees the incorrect password message
    And Tom sees the continue button is disabled
    Then Tom wants to dismiss th button
    When Tom clicks on "Discard" button
    
    When Tom clicks on Manage audio alarm
    Then Tom changes the alarm status
    Then Tom saves the alarm status
    Then Tom sees the popup message requiring the admin password
    And Tom sees the popup information about the audio silenced
    When Tom fills the alarm status password with the incorrect information
    And Tom clicks on the confirm button
    And Tom sees the incorrect password message
    And Tom sees the continue button is disabled
    Then Tom wants to dismiss th button
    When Tom clicks on "Discard" button

    When Tom clicks on Manage audio alarm
    Then Tom changes the alarm status
    Then Tom saves the alarm status
    Then Tom sees the popup message requiring the admin password
    And Tom sees the popup information about the audio silenced
    When Tom fills the alarm status password with the incorrect information
    And Tom clicks on the confirm button
    And Tom sees the incorrect password message
    And Tom sees the continue button is disabled
    Then Tom wants to dismiss th button
    When Tom clicks on "Discard" button

    When Tom clicks on Manage audio alarm
    Then Tom changes the alarm status
    Then Tom saves the alarm status
    Then Tom sees the popup message requiring the admin password
    And Tom sees the popup information about the audio silenced
    When Tom fills the alarm status password with the incorrect information
    And Tom clicks on the confirm button
    And Tom sees the incorrect password message
    And Tom sees the continue button is disabled
    Then Tom wants to dismiss th button
    When Tom clicks on "Discard" button

    When Tom clicks on Manage audio alarm
    Then Tom changes the alarm status
    Then Tom saves the alarm status
    Then Tom sees the popup message requiring the admin password
    And Tom sees the popup information about the audio silenced
    When Tom fills the alarm status password with the incorrect information
    And Tom clicks on the confirm button
    And Tom sees the incorrect password message
    And Tom sees the continue button is disabled
    Then Tom wants to dismiss th button
    When Tom clicks on "Discard" button

    When Tom clicks on Manage audio alarm
    Then Tom changes the alarm status
    Then Tom saves the alarm status
    Then Tom sees the popup message requiring the admin password
    And Tom sees the popup information about the audio silenced
    When Tom fills the alarm status password with the incorrect information
    And Tom clicks on the confirm button
    And Tom sees a message stating that the account is locked due to too many failed attempts on change password
