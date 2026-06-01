
Feature: Add to cart
  As a visitor
  I want to add product to cart
  So that I can buy the product later


  Background:
    Given User is on the home page


    #TC_001
    @smoke @cart
    Scenario: Add available product to cart
        When User navigates to a product page
        And User clicks the add to cart button
        Then User should see the product in the cart
        And User should see the cart item count updated


    #TC_002
    @regression @cart
    Scenario: Try to add out-of-stock product to cart
        When User adds an out-of-stock product to the cart
        And User clicks the add to cart button
        Then User should not be able to add the product to cart
        And User should see an error message



    #TC_003
    @regression @cart
    Scenario: Add two available product to cart and verify cart updates
        When User adds two available product to the cart
        And User clicks the add to cart button
        Then User should see the product in the cart
        And User should see the cart item count updated