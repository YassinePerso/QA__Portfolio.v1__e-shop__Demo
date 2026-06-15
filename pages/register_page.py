from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RegisterPage (BasePage):

    def __init__(self, driver):
        # super() is used to call the __init__ method of the parent class (BasePage) and pass the driver argument to it
        # so that we can use the driver in the RegisterPage class
        super().__init__(driver)
        self.firstname_input = (By.ID, "FirstName")
        self.lastname_input = (By.ID, "LastName")
        self.email_input = (By.ID, "Email")
        self.password_input = (By.ID, "Password")
        self.confirm_password_input = (By.ID, "ConfirmPassword")
        self.register_button = (By.ID, "register-button")
        self.url_register = "register"

    # Navigate to regsiter page

    def navigate_to_register_page(self, base_url):
        self.driver.get(base_url + self.url_register)

    # Enter firstname

    def enter_firstname(self, firstname):
        self.type_text(self.firstname_input, firstname)

    # Enter lastname
    def enter_lastname(self, lastname):
        self.type_text(self.lastname_input, lastname)

    # Enter email
    def enter_email(self, email):
        self.type_text(self.email_input, email)

    # Enter password
    def enter_password(self, password):
        self.type_text(self.password_input, password)

    # Enter confirm password
    def enter_confirm_password(self, confirm_password):
        self.type_text(self.confirm_password_input, confirm_password)

    # Click register button
    def click_register_button(self):
        self.click(self.register_button)

    # Method that performs all needed actions to register
    def register(self, firstname, lastname, email, password, confirm_password):
        self.enter_firstname(firstname)
        self.enter_lastname(lastname)
        self.enter_email(email)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)
        self.click_register_button()

    # If test case is negative, get the error message text and return it

    def get_error_message(self):
        # Locator for error message element (same locator for all)
        error_message_locator = (By.CSS_SELECTOR, "span[class='field-validation-error']")
        # Using .get_element_text() function of BasePage class to find error message element and return its text
        return self.get_element_text(error_message_locator)

    # Get error message is email is ALREADY REGISTERED

    def get_error_message_already_registered_email(self):
        # Locator for error message element (same locator for all)
        error_message_locator = (By.CSS_SELECTOR, "div[class='validation-summary-errors'] ul li")
        # Using .get_element_text() function of BasePage class to find error message element and return its text
        return self.get_element_text(error_message_locator)

    # Checking if registration is successful by checking if the logout link is visible since the URL does not change upon successful registration.

    def is_registration_successful(self):
        # Locator for logout link, which is only visible when registration is successful
        logout_link_locator = (By.CSS_SELECTOR, "a[class='ico-logout']")
        # Using .is_element_visible() function of BasePage class to check if logout link is visible, which indicates that registration was successful
        return self.is_element_visible(logout_link_locator)
