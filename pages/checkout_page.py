from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from selenium.webdriver.common.by import By



class CheckoutPage (BasePage):
    
    def __init__(self, driver):
        #super() is used to call the __init__ method of the parent class (BasePage) and pass the driver argument to it, so that we can use the driver in the RegisterPage class
        super().__init__(driver)
        #Billing Adress
        self.billing_address_input = (By.ID, "billing-address-select")
        self.billing_address_continue_button = (By.XPATH, "//input[@onclick='Billing.save()']")
        #Shipping Address
        self.shipping_address_input = (By.ID, "shipping-address-select")
        self.shipping_address_continue_button = (By.XPATH, "//input[@onclick='Shipping.save()']")
        #Shipping Method
        self.ground_shipping_method = (By.ID, "shippingoption_0")
        self.shipping_method_continue_button = (By.XPATH, "//input[@class='button-1 shipping-method-next-step-button']")
        #Payment Method
        self.cash_on_delivery_payment_method = (By.ID, "paymentmethod_0")
        self.payment_method_continue_button = (By.XPATH, "//input[@class='button-1 payment-method-next-step-button']")
        #Payment information
        self.payment_info_continue_button = (By.XPATH, "//input[@class='button-1 payment-info-next-step-button']")
        #Confirm Order
        self.total_price_order = (By.CSS_SELECTOR, "span[class='product-price order-total'] strong")
        self.confirm_order_button = (By.XPATH, "//input[@value='Confirm']")
        #URL - confirmed order 
        self.url_confirmed_order = "checkout/completed/"
        self.message_successful_order = (By.XPATH, "//strong[normalize-space()='Your order has been successfully processed!']")
        
        
        
        
    # Billing Address
    def select_billing_address(self):
        dropdown = Select(self.find_element(self.billing_address_input))    #Using Select() function to select dropdown's options
        dropdown.select_by_index(0)     #Select the first option in the list with select_by_index() function - (index[0] = first)
        self.click(self.billing_address_continue_button)



    # Shipping Address  
    def select_shipping_address(self):
        dropdown = Select(self.find_element(self.shipping_address_input))    #Using Select() function to select dropdown's options
        dropdown.select_by_index(0)     #Select the first option in the list with select_by_index() function - (index[0] = first)
        self.click(self.shipping_address_continue_button)

    # Shipping Method
    def select_shipping_method(self):
        self.click(self.ground_shipping_method)
        self.click(self.shipping_method_continue_button)

    # Payment Method
    def select_payment_method(self):
        self.click(self.cash_on_delivery_payment_method)
        self.click(self.payment_method_continue_button)

    # Payment Information
    def continue_payment_info(self):
        self.click(self.payment_info_continue_button)

    # Confirm Order
    def confirm_order(self):
        self.click(self.confirm_order_button)

    # Verify order confirmed
    def is_order_confirmed(self):
        return self.is_element_visible(self.message_successful_order)
    
    # Global method - complete checkout
    def complete_checkout(self):
        self.select_billing_address()
        self.select_shipping_address()
        self.select_shipping_method()
        self.select_payment_method()
        self.continue_payment_info()
        self.confirm_order()
    