from ctest.functional_test.webdriver_wrapper import WebdriverWrapper
from ctest.functional_test.config import TestConfig


class BaseElement(object):

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    def wait_for_visible(self, timeout=TestConfig['element_load_timeout']):
        """
        Wait for element until visible.
        
        :param timeout: Wait timeout.
        :return: Webdriver element or WebdriverException raised.
        """
        return WebdriverWrapper.find_visible_element(self.driver, self.locator, timeout)

    def wait_for_present(self, timeout=TestConfig['element_load_timeout']):
        """
        Wait for element until presented.
        
        :param timeout: Wait timeout.
        :return: Webdriver element or WebdriverException raised.
        """
        return WebdriverWrapper.find_visible_element(self.driver, self.locator, timeout)

    def get_text(self, timeout=TestConfig['element_load_timeout']):
        """
        Get text from an element.
        
        :param timeout: Wait timeout.
        :return: Webdriver element or WebdriverException raised.
        """
        return WebdriverWrapper.get_text(self.driver, self.locator, timeout)
