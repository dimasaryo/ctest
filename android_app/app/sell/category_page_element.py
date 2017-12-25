from appium.webdriver.common.mobileby import MobileBy
from ctest.functional_test.base_locator import BaseLocator


class CategoryPageElement(BaseLocator):

    SEARCH_FIELD = (MobileBy.XPATH, " //android.widget.EditText[@content-desc='category_page_search_label']")
    CATEGORY = (MobileBy.XPATH, "//android.widget.TextView[@text='{0}']/"
                                "parent::android.widget.LinearLayout")
