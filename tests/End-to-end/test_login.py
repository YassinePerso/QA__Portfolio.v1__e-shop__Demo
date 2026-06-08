import pytest
from pages.login_page import LoginPage
import os



@pytest.mark.smoke
def test_TC01_successful_login(driver):
    
    login_page = LoginPage(driver)    # First, we create an instance of the LoginPage by calling it to allow us to use the methods of LoginPage class

    email = os.getenv("REGISTERED_EMAIL")    # We fetch the username and password from environment variables, which are set in the .env file by using the os.getenv() function
    password = os.getenv("REGISTERED_PASSWORD")
    
    login_page.login(email, password)    # Then we launch the actions with login() function that includes every action needed to perform a sucessfull login

    # We put an assertion at the end of the test case to check if the login was successful by using the is_login_successful() method of LoginPage class
    # is_login_successful() method checks if the logout link is visible, which indicates that login was successful (returns true if visible, false if not visible)
    assert login_page.is_login_successful()
    
    
    
    
@pytest.mark.regression
def test_TC02_failed_login_invalid_email(driver):
    
    login_page = LoginPage(driver)
    fake_email = "invalid-email"
    password = os.getenv("REGISTERED_PASSWORD")
    login_page.login(fake_email, password)
    assert login_page.get_error_message()
    
    
    
    
@pytest.mark.regression
def test_TC03_failed_login_invalid_password(driver):
    
    login_page = LoginPage(driver)
    email = os.getenv("REGISTERED_EMAIL")
    fake_password = "jefebdjfioeubfjbef"
    login_page.login(email, fake_password)
    assert login_page.get_error_message()
    



@pytest.mark.smoke
def test_TC04_redirect_homepage_after_successful_login(driver):
    
    login_page = LoginPage(driver)
    email = os.getenv("REGISTERED_EMAIL")
    password = os.getenv("REGISTERED_PASSWORD")
    login_page.login(email, password)
    
    assert login_page.get_current_url() == "https://demowebshop.tricentis.com/"
    
    
    
    
@pytest.mark.regression
def test_TC05_failed_empty_fields_login(driver):    
    
    login_page = LoginPage(driver)
    empty_email = ""
    empty_password = ""
    login_page.login(empty_email, empty_password)
    
    assert login_page.get_error_message()