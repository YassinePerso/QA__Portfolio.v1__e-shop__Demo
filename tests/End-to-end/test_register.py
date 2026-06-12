import pytest
from pages.register_page import RegisterPage
import os
from faker import Faker




#We create an instance of Faker, which is going to generate new datas for every text execution (to avoid conflicts of test dependance)
fake = Faker()




#TC_01
@pytest.mark.smoke
def test_TC01_successful_registration (driver, base_url):
    
    random_firstname = fake.first_name() #fake FIRSTNAME generated for each execution
    random_lastname = fake.last_name()   #fake LASTNAME generated for each execution
    random_email = fake.email()          #fake EMAIL generated for each execution
    password = 'Jeoute123!'              #Valid password
    
    register_page = RegisterPage(driver)
    register_page.navigate_to_register_page(base_url)
    #Using register() function that combines all actions to perform successful registration
    register_page.register(random_firstname, random_lastname, random_email, password, password)
    assert register_page.is_registration_successful()
    
    
    
    
#TC_02
@pytest.mark.regression
def test_TC02_failed_registration_invalid_email (driver, base_url):
    
    random_firstname = fake.first_name() #fake FIRSTNAME generated for each execution
    random_lastname = fake.last_name()   #fake LASTNAME generated for each execution
    invalid_email = "invalid-email"      #invalid EMAIL generated - no @
    password = 'Jeoute123!'              #Valid password
    
    register_page = RegisterPage(driver)
    register_page.navigate_to_register_page(base_url)
    #Using register() function that combines all actions to perform successful registration
    register_page.register(random_firstname, random_lastname, invalid_email, password, password)
    assert register_page.get_error_message()
    
    
    
    
#TC_03
@pytest.mark.regression
def test_TC03_failed_registration_invalid_email_no_domain (driver, base_url):
    
    random_firstname = fake.first_name() #fake FIRSTNAME generated for each execution
    random_lastname = fake.last_name()   #fake LASTNAME generated for each execution
    invalid_email = "invalid@"           #invalid EMAIL generated - no domain
    password = 'Jeoute123!'              #Valid password
    
    register_page = RegisterPage(driver)
    register_page.navigate_to_register_page(base_url)
    #Using register() function that combines all actions to perform successful registration
    register_page.register(random_firstname, random_lastname, invalid_email, password, password)
    assert register_page.get_error_message()
    
    
    
    
#TC_04
@pytest.mark.smoke
def test_TC04_successful_registration_6_char_password (driver, base_url):
    
    random_firstname = fake.first_name() #fake FIRSTNAME generated for each execution
    random_lastname = fake.last_name()   #fake LASTNAME generated for each execution
    random_email = fake.email()          #fake EMAIL generated for each execution
    password = 'azerty'                  #6 characters password - VALID (BVA)
    
    register_page = RegisterPage(driver)
    register_page.navigate_to_register_page(base_url)
    #Using register() function that combines all actions to perform successful registration
    register_page.register(random_firstname, random_lastname, random_email, password, password)
    assert register_page.is_registration_successful()
    
    
    
    
#TC_05
@pytest.mark.regression
def test_TC05_failed_registration_5_char_password (driver, base_url):
    
    random_firstname = fake.first_name() #fake FIRSTNAME generated for each execution
    random_lastname = fake.last_name()   #fake LASTNAME generated for each execution
    random_email = fake.email()          #fake EMAIL generated for each execution
    password = 'azert'                   #5 characters password - INVALID (BVA)
    
    register_page = RegisterPage(driver)
    register_page.navigate_to_register_page(base_url)
    #Using register() function that combines all actions to perform successful registration
    register_page.register(random_firstname, random_lastname, random_email, password, password)
    assert register_page.get_error_message()
    
    
    
    
#TC_06
@pytest.mark.regression
def test_TC06_successful_registration_7_char_password (driver, base_url):
    
    random_firstname = fake.first_name() #fake FIRSTNAME generated for each execution
    random_lastname = fake.last_name()   #fake LASTNAME generated for each execution
    random_email = fake.email()          #fake EMAIL generated for each execution
    password = 'azertyl'                 #7 characters password - VALID (BVA)
    
    register_page = RegisterPage(driver)
    register_page.navigate_to_register_page(base_url)
    #Using register() function that combines all actions to perform successful registration
    register_page.register(random_firstname, random_lastname, random_email, password, password)
    assert register_page.is_registration_successful()
    
   
    
    
#TC_07
@pytest.mark.regression
def test_TC07_failed_registration_with_registered_email (driver, base_url):
    
    random_firstname = fake.first_name() #fake FIRSTNAME generated for each execution
    random_lastname = fake.last_name()   #fake LASTNAME generated for each execution
    registered_email = os.getenv('REGISTERED_EMAIL') 
    password = 'Jeoute123!'              #Valid password
    
    register_page = RegisterPage(driver)
    register_page.navigate_to_register_page(base_url)
    #Using register() function that combines all actions to perform successful registration
    register_page.register(random_firstname, random_lastname, registered_email, password, password)
    assert register_page.get_error_message_already_registered_email()
    
    
    
    
#TC_08
@pytest.mark.smoke
def test_TC08_successful_registration_redirect_homepage (driver, base_url):
    
    random_firstname = fake.first_name() #fake FIRSTNAME generated for each execution
    random_lastname = fake.last_name()   #fake LASTNAME generated for each execution
    random_email = fake.email()          #fake EMAIL generated for each execution
    password = 'Jeoute123!'              #Valid password
    
    register_page = RegisterPage(driver)
    register_page.navigate_to_register_page(base_url)
    #Using register() function that combines all actions to perform successful registration
    register_page.register(random_firstname, random_lastname, random_email, password, password)
    assert register_page.is_registration_successful()
    assert "registerresult" in register_page.get_current_url()  #Safer assertion even if the link changes than the entire url - checks if "registerresult" is present in the url
    
    
    
    
#TC_09   
@pytest.mark.regression
def test_TC09_failed_registration_invalid_credentials (driver, base_url):
    
    random_firstname = fake.first_name() #fake FIRSTNAME generated for each execution
    random_lastname = fake.last_name()   #fake LASTNAME generated for each execution
    invalid_email = "invalid-email"      #invalid EMAIL
    password = 'azert'                   #invalid PASSWORD
    
    register_page = RegisterPage(driver)
    register_page.navigate_to_register_page(base_url)
    #Using register() function that combines all actions to perform successful registration
    register_page.register(random_firstname, random_lastname, invalid_email, password, password)
    assert register_page.get_error_message()