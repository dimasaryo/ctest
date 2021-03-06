from selenium.common.exceptions import WebDriverException

from ctest.functional_test.base_page import BasePage
from ctest.functional_test.elements.button import Button
from android_app.app.collection.category_collection_page_element import CategoryCollectionPageElement
from ctest.functional_test.elements.text import Text
from ctest.functional_test.constants import PASSED
from ctest.functional_test.util import construct_locator, format_currency


class CategoryCollectionPage(BasePage):

    def __init__(self, driver):
        self.filter_button = Button(driver, CategoryCollectionPageElement.FILTER_BUTTON)
        self.ok_got_it_button = Button(driver, CategoryCollectionPageElement.OK_GOT_IT_BUTTON)
        self.dismiss_guide()
        super(CategoryCollectionPage, self).__init__(driver, self.filter_button)

    def dismiss_guide(self):
        """
        Dismiss guide pop up.
        
        :return: PASSED or WebdriverException raised.
        """
        try:
            self.ok_got_it_button.click(timeout=1, max_swipe=0)
        except WebDriverException:
            pass

    def change_filter(self):
        """
        Open filter page.
        
        :return: PASSED or WebdriverException raised.
        """
        return self.filter_button.click()

    def listing_is_exists(self, username, title, price, description=None, item_condition=None):
        """
        Verify listing is exists.
        
        :param username: Username.
        :param title: Title.
        :param price: Price.
        :param description: Description.
        :param item_condition: New or Used.
        :return: PASSED or WebdriverException raised.
        """
        self.verify_listing_detail(username, title)
        self.verify_listing_detail(username, format_currency(price))
        if description is not None:
            self.verify_listing_detail(username, description)
        if item_condition is not None:
            self.verify_listing_detail(username, item_condition)
        return PASSED

    def verify_listing_detail(self, username, expected):
        """
        Verify listing detail.
        
        :param username: Username.
        :param expected: Expected.
        :return: PASSED or WebdriverException raised.
        """
        item_detail_locator = construct_locator(CategoryCollectionPageElement.ITEM_DETAIL, username, expected)
        item_detail = Text(self.driver, item_detail_locator)
        item_detail.wait_for_visible()
        return PASSED
