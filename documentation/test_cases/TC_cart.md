### US-04 : Add to Cart

#### Acceptance Criteria
- [ ] Product must be available (in stock)
- [ ] When added, the product appears in the cart
- [ ] Cart item count is updated after adding a product
- [ ] If product is out of stock, an error message is displayed and product cannot be added




User Story 4: Add to Cart
    AC1:
        → TC-001 : Add out-of-stock product to cart and verify if product is added to cart → FAIL
        → TC-002 : Add available product to cart → PASS

    AC2:
        → TC-003 : Add product to cart and verify if it appears in the cart → PASS

    AC3:
        → TC-004 : Add second product to cart and verify if carti item count is updated → PASS

    AC4:
        → TC-005 : Add out-of-stock product and verify in an error message is displayed → PASS




| TC ID | Title | Preconditions | Steps | Expected Result | Status |
|-------|-------|---------------|-------|-----------------|--------|
| TC-001 | Add out-of-stock product to cart and verify product is not added | User is on product page | 1. Go to product page 2. Select out-of-stock product 3. Click Add to Cart | Product is not added to cart | TODO |
| TC-002 | Add available product to cart | User is on product page | 1. Go to product page 2. Select available product 3. Click Add to Cart | Product is successfully added to cart | TODO |
| TC-003 | Add product to cart and verify it appears in the cart | User is on product page | 1. Go to product page 2. Select available product 3. Click Add to Cart 4. Go to cart page | Product appears in cart | TODO |
| TC-004 | Add second product and verify cart item count is updated | User has one product in cart and is on product page | 1. Go to product page 2. Select a second available product 3. Click Add to Cart 4. Check cart item count | Cart item count is updated | TODO |
| TC-005 | Add out-of-stock product and verify error message is displayed | User is on product page | 1. Go to product page 2. Select out-of-stock product 3. Click Add to Cart | An error message is displayed | TODO |