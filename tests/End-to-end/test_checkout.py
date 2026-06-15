import pytest
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


# TC_01 - Add a product and go to checkout page AS LOGGED-IN USER
@pytest.mark.smoke
def test_TC01_add_product_and_go_checkout_page_as_logged_in_user(base_url, logged_in_user, empty_cart):

    product_page = ProductPage(logged_in_user)
    cart_page = CartPage(logged_in_user)

    url = "https://demowebshop.tricentis.com/onepagecheckout"

    product_page.navigate_to_product_page(base_url)
    product_page.add_product_to_cart(1)
    assert product_page.is_added_to_cart_message_displayed()  # Waiting for "Added to cart" message to appear
    cart_page.navigate_to_cart_page(base_url)
    assert cart_page.is_element_visible(cart_page.checkout_button)
    cart_page.accept_terms()
    cart_page.click_checkout_button()
    assert cart_page.get_current_url() == url


# TC_02 - Go to checkout with empty cart AS LOGGED-IN USER
@pytest.mark.regression
def test_TC02_go_checkout_page_with_empty_cart(base_url, logged_in_user, empty_cart):

    cart_page = CartPage(logged_in_user)
    cart_page.navigate_to_cart_page(base_url)
    assert not cart_page.is_element_visible(cart_page.checkout_button)


# TC_03 - Add a product and verify total amount is visible in checkout page as LOGGED-IN USER
@pytest.mark.smoke
def test_TC03_add_product_verify_total_visible_in_checkout_page(base_url, logged_in_user, empty_cart):

    product_page = ProductPage(logged_in_user)
    cart_page = CartPage(logged_in_user)
    checkout_page = CheckoutPage(logged_in_user)

    product_page.navigate_to_product_page(base_url)
    product_page.add_product_to_cart(1)
    assert product_page.is_added_to_cart_message_displayed()  # Waiting for "Added to cart" message to appear
    cart_page.navigate_to_cart_page(base_url)
    cart_page.accept_terms()  # accept terms of service before clicking on checkout button
    cart_page.click_checkout_button()
    checkout_page.select_billing_address()
    checkout_page.select_shipping_address()
    checkout_page.select_shipping_method()
    checkout_page.select_cash_on_delivery_payment()
    checkout_page.continue_payment_info()
    # Check if total price is visible in checkout page
    assert checkout_page.is_element_visible(checkout_page.total_price_order)


# TC_04 - Complete payment with valid credentials and verify order is confirmed
@pytest.mark.smoke
def test_TC04_complete_payment_verify_order_confirmation(base_url, logged_in_user, empty_cart):

    product_page = ProductPage(logged_in_user)
    cart_page = CartPage(logged_in_user)
    checkout_page = CheckoutPage(logged_in_user)

    product_page.navigate_to_product_page(base_url)
    product_page.add_product_to_cart(1)
    assert product_page.is_added_to_cart_message_displayed()  # Waiting for "Added to cart" message to appear
    cart_page.navigate_to_cart_page(base_url)
    cart_page.accept_terms()  # accept terms of service before clicking on checkout button
    cart_page.click_checkout_button()
    checkout_page.complete_checkout()
    assert checkout_page.is_order_confirmed()


# TC_05 - Pay the order and verify confirmation email is received
@pytest.mark.regression
def test_TC05_verify_confirmation_email():
    pytest.skip("Not automated because email verification requires Gmail API integration (future improvement)")


# TC_06 - Make payment fail and verify error message and order not confirmed
@pytest.mark.regression
def test_TC06_failed_payment_verify_message(base_url, logged_in_user, empty_cart):

    product_page = ProductPage(logged_in_user)
    cart_page = CartPage(logged_in_user)
    checkout_page = CheckoutPage(logged_in_user)

    product_page.navigate_to_product_page(base_url)
    product_page.add_product_to_cart(1)
    product_page.is_added_to_cart_message_displayed()
    cart_page.navigate_to_cart_page(base_url)
    cart_page.accept_terms()  # accept terms of service before clicking on checkout button
    cart_page.click_checkout_button()
    checkout_page.select_billing_address()
    checkout_page.select_shipping_address()
    checkout_page.select_shipping_method()
    checkout_page.select_credit_card_payment()
    checkout_page.complete_credit_card_informations()  # Entering credit card informations
    # Checking if error message if visible because of invalid card details
    assert checkout_page.get_error_message_invalid_card_details()
