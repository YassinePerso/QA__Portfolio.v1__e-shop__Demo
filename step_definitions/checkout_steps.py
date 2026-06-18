#Import needed
from pytest_bdd import scenarios, given, when, then
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import pytest


@pytest.fixture
def product_page(logged_in_user):
    return ProductPage(logged_in_user)

@pytest.fixture
def cart_page(logged_in_user):
    return CartPage(logged_in_user)

@pytest.fixture
def checkout_page(logged_in_user):
    return CheckoutPage(logged_in_user)


scenarios("../features/checkout.feature")


# Steps of SCENARIO__01 -> Add a product and go to checkout page as logged-in user
@given("User is logged in with an empty cart")
def user_logged_in_empty_cart(logged_in_user, empty_cart):
    pass  # logged_in_user and empty_cart fixtures already handle login and cart cleanup

@when("User adds the product to cart")
def add_product_to_cart(product_page, base_url):
    product_page.navigate_to_product_page(base_url)
    product_page.add_product_to_cart(1)

@then("User should see the added to cart message")
def verify_added_to_cart_message(product_page):
    assert product_page.is_added_to_cart_message_displayed()

@when("User goes to the cart page")
def go_to_cart_page(cart_page, base_url):
    cart_page.navigate_to_cart_page(base_url)

@when("User accepts terms of service")
def accept_terms_of_service(cart_page):
    cart_page.accept_terms()

@when("User clicks the checkout button")
def click_checkout_button(cart_page):
    cart_page.click_checkout_button()

@then("User should be redirected to the checkout page")
def verify_redirected_to_checkout_page(cart_page):
    url = "https://demowebshop.tricentis.com/onepagecheckout"
    assert cart_page.get_current_url() == url


# Steps of SCENARIO__02 -> Go to checkout with empty cart as logged-in user
@then("Checkout button should not be visible")
def verify_checkout_button_not_visible(cart_page):
    assert not cart_page.is_element_visible(cart_page.checkout_button)


# Steps of SCENARIO__03 -> Add a product and verify total amount is visible in checkout page
@when("User completes checkout with cash on delivery up to payment info")
def complete_checkout_cash_on_delivery_up_to_payment_info(checkout_page):
    checkout_page.select_billing_address()
    checkout_page.select_shipping_address()
    checkout_page.select_shipping_method()
    checkout_page.select_cash_on_delivery_payment()
    checkout_page.continue_payment_info()

@then("Total price should be visible in checkout page")
def verify_total_price_visible(checkout_page):
    assert checkout_page.is_element_visible(checkout_page.total_price_order)


# Steps of SCENARIO__04 -> Complete payment with valid information and verify order confirmation
@when("User completes the full checkout with cash on delivery")
def complete_full_checkout_cash_on_delivery(checkout_page):
    checkout_page.complete_checkout()

@then("Order should be confirmed")
def verify_order_confirmed(checkout_page):
    assert checkout_page.is_order_confirmed()


# Steps of SCENARIO__06 -> Failed payment with invalid credit card details
@when("User completes checkout with credit card payment using invalid details")
def complete_checkout_credit_card_invalid_details(checkout_page):
    checkout_page.select_billing_address()
    checkout_page.select_shipping_address()
    checkout_page.select_shipping_method()
    checkout_page.select_credit_card_payment()
    checkout_page.complete_credit_card_informations()

@then("User should see an error message for invalid card details")
def verify_error_message_invalid_card_details(checkout_page):
    assert checkout_page.get_error_message_invalid_card_details()