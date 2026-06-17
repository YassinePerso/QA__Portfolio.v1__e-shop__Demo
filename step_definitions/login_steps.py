#Import needed
from pytest_bdd import scenarios, given, when, then
from pages.login_page import LoginPage
import os
import pytest




#Declaring LoginPage Fixture here because we only need it in this file
#Not used in test_[file].py because every automated test case need to be isolated whith it's own context from beginning to end
@pytest.fixture
def login_page(driver):
    return LoginPage(driver)



#scenarios() function reads all scenarios of [login.feature] file
scenarios("../features/login.feature")



# Steps of SCENARIO__01 -> Successful login with VALID credentials
@given("User is on the login page")
def navigate_to_login(login_page, base_url):
    login_page.navigate_to_login_page(base_url)
    
@when("User enters valid e-mail and password")
def enter_valid_email_and_password(login_page):
    email = os.getenv("REGISTERED_EMAIL")
    password = os.getenv("REGISTERED_PASSWORD")
    login_page.enter_email(email)
    login_page.enter_password(password)
    
@when("User clicks the login button")
def user_clicks_login_button(login_page):
    login_page.click_login_button()
    
@then("User should be logged in successfully")
def user_logged_in_successfully(login_page):
    assert login_page.is_login_successful()
    
@then("User should be redirected to home page")
def user_redirected_homepage(login_page):
    url = "https://demowebshop.tricentis.com/"
    assert login_page.get_current_url() == url
    
    
    
    
# Steps of SCENARIO__02 -> Failed login with INVALID e-mail
@when("User enters invalid e-mail and valid password")
def enter_invalid_email_and_valid_password(login_page):
    fake_email = "invalid-email"
    password = os.getenv("REGISTERED_PASSWORD")
    login_page.enter_email(fake_email)
    login_page.enter_password(password)

@then("User should see an error message for invalid e-mail")
def user_should_see_error_message_invalid_mail(login_page):
    assert login_page.get_error_message_invalid_mail()




# Steps of SCENARIO__03 -> Failed login with INVALID password
@when("User enters valid e-mail and invalid password")
def enter_valid_email_and_invalid_password(login_page):
    email = os.getenv("REGISTERED_EMAIL")
    fake_password = "jefebdjfioeubfjbef"
    login_page.enter_email(email)
    login_page.enter_password(fake_password)
    
@then("User should see an error message")
def user_should_see_error_message(login_page):
    assert login_page.get_error_message()




# Steps of SCENARIO__04 -> Failed login with empty e-mail and password fields
@when("User leaves e-mail and password fields empty")
def empty_fields_failed_login(login_page):    
    empty_email = ""
    empty_password = ""
    login_page.enter_email(empty_email)
    login_page.enter_password(empty_password)


#   #TC_004
#   @regression @login
#         And User clicks the login button
#         Then User should see an error message