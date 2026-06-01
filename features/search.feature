
Feature: Product Search
  As a visitor
  I want to search product in search bar
  So that I can find the product I want to buy


  Background:
    Given User is on the home page


    #TC_001
    @smoke @search
    Scenario: Successful search with valid product name
        When User enters valid product name in search bar
        And User clicks the search button
        Then User should see matching product result(s) displayed


    #TC_002
    @regression @search
    Scenario: Search with no matching results
        When User enters non-existent product name in search bar
        And User clicks the search button
        Then User should see a message indicating no results found


    #TC_003
    @regression @search
    Scenario: Search is case-insensitive
        When User enters valid product name with wrong case in search bar
        And User clicks the search button
        Then User should see matching product result(s) displayed


    #TC_004
    @regression @search
    Scenario: Search with special characters
        When User enters product name with special characters in search bar
        And User clicks the search button
        Then User should see matching product result(s) displayed


    #TC_005
    @regression @search
    Scenario: Search with less than 3 characters
        When User enters a search term with less than 3 characters in search bar
        And User clicks the search button
        Then User should see a minimum length error message

   