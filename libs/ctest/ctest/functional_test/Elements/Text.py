from ctest.functional_test.elements.base_element import BaseElement
from ctest.functional_test.config import TestConfig


class Text(BaseElement):

    def __init__(self, driver, locator):
        super(Text, self).__init__(driver, locator)

    def get_text(self):
        """
        Get text of an element.
        :return: Text.
        """
        element = self.wait_for_visible(timeout=TestConfig['element_load_timeout'])
        return element.text
