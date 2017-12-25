from appium.webdriver.common.mobileby import MobileBy
from ctest.functional_test.base_locator import BaseLocator


class AlertPageElement(BaseLocator):

    OK_BUTTON = (MobileBy.XPATH, "//android.widget.Button[@text='OK']")
