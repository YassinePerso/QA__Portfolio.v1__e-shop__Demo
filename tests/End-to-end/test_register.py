import pytest
from pages.register_page import RegisterPage
import os
from faker import Faker


#We create an instance of Faker, which is going to generate new datas for every text execution (to avoid conflicts of test dependance)
fake = Faker()




@pytest.mark.smoke
def test_TC01_successful_registration (driver):
    
    register_page = RegisterPage(driver)
    
    random_firstname = fake.person.first_name() #fake FIRSTNAME generated for each execution
    random_lastname = fake.person.last_name()   #fake LASTNAME generated for each execution
    random_email = fake.internet.email()        #fake EMAIL generated for each execution
    password = 'Jeoute123!'                     #Valid password
    short_password = "iu"                       #Invalid password