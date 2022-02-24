from pages.images_page import ImagesPage
from pages.search_page import SearchPage


def test_search_yandex(browser):
    link = "https://yandex.ru/"
    page = SearchPage(browser, link)
    page.open()
    page.check_if_search_field_exists()
    page.search_for_tensor()
    page.should_be_table_with_hints()
    page.should_appear_search_results_table()
    page.first_five_results_have_link()


def test_images_yandex(browser):
    link = "https://yandex.ru/"
    page = ImagesPage(browser, link)
    page.open()
    page.should_be_link_to_images()
    page.open_to_images()
    page.should_be_url_to_images()
    page.open_first_category()
    page.open_and_check_images()
