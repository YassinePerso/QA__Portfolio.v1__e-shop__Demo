#Import needed
from pytest_bdd import scenarios, given, when, then
from pages.product_page import ProductPage
from pages.cart_page import CartPage
import pytest


@pytest.fixture
def product_page(driver):
    return ProductPage(driver)

@pytest.fixture
def cart_page(driver):
    return CartPage(driver)


scenarios("../features/cart.feature")


# Steps of SCENARIO__01 -> Try to add out-of-stock product to cart
@given("User is on the out-of-stock product page")
def navigate_to_outofstock_product(product_page, base_url):
    url_out_of_stock_product = "custom-t-shirt"
    product_page.driver.get(base_url + url_out_of_stock_product)

@then("Add to cart button should not be visible")
def verify_add_to_cart_button_not_visible(product_page):
    assert not product_page.is_element_visible(product_page.button_add_to_cart)

@then("Added to cart message should not be displayed")
def verify_added_to_cart_message_not_displayed(product_page):
    assert not product_page.is_added_to_cart_message_displayed()


# Steps of SCENARIO__02 -> Add available product to cart
@given("User is on the product page")
def navigate_to_product_page(product_page, base_url):
    product_page.navigate_to_product_page(base_url)

@when("User adds the product to cart")
def add_product_to_cart(product_page):
    product_page.add_product_to_cart(1)

@then("User should see the added to cart message")
def verify_added_to_cart_message_displayed(product_page):
    assert product_page.is_added_to_cart_message_displayed()


# Steps of SCENARIO__03 -> Add product and verify it appears in the cart
@when("User goes to the cart page")
def go_to_cart_page(cart_page, base_url):
    cart_page.navigate_to_cart_page(base_url)

@then("Product should be visible in the cart")
def verify_product_visible_in_cart(cart_page, product_page):
    assert cart_page.is_product_in_cart(product_page.product_name_text)


# Steps of SCENARIO__04 -> Add second product and verify cart item count is updated
@given("User is on the first product page")
def navigate_to_first_product_page(product_page, base_url):
    product_page.driver.get(base_url + product_page.url_name_product)

@when("User adds the first product to cart")
def add_first_product_to_cart(product_page):
    product_page.add_product_to_cart(1)

@when("User navigates to the second product page")
def navigate_to_second_product_page(product_page, base_url):
    product_page.driver.get(base_url + product_page.url_name_product_2)

@when("User adds the second product to cart")
def add_second_product_to_cart(product_page):
    product_page.add_product_to_cart(1)

@then("Cart item count should be 2")
def verify_cart_item_count(cart_page):
    assert cart_page.get_cart_items_count() == 2