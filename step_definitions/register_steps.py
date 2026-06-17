#Import needed
from pytest_bdd import scenarios, given, when, then
from pytest_bdd import parsers

from pages.register_page import RegisterPage
import os
import pytest
from faker import Faker




#Declaring LoginPage Fixture here because we only need it in this file
#Not used in test_[file].py because every automated test case need to be isolated whith it's own context from beginning to end
@pytest.fixture
def register_page(driver):
    return RegisterPage(driver)


# We create an instance of Faker, which is going to generate new datas for every text execution (to avoid conflicts of test dependance)
fake = Faker()

#Global variables
valid_password = 'Jeoute123!'  # Valid password 
invalid_email = "invalid@"  # invalid EMAIL generated - no domain
invalid_password = 'azert'  # invalid PASSWORD

#scenarios() function reads all scenarios of [login.feature] file
scenarios("../features/register.feature")




# Steps of SCENARIO__01 -> Successful registration with valid e-mail and valid password
@given("User is on the registration page")
def navigate_to_register(register_page, base_url):
    register_page.navigate_to_register_page(base_url)
    
@when("User enters firstname")
def user_enters_firstname(register_page):
    random_firstname = fake.first_name()        # fake FIRSTNAME generated for each execution
    register_page.enter_firstname(random_firstname)
    
@when("User enters lastname")
def user_enters_lastname(register_page):
    random_lastname = fake.last_name()          # fake LASTNAME generated for each execution
    register_page.enter_lastname(random_lastname)
    
@when("User enters valid e-mail")
def user_enters_valid_email(register_page):
    random_email = fake.email()                 # fake EMAIL generated for each execution
    register_page.enter_email(random_email)
    
@when("User enters valid password")
def user_enters_valid_password(register_page):
    register_page.enter_password(valid_password)   # Using global variable (valid_password)

@when("User enters valid confirm password")
def user_enters_valid_confirm_password(register_page):
    register_page.enter_confirm_password(valid_password)    # Using global variable (valid_password)

@when("User clicks the register button")
def user_clicks_register_button(register_page):
    register_page.click_register_button()
    
@then("User should be successfully registered")
def user_registered_successfully(register_page):
    assert register_page.is_registration_successful()
    
@then("User should be redirected to home page")
def user_redirected_homepage(register_page):
    # Safer assertion even if the link changes than the entire url - checks if "registerresult" is present in the url
    assert "registerresult" in register_page.get_current_url()
    



# Steps of SCENARIO__02 -> Failed registration with invalid e-mail format
@when("User enters invalid e-mail format")
def user_enters_invalid_email_format(register_page):
    register_page.enter_email(invalid_email)

@then("User should see an error message")
def user_should_see_error_message_invalid_mail(register_page):
    assert register_page.get_error_message()

    


# Steps of SCENARIO__03 -> Registration with different password lengths
@when(parsers.parse("User enters password of {length} characters"))     #parsers.parse() method to fetch datas of scenario 03
def user_enters_password_with_length(register_page, length):
    password = "j" * int(length)            #"j" multiplied by fetched number of length() function
    register_page.enter_password(password)

@when(parsers.parse("User enters confirm password of {length} characters"))     #parsers.parse() method to fetch datas of scenario 03
def user_enters_confirm_password_with_length(register_page, length):
    password = "j" * int(length)            #"j" multiplied by fetched number of length() function
    register_page.enter_confirm_password(password)

@then(parsers.parse("{result} of different length password"))
def result(register_page, result):
    if result == "User should see an error message":
        assert register_page.get_error_message()
    elif result == "User should be successfully registered":
        assert register_page.is_registration_successful()
    else:
        raise LookupError("no data from outline scenario")
        



# Steps of SCENARIO__04 -> Registration with existing e-mail
@when("User enters existing e-mail")
def user_enters_existing_email(register_page):
    existing_email = os.getenv("REGISTERED_EMAIL")    
    register_page.enter_email(existing_email)

@then("User should see an error message for existing e-mail")
def user_should_see_error_message_existing_mail(register_page):
    assert register_page.get_error_message_already_registered_email()




# Steps of SCENARIO__05 -> Failed registration with invalid credentials and verify if error message is displayed
@when("User enters invalid password")
def user_enters_invalid_password(register_page):
    register_page.enter_password(invalid_password)
    
@when("User enters invalid confirm password")
def user_enters_confirm_invalid_password(register_page):
    register_page.enter_confirm_password(invalid_password)

