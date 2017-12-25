from appium.webdriver.common.mobileby import MobileBy
from ctest.functional_test.base_locator import BaseLocator


class PostListingPageElement(BaseLocator):

    MAYBE_NEXT_TIME_BUTTON = (MobileBy.XPATH, "//android.widget.TextView[@text='Maybe next time']/"
                                              "parent::android.widget.FrameLayout")
