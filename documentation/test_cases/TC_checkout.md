### US-05 : Checkout



#### Acceptance Criteria
- [ ] Cart must contain at least one product before accessing checkout
- [ ] Total of amount of order is visible in checkout page
- [ ] Client can pay from checkout page
- [ ] When payment is done, client receives a "successful order payment" e-mail
- [ ] If payment fails, an error message is displayed and the order is not confirmed



User Story 5: Checkout
    AC1:
        → TC-001 : Add a product and go to checkout page → PASS
        → TC-002 : Go to empty cart page then go to checkout page → FAIL
    AC2:
        → TC-003 : Add a product and check if total of amount is visible in checkout page → PASS

    AC3 + AC4 :
        → TC-004 : Complete payment with valid credentials and verify if order is confirmed → PASS
        → TC-005 : Pay the order and check if "successful order payment" email is received → PASS
    AC5:
        → TC-006 : Make the payment fail and check if an error message is displayed and the order is not confirmed → PASS




| TC ID | Title | Preconditions | Steps | Expected Result | Status |
|-------|-------|---------------|-------|-----------------|--------|
| TC-001 | Add a product and go to checkout page | User is logged-in and on product page | 1. Go to product page 2. Add available product to cart 3. Go to cart page 4. Click Checkout | Checkout page is displayed | TODO |
| TC-002 | Go to checkout with empty cart | User is logged-in and on cart page | 1. Go to cart page 2. Ensure cart is empty 3. Click Checkout | User cannot proceed to checkout, error message is displayed | TODO |
| TC-003 | Add a product and verify total amount is visible in checkout page | User is logged-in and on product page | 1. Go to product page 2. Add available product to cart 3. Go to cart page 4. Click Checkout 5. Check total amount | Total amount of order is visible on checkout page | TODO |
| TC-004 | Complete payment with valid credentials and verify order is confirmed | User is logged-in and on checkout page with product in cart | 1. Go to checkout page 2. Fill in payment details 3. Click Pay | Order is confirmed | TODO |
| TC-005 | Pay the order and verify confirmation email is received | User is logged-in and on checkout page with product in cart | 1. Go to checkout page 2. Fill in payment details 3. Click Pay 4. Check email inbox | Confirmation email is received | TODO |
| TC-006 | Make payment fail and verify error message and order not confirmed | User is logged-in and on checkout page with product in cart | 1. Go to checkout page 2. Fill in invalid payment details 3. Click Pay | Error message is displayed and order is not confirmed | TODO |