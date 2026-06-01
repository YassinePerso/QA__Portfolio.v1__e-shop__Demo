
Feature: Checkout
  As a logged-in user
  I want to have access to the checkout page
  So that I can complete my purchase


  Background:
    Given User is logged in
    And User is on the home page


    #TC_001
    @smoke @checkout
    Scenario: Add a product and go to checkout page
        When User adds a product to the cart
        And  User clicks the checkout button
        Then User should be redirected to the checkout page
        And  User should see the total amount of the purchase


    #TC_002
    @regression @checkout
    Scenario: Go to empty cart page then go to checkout page
        When User goes to the cart page with an empty cart
        Then User should not have access to the checkout page
        And  User should see a message indicating the cart is empty


    #TC_003
    @regression @checkout
    Scenario: Complete payment with valid payment details and verify if order is confirmed
        When User adds a product to the cart
        And  User clicks the checkout button
        And  User enters valid payment details
        And  User clicks the confirm order button
        Then User should see an order confirmation message
        And  User should receive an order confirmation email


    #TC_004
    @regression @checkout
    Scenario: Make the payment fail and check if an error message is displayed and the order is not confirmed
        When User adds a product to the cart
        And  User clicks the checkout button
        And  User enters invalid payment details
        And  User clicks the confirm order button
        Then User should see an error message indicating payment failure
        And  User should not receive an order confirmation email
        

   