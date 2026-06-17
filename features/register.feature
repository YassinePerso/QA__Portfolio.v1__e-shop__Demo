
Feature: Registration
  As a visitor
  I want to create a new account
  So that I can access my account and place orders


  Background:
    Given User is on the registration page


    #TC_001
    @smoke @register
    Scenario: Successful registration with valid e-mail and valid password
        When User enters firstname
        And  User enters lastname
        And  User enters valid e-mail
        And  User enters valid password
        And  User enters valid confirm password
        And  User clicks the register button
        Then User should be successfully registered
        And  User should be redirected to home page


    #TC_002
    @regression @register
    Scenario: Failed registration with invalid e-mail format
        When User enters firstname
        And  User enters lastname
        And  User enters invalid e-mail format
        And  User enters valid password
        And  User enters valid confirm password
        And  User clicks the register button
        Then User should see an error message


    #TC_003
    @regression @register
    Scenario Outline: Registration with different password lengths
        When User enters firstname
        And  User enters lastname
        And  User enters valid e-mail
        And  User enters password of <length> characters
        And  User enters confirm password of <length> characters
        And  User clicks the register button
        Then <result>

    Examples:
      | length | result                                        |
      | 5      | User should see an error message              |
      | 6      | User should be successfully registered        |
      | 7      | User should be successfully registered        |


    #TC_004
    @regression @register
    Scenario: Registration with existing e-mail
        When User enters firstname
        And  User enters lastname
        And  User enters existing e-mail
        And  User enters valid password
        And  User enters valid confirm password
        And  User clicks the register button
        Then User should see an error message

    
    #TC_005
    @regression @register
    Scenario: Failed registration with invalid credentials and verify if error message is displayed
        When User enters firstname
        And  User enters lastname
        And  User enters invalid e-mail
        And  User enters invalid password
        And  User enters invalid confirm password
        And  User clicks the register button
        Then User should see an error message


    