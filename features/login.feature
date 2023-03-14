Feature: Login Functionality

  Scenario: Login using valid email and password
    Given I open the Application URL in the Browser
    And I click the login tab
    When I open the login page
    And I enter email and password
    Then I should get logged in

  Scenario: Login using valid mobile number and otp
    Given I open the Application URL in the Browser
    And I click the login tab
    When I open the login page
    And I enter mobile number and otp
    Then I should get logged in

  Scenario: Login using Google Accounts
    Given I open the Application URL in the Browser
    And I click the login tab
    When I open the login page
    And I click the Google Logo
    Then I should get navigated to the Google account page