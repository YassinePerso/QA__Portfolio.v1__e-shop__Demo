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

#Driver - fixture 
@pytest.fixture(scope="function")
def driver(base_url):
    
    options = Options()
    
    #if CI environment variable is set to "true", run in headless mode
    if os.getenv("CI"):
        options.add_argument("--headless")               #To make it run in headless mode for CI environment
        options.add_argument("--no-sandbox")             #To bypass os security model
        options.add_argument("--disable-dev-shm-usage")  #To overcome limited resource problems in CI environments
        
    driver = webdriver.Chrome(options=options)
    driver.get(base_url)
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
    
    email = os.getenv("REGISTERED_EMAIL")       #Fetching email data from environment variables and storing it in a variable
    password = os.getenv("REGISTERED_PASSWORD") #Fetching password data from environment variables and storing it in a variable
    
    if not email or not password:
        raise ValueError("One or more required environment variables not set") #If values are incorrect of missing, raise an error

    driver.find_element(By.ID, "Email").send_keys(email)
    driver.find_element(By.ID, "Password").send_keys(password)
    driver.find_element(By.XPATH, "//input[@value='Log in']").click()
    yield driver