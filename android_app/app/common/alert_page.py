from ctest.functional_test.base_page import BasePage
from ctest.functional_test.elements.button import Button
from android_app.app.common.alert_page_element import AlertPageElement


class AlertPage(BasePage):

    def __init__(self, driver):
        self.ok_button = Button(driver, AlertPageElement.OK_BUTTON)
        super(AlertPage, self).__init__(driver, self.ok_button)

    def dismiss(self):
        return self.ok_button.click()
