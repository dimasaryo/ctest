from ctest.functional_test.base_page import BasePage
from ctest.functional_test.elements.button import Button
from android_app.app.sell.post_listing_page_element import PostListingPageElement


class PostListingPage(BasePage):

    def __init__(self, driver):
        self.maybe_next_time_button = Button(driver, PostListingPageElement.MAYBE_NEXT_TIME_BUTTON)
        super(PostListingPage, self).__init__(driver, self.maybe_next_time_button)

    def click_may_be_next_time_button(self):
        """
        Click may be next time button.
        
        :return: PASSED or WebdriverException raised.
        """
        return self.maybe_next_time_button.click()
