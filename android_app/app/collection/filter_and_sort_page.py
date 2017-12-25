from ctest.functional_test.base_page import BasePage
from ctest.functional_test.elements.text import Text
from ctest.functional_test.elements.button import Button
from ctest.functional_test.elements.radio_button import RadioButton
from android_app.app.collection.filter_and_sort_page_element import FilterAndSortPageElement
from android_app.constants import SortBy


class FilterAndSortPage(BasePage):

    def __init__(self, driver):
        self.title = Text(driver, FilterAndSortPageElement.TITLE)
        self.sort_by_option = {
            SortBy.popular: RadioButton(driver, SortBy.popular),
            SortBy.recent: RadioButton(driver, SortBy.recent)
        }
        self.apply_button = Button(driver, FilterAndSortPageElement.APPLY_BUTTON)
        super(FilterAndSortPage, self).__init__(driver, self.title)

    def choose_sorting_method(self, value=None):
        """
        Choose sorting method.
        
        :param value: sorting method.
        :return: PASSED or WebdriverException raised.
        """
        option = self.sort_by_option[value]
        return option.click()

    def apply(self):
        """
        Apply sort and filter.
        
        :return: PASSED or WebdriverException raised.
        """
        return self.apply_button.click()
