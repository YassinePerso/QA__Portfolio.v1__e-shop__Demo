import pytest
from pages.product_page import ProductPage
from pages.cart_page import CartPage





#TC_01 - Add a product and go to checkout page AS LOGGED-IN USER
@pytest.mark.smoke
def test_TC01_add_product_and_go_checkout_page_as_logged_in_user(base_url, logged_in_user):
    
    product_page = ProductPage(logged_in_user)
    cart_page = CartPage(logged_in_user)
    
    url = "https://demowebshop.tricentis.com/onepagecheckout"
    
    product_page.navigate_to_product_page(base_url)
    product_page.add_product_to_cart(1)
    cart_page.navigate_to_cart_page(base_url)
    assert cart_page.is_element_visible(cart_page.checkout_button)
    cart_page.accept_terms()
    cart_page.click_checkout_button()
    assert cart_page.get_current_url() == url




#TC_02 - Go to checkout with empty cart AS LOGGED-IN USER
@pytest.mark.regression
def test_TC02_go_checkout_page_with_empty_cart(base_url, logged_in_user, empty_cart):
    
    cart_page = CartPage(logged_in_user)
    cart_page.navigate_to_cart_page(base_url)
    assert not cart_page.is_element_visible(cart_page.checkout_button)




#TC_03 - Add a product and verify total amount is visible in checkout page
@pytest.mark.smoke
def test_TC03_add_product_verify_total_amount_visible(base_url, logged_in_user, empty_cart):
    
    product_page = ProductPage(logged_in_user)
    cart_page = CartPage(logged_in_user)
    
    product_page.navigate_to_product_page(base_url)
    product_page.add_product_to_cart(1)
    cart_page.navigate_to_cart_page(base_url)
    assert cart_page.is_element_visible(cart_page.total_price)




#TC_04 - Complete payment with valid credentials and verify order is confirmed



#TC_05 - Pay the order and verify confirmation email is received



#TC_06 - Make payment fail and verify error message and order not confirmed