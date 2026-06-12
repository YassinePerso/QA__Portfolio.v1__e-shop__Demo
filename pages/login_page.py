from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage (BasePage):
    
    def __init__(self, driver):
        #super() is used to call the __init__ method of the parent class (BasePage) and pass the driver argument to it, so that we can use the driver in the LoginPage class
        super().__init__(driver)
        self.username_input = (By.ID, "Email")
        self.password_input = (By.ID, "Password")
        self.login_button = (By.XPATH, "//input[@value='Log in']")
        self.url_login = "login"
        
        
    #Navigate to login page  
    def navigate_to_login_page(self, base_url):
        self.driver.get(base_url + self.url_login)
        
    #Using type_text() function of BasePage class to find email input and fill it with value
    def enter_email(self, email):
        self.type_text(self.username_input, email)
        
        
    #Using type_text() function of BasePage class to find password input and fill it with value
    def enter_password(self, password):
        self.type_text(self.password_input, password)
        
        
    #Using click() function of BasePage class to find login button and click on it
    def click_login_button(self):
        self.click(self.login_button)
    
    
    #Complete login method that combines all the steps to perform login action
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
        
        
    #If test case is negative, get the error message text and return it
    def get_error_message(self):
        error_message_locator = (By.XPATH, "//span[@for='Email']")      #Locator for error message element
        return self.get_element_text(error_message_locator)      #Using .get_element_text() function of BasePage class to find error message element and return its text
    
    
    #Checking if login is succesful by checking if the logout link is visible since the URL does not change upon successful login
    def is_login_successful(self):
        #Locator for logout link, which is only visible when login is successful
        logout_link_locator = (By.CSS_SELECTOR, "a[class='ico-logout']")
        return self.is_element_visible(logout_link_locator)     #Using .is_element_visible() function of BasePage class to check if logout link is visible, which indicates that login was successful