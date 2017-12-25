from selenium.common.exceptions import WebDriverException
from ctest.functional_test.base_page import BasePage
from ctest.functional_test.elements.button import Button

from android_app.app.collection.header_page import HeaderPage
from android_app.app.collection.collection_page_element import CollectionPageElement


class CollectionPage(BasePage):

    def __init__(self, driver):
        self.header = HeaderPage(driver)
        self.sell_button = Button(driver, CollectionPageElement.SELL_BUTTON)
        self.everything_else_category = Button(driver, CollectionPageElement.EVERYTHING_ELSE_CATEGORY)
        super(CollectionPage, self).__init__(driver, self.sell_button)

    def open_sell_form(self):
        return self.sell_button.click()

    def open_everything_else_category(self):
        return self.everything_else_category.click()

