from ctest.functional_test.base_page import BasePage
from ctest.functional_test.elements.button import Button
from android_app.app.startup.startup_page_element import StartupPageElement


class StartupPage(BasePage):

    def __init__(self, driver):
        self.login_button = Button(driver, StartupPageElement.LOGIN_BUTTON)
        super(StartupPage, self).__init__(driver, self.login_button)

    def open_login_page(self):
        """
        Open login page.
        
        :return: PASSED or WebdriverException raised.
        """
        self.login_button.click()




