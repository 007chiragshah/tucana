Feature: User Login

  Scenario: Happy Path
    Given the application is running
    And a valid request to login a user
    And the user trying to login exists
    When the request is made to login a user
    Then the user is told the request was successful
    And access and refresh tokens are provided

  Scenario: User doesn't exist
    Given the application is running
    And a valid request to login a user
    When the request is made to login a user
    Then the user is told the request was unauthorized

  Scenario: Wrong password
    Given the application is running
    And a valid request to login a user
    And the user trying to login exists
    And the provided password is wrong
    When the request is made to login a user
    Then the user is told the request was unauthorized

  Scenario: Login User - Invalid Password max attempts
    Given the application is running
    And a valid request to login a user
    And the user trying to login exists
    And the provided password is wrong
    And is the last available login attempt
    When the request is made to login a user
    Then the user is told the request was unauthorized
    And the account logging in was locked

  Scenario: Account is locked
    Given the application is running
    And a valid request to login a user
    And the user trying to login exists
    And the account is locked
    When the request is made to login a user
    Then the user is told the request was forbidden

  Scenario: Empty password
    Given the application is running
    And a valid request to login a user
    And the user trying to login exists
    And the provided password is empty
    When the request is made to login a user
    Then the user is told the request was unauthorized
