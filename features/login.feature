
Feature: Account Login
  As a visitor
  I want to log into my account
  So that I can access my account and place orders

  Background:
    Given User is on the login page

  #TC_001
  @smoke @login
    Scenario: Successful login with valid credentials
        When User enters valid e-mail and password
        And User clicks the login button
        Then User should be logged in successfully
        And User should be redirected to home page

  #TC_002
  @regression @login
    Scenario: Failed login with invalid e-mail
        When User enters invalid e-mail and valid password
        And User clicks the login button
        Then User should see an error message

  #TC_003
  @regression @login
    Scenario: Failed login with invalid password
        When User enters valid e-mail and invalid password
        And User clicks the login button
        Then User should see an error message
    
  #TC_004
  @regression @login
    Scenario: Failed login with empty e-mail and password fields
        When User leaves e-mail and password fields empty
        And User clicks the login button
        Then User should see an error message