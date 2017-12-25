from appium.webdriver.common.mobileby import MobileBy
from ctest.functional_test.base_locator import BaseLocator


class DealLocationPageElement(object):

    SEARCH_BUTTON = (MobileBy.XPATH, "//android.widget.ImageView[@content-desc='Search']")
    SEARCH_FIELD = (MobileBy.XPATH, "//android.widget.EditText[@text='Search']")
    LOCATION_LIST = (MobileBy.XPATH, "//android.widget.TextView[@text='{0}']/"
                                     "parent::android.widget.LinearLayout/parent::android.widget.LinearLayout")
