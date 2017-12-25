from appium.webdriver.common.mobileby import MobileBy
from ctest.functional_test.base_locator import BaseLocator


class FilterAndSortPageElement(BaseLocator):
    TITLE = (MobileBy.XPATH, "//android.widget.TextView[@text='SORT BY']")
    APPLY_BUTTON = (MobileBy.XPATH, "//android.widget.Button[@text='See filtered results']")
