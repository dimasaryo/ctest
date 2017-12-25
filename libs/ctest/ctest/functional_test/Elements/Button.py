from ctest.functional_test.elements.base_element import BaseElement
from ctest.functional_test.webdriver_wrapper import WebdriverWrapper
from ctest.functional_test.config import TestConfig
from ctest.functional_test.constants import PASSED


class Button(BaseElement):

    def __init__(self, driver, locator):
        super(Button, self).__init__(driver, locator)

    def click(self, timeout=TestConfig['element_load_timeout'], max_swipe=TestConfig['max_swipe']):
        """
        Click of an element.
        
        :param timeout: Wait timeout.
        :param max_swipe: Maximum swipes until the element is clickable.
        :return: PASSED or WebdriverException raised.
        """
        element = WebdriverWrapper.find_clickable_element(self.driver, self.locator, timeout, max_swipe=max_swipe)
        element.click()
        return PASSED
