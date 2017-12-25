from appium.webdriver.common.mobileby import MobileBy
from ctest.functional_test.base_locator import BaseLocator


class LoginPageElement(BaseLocator):

    USERNAME_FIELD = (MobileBy.XPATH, "//android.widget.LinearLayout[@text='email or username']"
                                      "//android.widget.EditText")
    PASSWORD_FIELD = (MobileBy.XPATH, "//android.widget.LinearLayout[@text='password']"
                                      "//android.widget.EditText")
    LOGIN_BUTTON = (MobileBy.XPATH, "//android.widget.Button[@text='Log In']")
    FORGOT_PASSWORD = (MobileBy.XPATH, "//android.widget.TextView[@text='Forgot your password?']")