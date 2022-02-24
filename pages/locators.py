from selenium.webdriver.common.by import By


class SearchPageLocators:
    SEARCH_FIELD = (By.CSS_SELECTOR, "#text")
    SUGGEST = (By.CSS_SELECTOR, "div.mini-suggest__popup.mini-suggest__popup_svg_yes.mini-suggest__popup_theme_tile")
    RESULTS_TABLE = (By.CSS_SELECTOR, "#search-result")
    LINK_TENZOR = (By.CSS_SELECTOR, "a.Link.Link_theme_outer.Path-Item > b")


class ImagesPageLocators:
    IMAGE_LINK = (By.CSS_SELECTOR, "div.services-new__icon.services-new__icon_images")
    FIRST_CATEGORY = (By.CSS_SELECTOR, "div.PopularRequestList-Item.PopularRequestList-Item_pos_0")
    NAME_CATEGORY = (By.CSS_SELECTOR,
                     "div.PopularRequestList-Item.PopularRequestList-Item_pos_0 > a div.PopularRequestList-SearchText")
    WORD_SEARCH = (By.CSS_SELECTOR, "input.input__control.mini-suggest__input")
    FIRST_IMAGE = (By.CSS_SELECTOR, "div.serp-item.serp-item_type_search.serp-item_group_search.serp-item_pos_0")
    BUTTON_FORWARD = (By.CSS_SELECTOR, "div.MediaViewer-ButtonNext.MediaViewer_theme_fiji-ButtonNext "
                                       "i.CircleButton-Icon")
    BUTTON_BACK = (By.CSS_SELECTOR, "div.MediaViewer-ButtonPrev.MediaViewer_theme_fiji-ButtonPrev i.CircleButton-Icon")
    OPEN_IMAGE = (By.CSS_SELECTOR, ".MMImage-Origin")
