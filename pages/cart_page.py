from pages.base_page import BasePage
from selenium.webdriver.common.by import By



class CartPage (BasePage):
    
    def __init__(self, driver):
        #super() is used to call the __init__ method of the parent class (BasePage) and pass the driver argument to it, so that we can use the driver in the RegisterPage class
        super().__init__(driver)
        self.url_cart_page = "cart"    #URL for the cart page
        self.empty_cart_message = (By.XPATH, "//div[@class='order-summary-content']")    #Locator for the message that appears when the cart is empty
        self.cart_item_row = (By.CSS_SELECTOR, ".cart-item-row")    #Locator for the cart item row in the cart page
        self.cart_remove_checkbox = (By.XPATH, "//input[@name='removefromcart']")    #Locator for the checkbox to remove a product from the cart
        self.cart_item_name = (By.CSS_SELECTOR, ".product-name")  #Locator the product name in the cart item row
        self.cart_item_price = (By.CSS_SELECTOR, ".product-unit-price")    #Locator for the product price in the cart item row
        self.cart_item_quantity = (By.CSS_SELECTOR, ".qty-input")   #Locator for the iquantity input field in the cart item row
        self.cart_item_total = (By.CSS_SELECTOR, ".product-subtotal")   #Locator for the total price of the product in the cart item row
        self.update_cart_button = (By.CSS_SELECTOR, "input[value='Update shopping cart']")    #Locator for the button to update the cart
        self.continue_shopping_button = (By.CSS_SELECTOR, "input[value='Continue shopping']")    #Locator for the button to return to home page and continue shopping
        self.total_price = (By.CSS_SELECTOR, ".order-total .product-price")    #Locator for the total price of the cart in the cart page
        self.checkout_button = (By.ID, "checkout")    #Locator for the button to proceed to checkout
        
        
    #Method to navigate to cart page from home page
    def navigate_to_cart_page(self, base_url):
        self.driver.get(base_url + self.url_cart_page)
        
        
    #Method to verify is cart page is empty by checking if the empty cart message is displayed
    def is_cart_empty(self):
        return self.is_element_visible(self.empty_cart_message)
        
        
    #Method to check if remove checkbox is displayed for the product in the cart item row
    def is_remove_checkbox_displayed(self):
        return self.is_element_visible(self.cart_remove_checkbox)
        
        
    #Method to get the product name in the cart item row
    def get_cart_item_name(self):
        return self.get_element_text(self.cart_item_name)
        
        
    #Method to get the product price in the cart item row
    def get_cart_item_price(self):
        return self.get_element_text(self.cart_item_price)
        
        
    #Method to get the quantity of the product in the cart item row
    def get_cart_item_quantity(self):
        return self.get_element_text(self.cart_item_quantity)
        
        
    #Method to get the total price of the product in the cart item row
    def get_cart_item_total(self):
        return self.get_element_text(self.cart_item_total)
        
        
    #Method to click the button "Update shopping cart"
    def click_update_cart_button(self):
        self.click(self.update_cart_button)
            
            
    #Method to click the button "Continue shopping"
    def click_continue_shopping_button(self):
        self.click(self.continue_shopping_button)
        
    #Method to get the total price of the cart
    def get_total_price(self):
        return self.get_element_text(self.total_price)
        
    
    
    #----- Additional methods for more complex tests -----#
    
    #Method to get the total number of items in the cart
    def get_cart_items_count(self):
        self.driver.find_elements(*self.cart_item_row)
    
    