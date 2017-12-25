from ctest.functional_test.base_page import BasePage
from ctest.functional_test.elements.button import Button
from android_app.app.sell.success_listing_page_element import SuccessListingPageElement


class PostListingPage(BasePage):

    def __init__(self, driver):
        self.close_button = Button(driver, SuccessListingPageElement.CLOSE_BUTTON)
        super(PostListingPage, self).__init__(driver, self.close_button)

    def click_may_be_next_time_button(self):
        return self.close_button.click()
