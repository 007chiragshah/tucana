@WEB @AUTHENTICATION @SMOKE
Feature: [WEB] Change Password

Background:
   Given Tom goes to "Tucana" Web APP login page
   And Tom logs in with his credentials
   Then Tom sees the dashboard

  @SR-1.1.4 @SR-1.6.10 @SR-1.1.5.1 @SR-1.1.5.2 @SR-1.1.5.3 @SR-1.1.5.4 @SR-1.1.5.5 @SR-1.1.5.6 @SR-1.1.5.7 @SR-1.1.5.8 @SR-1.1.5.18
  Scenario: Change Password - validate the minimum size for a password
    Given Tom wants to update the password
    Then Tom sees the popup message requiring the admin password
    And Tom fills the password information with is admin password
    And Tom clicks on the confirm button
    And Tom sees the placeholder for the new password
    And Tom sees the placeholder for the re-enter new password
    When Tom sets the new password "Xc4"
    And Tom re-enter the new password "Xc4"
    Then the application notifies him the password does not meet criteria

  @SR-1.1.22 @SR-1.1.23 @SR-1.6.10 @SR-1.1.5.9 @SR-1.1.5.10 @SR-1.1.5.11 @SR-1.1.5.12 @SR-1.1.5.13 
  Scenario: Change Password - validate the re-entry of the new password with another password
    Given Tom wants to update the password
    Then Tom sees the popup message requiring the admin password
    And Tom fills the password information with is admin password
    And Tom clicks on the confirm button
    When Tom sets the new password "AcBt34TY13"
    And Tom sees the continue button in change password is "disabled"
    And Tom re-enter the new password "TvBgt67HK9"
    And Tom sees the continue button in change password is "disabled"
    Then the application notifies him the password does not match previous entry

  @SR-1.1.5.9 @SR-1.1.5.10 @SR-1.1.5.11 @SR-1.1.5.12 @SR-1.1.5.13   @SR-1.1.5.14 @SR-1.1.5.15 @SR-1.1.5.16 @SR-1.1.5.17 
  Scenario: Change Password - validate the re-entry of the new password with same password
    Given Tom wants to update the password
    Then Tom sees the popup message requiring the admin password
    And Tom fills the password information with is admin password
    And Tom clicks on the confirm button
    When Tom sets the new password "VX8jbXgHc2Yy_&gA"
    And Tom sees the continue button in change password is "disabled"
    And Tom re-enter the new password "VX8jbXgHc2Yy_&gA"
    And Tom sees the continue button in change password is "enaled"
    And Tom clicks on the confirm button
    Then the application notifies him Password changed successfully
    Then the application notifies him Please use your new password for future logins
    And Tom clicks on the ok button

  @SR-1.1.24 @SR-1.6.10
  Scenario: Change Password - validate incorrect admin password
    Given Tom wants to update the password
    Then Tom sees the popup message requiring the admin password
    And Tom fills the password information with an incorrect admin password
    And Tom clicks on the confirm button
    And the application notifies him the password was incorrect
    
  
    
    
    

    



