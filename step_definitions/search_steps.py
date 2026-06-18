# Import needed
from pytest_bdd import scenarios, given, when, then
from pages.home_page import HomePage
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def home_page(driver):
    return HomePage(driver)


scenarios("../features/search.feature")


# Steps of SCENARIO__01 -> Successful search with valid product name
@given("User is on the home page")
def navigate_to_home(home_page, base_url):
    home_page.driver.get(base_url)


@when("User enters valid product name in search bar")
def enter_valid_product_name(home_page):
    home_page.enter_search_query("Fiction")


@when("User clicks the search button")
def click_search_button(home_page):
    home_page.click_search_button()


@then("User should see matching product result(s) displayed")
def verify_matching_results_displayed(home_page):
    assert home_page.is_element_visible((By.CSS_SELECTOR, ".search-results"))


# Steps of SCENARIO__02 -> Search with no matching results
@when("User enters non-existent product name in search bar")
def enter_non_existent_product_name(home_page):
    home_page.enter_search_query("xyznonexistent123")


@then("User should see a message indicating no results found")
def verify_no_results_message(home_page):
    assert home_page.is_no_results_message_visible()


# Steps of SCENARIO__03 -> Search is case-insensitive
@when("User enters valid product name with wrong case in search bar")
def enter_product_name_wrong_case(home_page):
    home_page.enter_search_query("FICTION")


# Steps of SCENARIO__04 -> Search with special characters
@when("User enters product name with special characters in search bar")
def enter_product_name_special_characters(home_page):
    home_page.enter_search_query("Fiction@#$%")


# Steps of SCENARIO__05 -> Search with less than 3 characters
@when("User enters a search term with less than 3 characters in search bar")
def enter_search_term_less_than_3_characters(home_page):
    home_page.enter_search_query("ab")


@then("User should see a minimum length error message")
def verify_minimum_length_error_message(home_page):
    assert home_page.is_search_error_message_visible()
