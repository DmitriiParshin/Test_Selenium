from selenium.webdriver import Keys
from pages.base_page import BasePage
from pages.locators import SearchPageLocators


class SearchPage(BasePage):
    def check_if_search_field_exists(self):
        assert self.is_element_present(*SearchPageLocators.SEARCH_FIELD), "No search field"

    def search_for_tensor(self):
        self.browser.find_element(*SearchPageLocators.SEARCH_FIELD).send_keys('Тензор')

    def should_be_table_with_hints(self):
        assert self.is_element_present(*SearchPageLocators.SUGGEST), "No suggest"

    def should_appear_search_results_table(self):
        self.browser.find_element(*SearchPageLocators.SEARCH_FIELD).send_keys(Keys.ENTER)
        assert self.is_element_present(*SearchPageLocators.RESULTS_TABLE), "No search results table"

    def first_five_results_have_link(self):
        links_list = self.browser.find_elements(*SearchPageLocators.LINK_TENZOR)
        items = [link.text.strip() for link in links_list[:5]]
        assert "tensor.ru" in items, "In the first five results there is no link to tensor.ru"
