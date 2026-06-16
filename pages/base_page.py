from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Make webdriver wait until the element is visible, then return the element
    def find_element(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element

    # Make webdriver wait until the element is clickable, then click on the element
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    # Make webdriver wait until the element is visible, then type the text in the element
    def type_text(self, locator, text):
        type_text = self.wait.until(EC.visibility_of_element_located(locator))
        type_text.send_keys(text)

    # Return the text of the element
    def get_element_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    # Make webdriver wait until the element is visible, then return True if the element is visible, otherwise return False
    def is_element_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:  # TimeoutException - when the element is not found within the specified time, so we catch it and return False
            return False

    # Get current url method, return the current url of the page
    def get_current_url(self):
        return self.driver.current_url
