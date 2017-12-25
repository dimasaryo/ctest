from selenium.common.exceptions import WebDriverException
from ctest.functional_test.config import TestConfig
from ctest.functional_test.webdriver_wrapper import WebdriverWrapper


class BasePage(object):
    """
    BasePage
    """

    def __init__(self, driver, identifier):
        self.driver = driver
        self.identifier = identifier
        self.wait_for_page_load()

    def wait_for_page_load(self):
        """
        Wait until the page identifier become visible.
        
        :return: PASSED or WebdriverException raised.
        """
        try:
            self.identifier.wait_for_visible(timeout=TestConfig['page_load_timeout'])
        except WebDriverException as e:
            raise WebDriverException("Failed load page. Error: {0}".format(e.__str__()))

    def click_back_button(self):
        """
        Click back button.
        
        :return: PASSED or WebdriverException raised.
        """
        return WebdriverWrapper.click_back_button(self.driver)
