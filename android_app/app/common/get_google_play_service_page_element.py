from appium.webdriver.common.mobileby import MobileBy
from ctest.functional_test.base_locator import BaseLocator


class GetGooglePlayServiceElement(BaseLocator):

    TITLE = (MobileBy.XPATH, "//android.widget.TextView[@text='Get Google Play Service']")
    DESCRIPTION = (MobileBy.XPATH, "//android.widget.TextView[contains(@text, 'Google Play Service is')]")
    GET_GOOGLE_PLAY_SERVICE = (MobileBy.XPATH, "//android.widget.Button[@text='Get Google Play Service']")
