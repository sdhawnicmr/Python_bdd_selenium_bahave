Feature: Login functionality

  Scenario: Login with valid credentials
    Given User navigates to Login page
    When user enters correct username and password
    And User clicks on Login button
    Then user should be successfully logged In

  @Login
  Scenario: Login with Invalid username and valid password
    Given User navigates to Login page
    When user enters Incorrect username and Valid password
    And User clicks on Login button
    Then user should be get message to Enter valid username

  @Login
  Scenario: Login with valid username and Invalid password
    Given User navigates to Login page
    When user enters correct username and Invalid password
    And User clicks on Login button
    Then user should get message to Enter Invalid password