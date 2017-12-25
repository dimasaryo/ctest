from ctest.functional_test.base_page import BasePage
from ctest.functional_test.elements.text_field import TextField
from ctest.functional_test.elements.button import Button
from ctest.functional_test.util import construct_locator
from android_app.app.sell.category_page_element import CategoryPageElement


class CategoryPage(BasePage):

    def __init__(self, driver):
        self.search_field = TextField(driver, CategoryPageElement.SEARCH_FIELD)
        super(CategoryPage, self).__init__(driver, self.search_field)

    def search(self, category):
        """
        Search category
        
        :param category: Category.
        :return: PASSED or WebdriverException raised.
        """
        return self.search_field.set_text(category)

    def choose_category(self, category, sub_category):
        """
        Choose category.
        
        :param category: Category.
        :param sub_category: Sub Category.
        :return: PASSED or WebdriverException raised.
        """
        category_element = construct_locator(CategoryPageElement.CATEGORY, category)
        category = Button(self.driver, category_element)
        category.click()
        sub_category_element = construct_locator(CategoryPageElement.CATEGORY, sub_category)
        sub_category = Button(self.driver, sub_category_element)
        return sub_category.click()
