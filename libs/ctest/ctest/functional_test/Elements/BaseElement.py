from ctest.functional_test.webdriver_wrapper import WebdriverWrapper


class BaseElement(object):

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    def wait_for_visible(self, timeout=10):
        return WebdriverWrapper.find_visible_element(self.driver, self.locator, timeout)

    def wait_for_present(self, timeout=10):
        return WebdriverWrapper.find_visible_element(self.driver, self.locator, timeout)
