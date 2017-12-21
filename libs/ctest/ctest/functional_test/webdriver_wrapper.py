from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, \
    WebDriverException, NoSuchElementException

from constants import PASSED


class WebdriverWrapper():

    def __init__(self):
        pass

    @staticmethod
    def find_present_element(driver, locator, timeout=10, pool_frequency=5, throw_exception=True):
        try:
            return WebDriverWait(driver,
                                 timeout,
                                 pool_frequency,
                                 [NoSuchElementException]).until(
                EC.presence_of_element_located(locator)
            )
        except WebDriverWait:
            if throw_exception:
                raise Exception('Could not found present element {0} - {1}'.format(locator[0], locator[1]))

    @staticmethod
    def find_visible_element(driver, locator, timeout=10, pool_frequency=5, throw_exception=True):
        try:
            return WebDriverWait(driver,
                                 timeout,
                                 pool_frequency,
                                 [ElementNotVisibleException, NoSuchElementException]).until(
                EC.visibility_of_element_located(locator)
            )
        except WebDriverException:
            if throw_exception:
                raise Exception('Could not found visible element {0} - {1}'.format(locator[0], locator[1]))

    @staticmethod
    def find_present_element(driver, locator, timeout=10, pool_frequency=5, throw_exception=True):
        try:
            return WebDriverWait(driver,
                                 timeout,
                                 pool_frequency,
                                 [NoSuchElementException]).until(
                EC.presence_of_element_located(locator)
            )
        except WebDriverWait:
            if throw_exception:
                raise Exception('Could not found present element {0} - {1}'.format(locator[0], locator[1]))

    @staticmethod
    def find_clickable_element(driver, locator, timeout=10, pool_frequency=5, throw_exception=True):
        try:
            return WebDriverWait(driver,
                                 timeout,
                                 pool_frequency,
                                 [NoSuchElementException, ElementNotVisibleException]).until(
                EC.presence_of_element_located(locator))
        except WebDriverWait:
            if throw_exception:
                raise Exception('Could not found clickable element {0} - {1}'.format(locator[0], locator[1]))

    @staticmethod
    def find_visible_native_element(driver, locator, timeout):
        try:
            element = WebdriverWrapper.find_present_element(driver, locator, timeout)
            if element is not None and element.is_displayed():
                return element
            return None
        except WebDriverException:
            return None

    @staticmethod
    def swipe_down_android(driver, steps=1):
        size = driver.get_window_size()
        start_y = size["height"] * 0.80
        end_y = size["height"] * 0.20
        start_x = size["width"] / 2
        for i in range(0, steps):
            driver.swipe(start_x, start_y, start_x, end_y, 3000)
        return PASSED

    @staticmethod
    def swipe_up_android(driver, steps=1):
        size = driver.get_window_size()
        start_y = size["height"] * 0.80
        end_y = size["height"] * 0.20
        start_x = size["width"] / 2
        for i in range(0, steps):
            driver.swipe(start_x, end_y, start_x, start_y, 3000)
        return PASSED

    @staticmethod
    def find_visible_android_element(driver, locator, timeout, max_swipe=3):
        element = WebdriverWrapper.find_visible_native_element(driver, locator, timeout)
        if element is not None:
            return element

        for i in range(1, max_swipe + 1):
            WebdriverWrapper.swipe_down_android(i)
            element = WebdriverWrapper.find_visible_native_element(driver, locator, timeout)
            if element is not None:
                return element

        WebdriverWrapper.swipe_up_android(max_swipe)

        for i in range(1, max_swipe + 1):
            WebdriverWrapper.swipe_up_android(i)
            element = WebdriverWrapper.find_visible_native_element(driver, locator, timeout)
            if element is not None:
                return element

        WebdriverWrapper.swipe_down_android(max_swipe)
        raise Exception('Could not find visible element {0} - {1}'.format(locator[0], locator[1]))
