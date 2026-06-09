import pytest
from pages.home_page import HomePage
from selenium.webdriver.common.by import By



#TC_01 - Enter valid product name and verify matching results are displayed
@pytest.mark.smoke
def test_TC01_verify_results_valid_product(driver):
    
    home_page = HomePage(driver)
    home_page.search_for_product("Fiction")
    
    assert home_page.is_element_visible((By.CSS_SELECTOR, ".search-results"))
    
    
    
    
#TC_02 - Enter invalid product name and verify "no results" message is displayed
@pytest.mark.regression
def test_TC02_invalid_product_verify_no_results_message(driver):
    
    home_page = HomePage(driver)
    home_page.search_for_product("Harry potter")
    
    assert home_page.is_no_results_message_visible()
    



#TC_03 - Enter valid product name with WRONG CASE and verify matching results are displayed
@pytest.mark.regression
def test_TC03_valid_product_wrong_case(driver):
    
    home_page = HomePage(driver)
    home_page.search_for_product("fiction")
    
    assert home_page.is_element_visible((By.CSS_SELECTOR, ".search-results"))
    
    
    
    
#TC_04 - Search with special characters
@pytest.mark.regression
def test_TC04_special_characters(driver):
    
    home_page = HomePage(driver)
    home_page.search_for_product("##ù%")
    
    assert home_page.is_no_results_message_visible()
    
    
    
#TC_05 - Search with less than 3 characters
@pytest.mark.regression
def test_TC05_search_less_3_characters(driver):
    
    home_page = HomePage(driver)
    home_page.search_for_product("de")
    
    assert home_page.is_search_error_message_visible()