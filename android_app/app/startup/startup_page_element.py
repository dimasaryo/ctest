from appium.webdriver.common.mobileby import MobileBy
from ctest.functional_test.base_locator import BaseLocator


class StartupPageElement(BaseLocator):

    LOGIN_BUTTON = (MobileBy.XPATH, "//android.widget.Button[@text='Log In']")
    FACEBOOK_BUTTON = (MobileBy.XPATH, "//android.widget.Button[@text='Continue with Facebook']")
    GOOGLE_BUTTON = (MobileBy.XPATH, "//android.widget.Button[@text='Continue with Google']")
    EMAIL_SIGNUP_BUTTON = (MobileBy.XPATH, "//android.widget.Button[@text='Sign up with Email']")
