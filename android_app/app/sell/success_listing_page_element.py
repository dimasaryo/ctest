from appium.webdriver.common.mobileby import MobileBy
from ctest.functional_test.base_locator import BaseLocator


class SuccessListingPageElement(BaseLocator):
    CLOSE_BUTTON = (MobileBy.XPATH, "//android.widget.ImageView[@content-desc='Image']")
