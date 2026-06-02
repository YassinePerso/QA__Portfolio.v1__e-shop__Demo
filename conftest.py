import pytest
from selenium import webdriver
# Global fixtures for Pytest


#Driver - fixture for Selenium tests
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


#Base_url - fixture for test URLs
@pytest.fixture
def base_url():
    return "https://demowebshop.tricentis.com/"


#Logged-in user fixture for authentication tests (required for cart and checkout tests)
@pytest.fixture
def logged_in_user(driver, base_url):
    driver.get(base_url + "login")
    driver.find_element("id", "Email").send_keys("testuser@example.com")
    driver.find_element("id", "Password").send_keys("Password123!")
    driver.find_element("xpath", "//input[@value='Log in']").click()
    yield driver
