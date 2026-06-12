import pytest
from pages.product_page import ProductPage
from pages.cart_page import CartPage




#TC_01 - Add out-of-stock product to cart and verify product is not added
#Given that Add to cart button is not displayed when product is out of stock, we only verify if Add to cart button is visible
@pytest.mark.regression
def test_TC01_failed_add_outofstock_product_to_cart(driver, base_url):
    #Instance of ProductPage class
    product_page = ProductPage(driver)
    
    #local variables for TC_01
    url_out_of_stock_product = "custom-t-shirt"
    
    #concatenation of base_url + name of the product in URL format
    product_page.driver.get(base_url + url_out_of_stock_product)
    
    #assertion "NOT" to return False - which is the expected value
    assert not product_page.is_element_visible(product_page.button_add_to_cart)
    assert not product_page.is_added_to_cart_message_displayed()
    
    


#TC_02 - Add available product to cart and verify if "added to cart" message is displayed
@pytest.mark.smoke
def test_TC02_add_available_product_to_cart(driver, base_url):
    
    product_page = ProductPage(driver)
    
    product_page.navigate_to_product_page(base_url)
    product_page.add_product_to_cart(1)
    assert product_page.is_added_to_cart_message_displayed()  #Waiting for "Added to cart" message to appear
    
    
    
    
#TC_03 - Add product to cart and verify it appears in the cart by navigating and checking in cart page
@pytest.mark.smoke
def test_TC03_add_product_verify_displayed_in_cart(driver, base_url):
    
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)
    
    product_page.navigate_to_product_page(base_url)
    product_page.add_product_to_cart(1)
    assert product_page.is_added_to_cart_message_displayed()  #Waiting for "Added to cart" message to appear
    cart_page.navigate_to_cart_page(base_url)                 #Then navigates to cart page to verify if product is successfully added
    assert cart_page.is_product_in_cart(product_page.product_name_text)
    
    
    
    
#TC_04 - Add second product and verify cart item count is updated
@pytest.mark.smoke
def test_TC04_add_second_product_verify_count_update(driver, base_url):
    
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)
    
    product_page.driver.get(base_url + product_page.url_name_product) 
    product_page.add_product_to_cart(1)
    assert product_page.is_added_to_cart_message_displayed()  #Waiting for "Added to cart" message to appear
    product_page.driver.get(base_url + product_page.url_name_product_2) 
    product_page.add_product_to_cart(1)
    assert product_page.is_added_to_cart_message_displayed()  #Waiting for "Added to cart" message to appear
    cart_page.navigate_to_cart_page(base_url)
    assert cart_page.get_cart_items_count() == 2




