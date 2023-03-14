Feature: SignUp Functionality

  Scenario: SignUp using valid details
    Given I open Application URL in the Browser
    And I click the login tab
    When I open the login page
    And I click signup and enter details
    Then I should get signed up