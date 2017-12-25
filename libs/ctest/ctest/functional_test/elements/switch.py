from appium.webdriver.common.mobileby import MobileBy
from ctest.functional_test.config import TestConfig
from ctest.functional_test.elements.button import Button
from ctest.functional_test.util import construct_locator


class Switch(Button):

    def __init__(self, driver, value):
        locator = construct_locator((MobileBy.XPATH, "//android.widget.Switch[contains(@text, '{0}')]"), value)
        super(Switch, self).__init__(driver, locator)

    def is_on(self, timeout=TestConfig['element_load_timeout']):
        """
        Switch status.
        
        :param timeout: Wait timeout.
        :return: True or False.
        """
        status = self.get_text(timeout)
        if 'ON' in status:
            return True

        return False
