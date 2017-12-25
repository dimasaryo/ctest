from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, \
    WebDriverException, NoSuchElementException

from ctest.functional_test.constants import PASSED, Platform
from ctest.functional_test.config import TestConfig


class WebdriverWrapper(object):
    """
    Abstraction layer for webdriver
    """

    def __init__(self):
        pass

    @staticmethod
    def find_present_element(driver, locator, timeout=TestConfig['element_load_timeout'], pool_frequency=5,
                             throw_exception=True):
        """
        Find present element.
        
        :param driver: Webdriver.
        :param locator: Targeted locator.
        :param timeout: Wait timeout.
        :param pool_frequency: Pool frequency.
        :param throw_exception: Throw exception if failed. Default is True.
        :return: Webdriver element or None
        """
        try:
            return WebDriverWait(driver,
                                 timeout,
                                 pool_frequency,
                                 [NoSuchElementException]).until(
                EC.presence_of_element_located(locator)
            )
        except WebDriverWait:
            if throw_exception:
                raise WebDriverException('Could not found present element {0} - {1}'.format(locator[0], locator[1]))

    @staticmethod
    def find_visible_element(driver, locator, timeout=TestConfig['element_load_timeout'], pool_frequency=5,
                             throw_exception=True, max_swipe=3):
        """
        Find visible element.
        
        :param driver: Webdriver.
        :param locator: Targeted locator.
        :param timeout: Wait timeout.
        :param pool_frequency: Pool frequency.
        :param throw_exception: Throw exception if failed. Default is True.
        :param max_swipe: Maximum swipe until the element found (Android & iOS native only)
        :return: Webdriver element or None
        """
        try:
            if TestConfig['platform'] == Platform['android']:
                return WebdriverWrapper.find_visible_android_element(driver, locator, timeout, max_swipe)

            return WebDriverWait(driver,
                                 timeout,
                                 pool_frequency,
                                 [ElementNotVisibleException, NoSuchElementException]).until(
                EC.visibility_of_element_located(locator)
            )
        except WebDriverException:
            if throw_exception:
                raise WebDriverException('Could not found visible element {0} - {1}'.format(locator[0], locator[1]))

    @staticmethod
    def find_clickable_element(driver, locator, timeout=TestConfig['element_load_timeout'], pool_frequency=5,
                               throw_exception=True, max_swipe=3):
        """
        Find clickable element.
        
        :param driver: Webdriver.
        :param locator: Targeted locator.
        :param timeout: Wait timeout.
        :param pool_frequency: Pool frequency.
        :param throw_exception: Throw exception if failed. Default is True.
        :param max_swipe: Maximum swipe until the element found (Android & iOS native only)
        :return: Webdriver element or None 
        """
        try:
            if TestConfig['platform'] == Platform['android']:
                WebdriverWrapper.find_visible_android_element(driver, locator, timeout, max_swipe)
            return WebDriverWait(driver,
                                 timeout,
                                 pool_frequency,
                                 [NoSuchElementException, ElementNotVisibleException]).until(
                EC.element_to_be_clickable(locator))
        except WebDriverWait:
            if throw_exception:
                raise WebDriverException('Could not found clickable element {0} - {1}'.format(locator[0], locator[1]))

    @staticmethod
    def find_visible_native_element(driver, locator, timeout):
        """
        Find visible native element (Android & iOS native only)
        
        :param driver: Webdriver.
        :param locator: Targeted locator.
        :param timeout: Wait timeout. 
        :return: Webdriver element or None
        """
        try:
            element = WebdriverWrapper.find_present_element(driver, locator, timeout)
            if element is not None and element.is_displayed():
                return element
            return None
        except WebDriverException:
            return None

    @staticmethod
    def swipe_down_android(driver, steps=1):
        """
        Swipe down (Android only)
        
        :param driver: Webdriver.
        :param steps: Number of swipes.
        :return: 
        """
        size = driver.get_window_size()
        start_y = size["height"] * 0.80
        end_y = size["height"] * 0.20
        start_x = size["width"] / 2
        for i in range(0, steps):
            driver.swipe(start_x, start_y, start_x, end_y, 3000)
        return PASSED

    @staticmethod
    def swipe_up_android(driver, steps=1):
        """
        Swipe up (Android only)
        
        :param driver: Webdriver.
        :param steps: Number of swipes.
        :return: 
        """
        size = driver.get_window_size()
        start_y = size["height"] * 0.80
        end_y = size["height"] * 0.20
        start_x = size["width"] / 2
        for i in range(0, steps):
            driver.swipe(start_x, end_y, start_x, start_y, 3000)
        return PASSED

    @staticmethod
    def find_visible_android_element(driver, locator, timeout, max_swipe=3):
        """
        Find visible element (Android only)
        
        :param driver: Webdriver.
        :param locator: Targeted element.
        :param timeout: Wait timeout.
        :param max_swipe: Maximum number of swipe.
        :return: Webdriver element or None.
        """
        element = WebdriverWrapper.find_visible_native_element(driver, locator, timeout)
        if element is not None:
            return element

        for i in range(1, max_swipe + 1):
            WebdriverWrapper.swipe_down_android(driver, i)
            element = WebdriverWrapper.find_visible_native_element(driver, locator, 1)
            if element is not None:
                return element

        WebdriverWrapper.swipe_up_android(driver, max_swipe)

        for i in range(1, max_swipe + 1):
            WebdriverWrapper.swipe_up_android(driver, i)
            element = WebdriverWrapper.find_visible_native_element(driver, locator, 1)
            if element is not None:
                return element

        WebdriverWrapper.swipe_down_android(driver, max_swipe)
        raise WebDriverException('Could not find visible element {0} - {1}'.format(locator[0], locator[1]))

    @staticmethod
    def click_back_button(driver):
        """
        Click back button of the phone
        
        :param driver: Webdriver.
        :return: PASSED
        """
        driver.back()
        return PASSED

    @staticmethod
    def get_text(driver, locator, timeout=TestConfig['element_load_timeout']):
        """
        Get text
        
        :param driver: Webdriver.
        :param locator: Targeted element.
        :param timeout: Wait timeout.
        :return: Text.
        """
        element = WebdriverWrapper.find_visible_element(driver, locator, timeout)
        return element.get_attribute('text')

    @staticmethod
    def hide_keyboard(driver):
        """
        Hide keyboard.
        
        :param driver: Webdriver.
        :return: None
        """
        try:
            driver.hide_keyboard()
        except WebDriverException:
            pass
