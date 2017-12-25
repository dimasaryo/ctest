from appium.webdriver.common.mobileby import MobileBy
from ctest.functional_test.elements.button import Button
from ctest.functional_test.util import construct_locator


class RadioButton(Button):

    def __init__(self, driver, value):
        locator = construct_locator((MobileBy.XPATH, "//android.widget.RadioButton[@text='{0}']"), value)
        super(RadioButton, self).__init__(driver, locator)
