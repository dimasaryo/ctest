from appium.webdriver.common.mobileby import MobileBy
from ctest.functional_test.base_locator import BaseLocator


class CollectionPageElement(BaseLocator):

    SELL_BUTTON = (MobileBy.XPATH, "//android.widget.Button[@text='SELL']")
    BROWSE_BUTTON = (MobileBy.XPATH, "//android.widget.TextView[@text='Browse']")
    EVERYTHING_ELSE_CATEGORY = (MobileBy.XPATH, "//android.widget.TextView[@text='Everything Else']/"
                                                "parent::android.widget.FrameLayout")
