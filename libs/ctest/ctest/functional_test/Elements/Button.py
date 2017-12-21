from ctest.functional_test.Elements.BaseElement import BaseElement
from ctest.functional_test.webdriver_wrapper import WebdriverWrapper

from ctest.functional_test.constants import PASSED


class Button(BaseElement):

    def __init__(self, driver, locator):
        super(Button, self).__init__(driver, locator)

    def click(self, timeout=10):
        element = WebdriverWrapper.find_clickable_element(self.driver, self.locator, timeout)
        element.click()
        return PASSED
