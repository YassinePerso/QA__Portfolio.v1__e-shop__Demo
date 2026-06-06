from pages.base_page import BasePage
from selenium.webdriver.common.by import By



class ProductPage (BasePage):
    
    def __init__(self, driver):
        #super() is used to call the __init__ method of the parent class (BasePage) and pass the driver argument to it, so that we can use the driver in the RegisterPage class
        super().__init__(driver)
        self.product_name = (By.CSS_SELECTOR, "h1[itemprop='name']")  
        self.button_add_to_cart = (By.CSS_SELECTOR, ".add-to-cart-button")
        self.quantity_input = (By.CSS_SELECTOR, ".qty-input") #CSS selector for the quantity input field
        self.added_to_cart_message = (By.CSS_SELECTOR, ".content")    #CSS selector for the message that appears when a product is added to the cart
        self.url_name_product = "black-white-diamond-heart"
    
    
    #Get the product name
    def get_product_name(self):
        return self.get_element_text(self.product_name)
    
        #Method to enter value in quantity input
    def enter_quantity(self, value):
        self.type_text(self.quantity_input, value)
    
    
    #Method to click the button "Add to cart"
    def click_add_to_cart_button(self):
        self.click(self.button_add_to_cart)
        
        
    #GLobal method to add a product to the cart, which includes entering the quantity and clicking the "Add to cart" button
    def add_product_to_cart(self, quantity=1):
        self.enter_quantity(quantity)
        self.click_add_to_cart_button()
        
        
    #Method to get message that appears when a product is added to the cart
    def is_added_to_cart_message_displayed(self):
        return self.is_element_visible(self.added_to_cart_message)
    
    
    #Method to navigate to the product page (concatenating the base URL with the product URL)
    def navigate_to_product_page(self, base_url):
        self.driver.get(base_url + self.url_name_product)