Feature: Add to cart
  As a visitor
  I want to add products to cart
  So that I can buy the product later


  #TC_001
  @regression @cart
  Scenario: Try to add out-of-stock product to cart
      Given User is on the out-of-stock product page
      Then  Add to cart button should not be visible
      And   Added to cart message should not be displayed


  #TC_002
  @smoke @cart
  Scenario: Add available product to cart
      Given User is on the product page
      When  User adds the product to cart
      Then  User should see the added to cart message


  #TC_003
  @smoke @cart
  Scenario: Add product and verify it appears in the cart
      Given User is on the product page
      When  User adds the product to cart
      Then  User should see the added to cart message
      When  User goes to the cart page
      Then  Product should be visible in the cart


  #TC_004
  @smoke @cart
  Scenario: Add second product and verify cart item count is updated
      Given User is on the first product page
      When  User adds the first product to cart
      Then  User should see the added to cart message
      When  User navigates to the second product page
      And   User adds the second product to cart
      Then  User should see the added to cart message
      When  User goes to the cart page
      Then  Cart item count should be 2