from pages.base_page import BasePage
from selenium.webdriver.common.by import By



class HomePage (BasePage):
    
    def __init__(self, driver):
        #super() is used to call the __init__ method of the parent class (BasePage) and pass the driver argument to it, so that we can use the driver in the RegisterPage class
        super().__init__(driver)
        self.search_bar_input = (By.ID, "small-searchterms")
        self.search_button = (By.CSS_SELECTOR, "input[value='Search']")
    
    
    #Method to enter search query in the search bar
    def enter_search_query(self, query):
        self.type_text(self.search_bar_input, query)


    #Method to click on the search button
    def click_search_button(self):
        self.click(self.search_button)
    
    
    #method that combines the above two methods to perform a search for a product   
    def search_for_product(self, query):
        self.enter_search_query(query)
        self.click_search_button()
    
    
    #Method to check if the "No products were found that matched your criteria." message is visible, which is displayed when there are no search results for the query
    def is_no_results_message_visible(self):
        no_results_message = (By.CSS_SELECTOR, ".result")  #CSS selector for the "No products were found that matched your criteria."
        return self.is_element_visible(no_results_message)
    
    
    #For negative test case, if query has less than 3 characters, it should not perform search and should show an error message, so we need to check if the error message is visible
    def is_search_error_message_visible(self):
        search_error_message = (By.CSS_SELECTOR, ".warning")  #The error message is displayed in a div with class "warning", so we locate it using CSS selector
        return self.is_element_visible(search_error_message)