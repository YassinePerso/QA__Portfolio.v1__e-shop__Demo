Feature: Checkout
  As a logged-in user
  I want to complete the checkout process
  So that I can place my order


  Background:
    Given User is logged in with an empty cart


  #TC_001
  @smoke @checkout
  Scenario: Add a product and go to checkout page as logged-in user
      When  User adds the product to cart
      Then  User should see the added to cart message
      When  User goes to the cart page
      And   User accepts terms of service
      And   User clicks the checkout button
      Then  User should be redirected to the checkout page


  #TC_002
  @regression @checkout
  Scenario: Go to checkout with empty cart as logged-in user
      When  User goes to the cart page
      Then  Checkout button should not be visible


  #TC_003
  @smoke @checkout
  Scenario: Add a product and verify total amount is visible in checkout page
      When  User adds the product to cart
      Then  User should see the added to cart message
      When  User goes to the cart page
      And   User accepts terms of service
      And   User clicks the checkout button
      And   User completes checkout with cash on delivery up to payment info
      Then  Total price should be visible in checkout page


  #TC_004
  @smoke @checkout
  Scenario: Complete payment with valid information and verify order confirmation
      When  User adds the product to cart
      Then  User should see the added to cart message
      When  User goes to the cart page
      And   User accepts terms of service
      And   User clicks the checkout button
      And   User completes the full checkout with cash on delivery
      Then  Order should be confirmed


  #TC_006
  @regression @checkout
  Scenario: Failed payment with invalid credit card details
      When  User adds the product to cart
      Then  User should see the added to cart message
      When  User goes to the cart page
      And   User accepts terms of service
      And   User clicks the checkout button
      And   User completes checkout with credit card payment using invalid details
      Then  User should see an error message for invalid card details