Feature: Register new user functionality

  @register
  Scenario: Register a new user with valid details
    Given User navigates to Register page
    When user enters all the fields
    And User clicks on continue button
    Then user should be successfully Registered