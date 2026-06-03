#All imports needed
import pytest

from selenium import webdriver
from selenium .webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import os
from dotenv import load_dotenv

import csv



# ---------- Calling load_dotenv() function to load environment variables (not native with python) ---------- #

load_dotenv()



# ---------- Global fixtures for Pytest ---------- #

#Driver - fixture for Selenium tests
@pytest.fixture(scope="function")
def driver():
    
    options = Options()
    
    #if CI environment variable is set to "true", run in headless mode
    if os.getenv("CI"):
        options.add_argument("--headless")               #To make it run in headless mode for CI environment
        options.add_argument("--no-sandbox")             #To Bypass OS security model
        options.add_argument("--disable-dev-shm-usage")  #
        
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


#Base_url - fixture for test URLs
@pytest.fixture(scope="session")
def base_url():
    return "https://demowebshop.tricentis.com/"


#Logged-in user fixture for authentication tests (required for cart and checkout tests)
@pytest.fixture(scope="function")
def logged_in_user(driver, base_url):
    driver.get(base_url + "login")
    driver.find_element("id", "Email").send_keys("testuser@example.com")
    driver.find_element("id", "Password").send_keys("Password123!")
    driver.find_element("xpath", "//input[@value='Log in']").click()
    yield driver
