from pages.base_page import BasePage
from pages.locators import ImagesPageLocators


class ImagesPage(BasePage):
    def should_be_link_to_images(self):
        assert self.is_element_present(*ImagesPageLocators.IMAGE_LINK), "No link to images"

    def open_to_images(self):
        self.browser.find_element(*ImagesPageLocators.IMAGE_LINK).click()

    def should_be_url_to_images(self):
        self.browser.switch_to.window(self.browser.window_handles[1])
        assert "https://yandex.ru/images" in self.browser.current_url, "Not this URL"

    def open_first_category(self):
        name_category = self.browser.find_element(*ImagesPageLocators.NAME_CATEGORY)
        name = name_category.text
        self.browser.find_element(*ImagesPageLocators.FIRST_CATEGORY).click()
        word_search = self.browser.find_element(*ImagesPageLocators.WORD_SEARCH)
        value = word_search.get_attribute('value')
        assert name == value, "Open not first category"

    def open_and_check_images(self):
        self.browser.find_element(*ImagesPageLocators.FIRST_IMAGE).click()
        assert self.browser.find_element(*ImagesPageLocators.OPEN_IMAGE), "Image not open"
        image_first = self.browser.find_element(*ImagesPageLocators.OPEN_IMAGE)
        first = image_first.get_attribute('src')
        self.browser.find_element(*ImagesPageLocators.BUTTON_FORWARD).click()
        image_second = self.browser.find_element(*ImagesPageLocators.OPEN_IMAGE)
        second = image_second.get_attribute('src')
        assert first != second, "Open same image"
        self.browser.find_element(*ImagesPageLocators.BUTTON_BACK).click()
        image_first_back = self.browser.find_element(*ImagesPageLocators.OPEN_IMAGE)
        first_back = image_first_back.get_attribute('src')
        assert first_back == first, "Images different"
