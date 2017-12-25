from appium.webdriver.common.mobileby import MobileBy
from ctest.functional_test.base_locator import BaseLocator


class ListingDetailPageElement(BaseLocator):

    TITLE_FIELD = (MobileBy.XPATH, "//android.widget.EditText[@content-desc='title']")
    PRICE_FIELD = (MobileBy.XPATH, "//android.widget.EditText[@content-desc='price']")
    PREFERRED_LOCATION = (MobileBy.XPATH, "//android.widget.TextView[@text='Choose preferred location']/"
                                          "parent::android.widget.LinearLayout")
    MEETUP_DETAIL_FIELD = (MobileBy.XPATH, "//android.widget.EditText[@content-desc='meetup_details']")
    MAILING_DETAIL_FIELD = (MobileBy.XPATH, "//android.widget.EditText[@content-desc='mailing_details']")
    DESCRIPTION_FIELD = (MobileBy.XPATH, "//android.widget.EditText[@content-desc='description']")
    LIST_IT_BUTTON = (MobileBy.XPATH, "//android.widget.FrameLayout[@content-desc='sell_form_page_list_it_button']")