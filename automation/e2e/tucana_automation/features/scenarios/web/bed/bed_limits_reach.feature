@WEB @SMOKE
Feature: [WEB] Beds Limitation Popup

    @SR-1.2.1.2 @SR-1.2.2.10 @SR-1.2.2.13 @SR-1.2.2.19  @SR-1.2.3.11 
    Scenario: Force beds creation to obtain the bed limits popup
        Given Tom goes to "Tucana" Web APP login page
        And Tom logs in with his credentials
        And Tom sees the dashboard
        When Tom clicks on "Bed Management" Option
        Then Tom sees the "Bed Management" Page
        And Tom clicks on the "Back to Step One" button
        And Tom completes the 64 beds limits
        Then Tom wants to create one bed more and see the Bed Limit Reached popup
        Then Tom closes the Bed Limit popup
        Then Tom sees the "Bed Management" Page
        Then Tom deletes all created beds