from ctest.functional_test.constants import PASSED
from ctest.functional_test.config import TestConfig
from ctest.functional_test.elements.base_element import BaseElement
from ctest.functional_test.webdriver_wrapper import WebdriverWrapper


class TextField(BaseElement):

    def __init__(self, driver, locator):
        super(TextField, self).__init__(driver, locator)

    def set_text(self, value, key=None):
        """
        Set text to an element.
        
        :param value: Text.
        :param key: Key.
        :return: PASSED or WebdriverException raised.
        """
        element = self.wait_for_visible(timeout=TestConfig['element_load_timeout'])
        element.set_value(value)
        if key is not None:
            element.send_keys(key)
        WebdriverWrapper.hide_keyboard(self.driver)
        return PASSED
