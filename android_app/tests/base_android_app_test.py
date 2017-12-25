from selenium.common.exceptions import WebDriverException
from ctest.functional_test.base_test import BaseTest
from android_app.app.common.get_google_play_service_page import GetGooglePlayServicePage


class BaseAndroidAppTest(BaseTest):

    def skip_get_google_play_service(self):
        try:
            get_google_play_service_page = GetGooglePlayServicePage(self.driver)
            get_google_play_service_page.skip()
        except WebDriverException:
            pass
