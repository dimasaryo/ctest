from appium.webdriver.common.mobileby import MobileBy
from ctest.functional_test.base_locator import BaseLocator


class CategoryCollectionPageElement(BaseLocator):

    FILTER_BUTTON = (MobileBy.XPATH, "//android.widget.TextView[@text='SORT/FILTER']/"
                                     "parent::android.widget.LinearLayout")
    OK_GOT_IT_BUTTON = (MobileBy.XPATH, "//android.widget.TextView[@text='OK, Got it!']")
    ITEM_DETAIL = (MobileBy.XPATH, "//android.widget.TextView[@text='{0}']/parent::"
                                   "android.widget.RelativeLayout/android.widget.TextView[@text='{1}']")
