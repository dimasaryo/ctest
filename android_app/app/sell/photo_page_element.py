from appium.webdriver.common.mobileby import MobileBy
from ctest.functional_test.base_locator import BaseLocator


class PhotoPageElement(BaseLocator):

    PHOTO = (MobileBy.XPATH, "//android.widget.FrameLayout[{0}]/android.widget.ImageView")
    NEXT_BUTTON = (MobileBy.XPATH, "//android.widget.TextView[@text='Next']")