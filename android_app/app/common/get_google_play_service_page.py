from ctest.functional_test.base_page import BasePage
from ctest.functional_test.elements.button import Button
from android_app.app.common.get_google_play_service_page_element import GetGooglePlayServiceElement


class GetGooglePlayServicePage(BasePage):

    def __init__(self, driver):
        self.get_google_play_service = Button(driver, GetGooglePlayServiceElement.GET_GOOGLE_PLAY_SERVICE)
        super(GetGooglePlayServicePage, self).__init__(driver, self.get_google_play_service)

    def skip(self):
        self.click_back_button()
