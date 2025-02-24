Feature: User Logout

  Scenario: Happy Path
    Given the application is running
    And a valid request to logout
    And the requester has role `clinical`
    And valid credentials are provided
    And the requester user exists
    When the request to logout is made
    Then the user is told the request was successful
    And the token is blacklisted

  Scenario: Password not required
    Given the application is running
    And a valid request to logout
    And the requester has role `admin`
    And the password is not provided
    And valid credentials are provided
    And the requester user exists
    When the request to logout is made
    Then the user is told the request was successful
    And the token is blacklisted

  Scenario: Password required but not provided
    Given the application is running
    And a valid request to logout
    And the requester has role `clinical`
    And the password is not provided
    And valid credentials are provided
    And the requester user exists
    When the request to logout is made
    Then the user is told the request was unauthorized

  Scenario: Invalid password provided
    Given the application is running
    And a valid request to logout
    And the requester has role `clinical`
    And a wrong password is provided
    And valid credentials are provided
    And the requester user exists
    When the request to logout is made
    Then the user is told the request was unauthorized

  Scenario: Invalid password provided - Max attempts
    Given the application is running
    And a valid request to logout
    And the requester has role `clinical`
    And a wrong password is provided
    And valid credentials are provided
    And the requester user exists
    And is the last available logout attempt
    When the request to logout is made
    Then the user is told the request was unauthorized
    And the account logging out was locked

  Scenario: Account is locked
    Given the application is running
    And a valid request to logout
    And the requester has role `clinical`
    And valid credentials are provided
    And the requester user exists
    And the logout account is locked
    When the request to logout is made
    Then the user is told the request was forbidden
