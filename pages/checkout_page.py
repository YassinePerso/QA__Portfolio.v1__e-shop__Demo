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
        
        # -------CREDIT CART Payment method ------- #
        # CREDIT CARD payment method
        self.credit_card_payment_method = (By.ID, "paymentmethod_2")
        #Input SELECT - to choose between different credit cards (amex, visa, mastercard etc ...)
        self.type_credit_card_select_input = (By.ID, "CreditCardType")
        #Text - Enter card holder name
        self.card_holder_name_input = (By.ID, "CardholderName")
        #Text - Enter car number
        self.card_number_input = (By.ID, "CardNumber")
        #Input SELECT - Expiration date - MONTH
        self.expiration_date_month = (By.ID, "ExpireMonth")
        #Input SELECT - Expiration date - YEAR
        self.expiration_date_year = (By.ID, "ExpireYear")
        #Text - Enter card code
        self.card_code_input = (By.ID, "CardCode")
        #Error message when invalid card details are completed
        self.error_message_invalid_card_info = (By.XPATH, "//li[normalize-space()='Wrong card number']")

        
        
        
    # Billing Address
    def select_billing_address(self):
        dropdown = Select(self.find_element(self.billing_address_input))    #Using Select() function to select dropdown's options
        dropdown.select_by_index(0)     #Select the first option in the list with select_by_index() function - (index[0] = first)
        self.click(self.billing_address_continue_button)


    #Shipping Address  
    def select_shipping_address(self):
        dropdown = Select(self.find_element(self.shipping_address_input))    #Using Select() function to select dropdown's options
        dropdown.select_by_index(0)     #Select the first option in the list with select_by_index() function - (index[0] = first)
        self.click(self.shipping_address_continue_button)


    #Shipping Method
    def select_shipping_method(self):
        self.click(self.ground_shipping_method)
        self.click(self.shipping_method_continue_button)


    #Payment Method - CASH ON DELIVERY 
    def select_cash_on_delivery_payment(self):
        self.click(self.cash_on_delivery_payment_method)
        self.click(self.payment_method_continue_button)
        
    
    #Payment Method - CREDIT CARD
    def select_credit_card_payment(self):
        self.click(self.credit_card_payment_method)
        self.click(self.payment_method_continue_button)
        
        
        
    #Complete Credit Card informations
    def complete_credit_card_informations(self):
        
        holder_name = "Yass"                                   #Invalid holder name data to trigger payment failure
        card_number = "4587 9581 3264 7412 84362 65874 123"    #Invalid card number to trigger payment failure
        card_code = "846"                                      #Invalid card code to trigger payment failure
        
        #Selecting credit card type in dropdown
        type_credit_card_dropdown = Select(self.find_element(self.type_credit_card_select_input))    #Using Select() function to select dropdown's options
        type_credit_card_dropdown.select_by_index(1)                #Selecting the second option - MASTER CARD
        self.type_text(self.card_holder_name_input, holder_name)    #Typing text in "holder card name" input
        self.type_text(self.card_number_input, card_number)         #Typing text in "card number" input
        
        expiration_month_dropdown = Select(self.find_element(self.expiration_date_month))    #Using Select() function to select dropdown's options
        expiration_month_dropdown.select_by_index(0)   #(= January)
        
        expiration_year_dropdown = Select(self.find_element(self.expiration_date_year))    #Using Select() function to select dropdown's options
        expiration_year_dropdown.select_by_index(0)    #(= 2026)
        
        self.type_text(self.card_code_input, card_code) #Entering card code number 
        self.click(self.payment_info_continue_button)



    #Payment Information
    def continue_payment_info(self):
        self.click(self.payment_info_continue_button)
        
        
    #Confirm Order
    def confirm_order(self):
        self.click(self.confirm_order_button)


    #Verify if order confirmed
    def is_order_confirmed(self):
        return self.is_element_visible(self.message_successful_order)
    
    
    #ERROR MESSAGE - Failed credit card payment - Invalid details
    def get_error_message_invalid_card_details(self):
        return self.is_element_visible(self.error_message_invalid_card_info)
    
    #Global method that includes all actions to perform a complete checkout - (CASH ON DELIVERY)
    def complete_checkout(self):
        self.select_billing_address()
        self.select_shipping_address()
        self.select_shipping_method()
        self.select_cash_on_delivery_payment()
        self.continue_payment_info()
        self.confirm_order()
    