from ctest.functional_test.base_page import BasePage
from ctest.functional_test.elements.text_field import TextField
from ctest.functional_test.elements.button import Button
from android_app.app.login.login_page_element import LoginPageElement


class LoginPage(BasePage):

    def __init__(self, driver):
        self.username_field = TextField(driver, LoginPageElement.USERNAME_FIELD)
        self.password_field = TextField(driver, LoginPageElement.PASSWORD_FIELD)
        self.login_button = Button(driver, LoginPageElement.LOGIN_BUTTON)
        super(LoginPage, self).__init__(driver, self.username_field)

    def login(self, username, password):
        """
        Login.
        
        :param username: Username.
        :param password: Password.
        :return: 
        """
        self.username_field.set_text(username)
        self.password_field.set_text(password)
        return self.login_button.click()
