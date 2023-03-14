Feature: HomePage Functionality

  Scenario: Checking location functionalities in HomePage
    Given I open Application URL in the Browser
    And I click the search bar
    When I enter the preferred location
    And I click the search button
    Then I should get preferred location

  Scenario: Checking MB prime functionalities in HomePage
    Given I open Application URL in the Browser
    And I click mb prime button
    When I click join now  button
    Then I should get into MB Prime page

  Scenario: Checking Help functionalities in HomePage
    Given I open Application URL in the Browser
    And I click help tab
    When I click help center button
    And I raise my question and search
    Then I should get answers

  Scenario: Checking Header Tabs in HomePage
    Given I open Application URL in the Browser
    And I click buy and rent buttons
    When I click sell and home loans buttons
    And I click property and mb advices buttons
    Then I should able to open all tabs

  Scenario: Checking Stores section in HomePage
    Given I open Application URL in the Browser
    And I scroll down to bottom of the page
    When I click playstore button
    And I should get navigate to the play store
    And I click app store
    Then I should get navigate to the app store

  Scenario: Checking SocialMedia sections in HomePage
    Given I open Application URL in the Browser
    And I scroll down to bottom of the page
    When I click the social media buttons
    Then I should get into social media pages