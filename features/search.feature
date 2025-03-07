Feature: Search functionality

  @completed
  Scenario: Search for a valid product
    Given User navigate to home page
    When User enters product name in the search box
    And clicks on Search button
    Then product should be displayed in the search results

  @completed
  Scenario: Search for a Invalid product
    Given User navigate to home page
    When User enters invalid product name in the search box
    And clicks on Search button
    Then Message is displayed saying enter the valid product name in the search results

  @completed
  Scenario: Search for entering any product
    Given User navigate to home page
    When User do not enters any product in the search box
    And clicks on Search button
    Then Message is displayed saying enter the valid product name in the search results
