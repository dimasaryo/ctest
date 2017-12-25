from ctest.functional_test.constants import PASSED
from ctest.functional_test.base_page import BasePage
from ctest.functional_test.elements.button import Button
from ctest.functional_test.util import construct_locator
from android_app.app.sell.photo_page_element import PhotoPageElement


class PhotoPage(BasePage):

    def __init__(self, driver):
        photo_element = construct_locator(PhotoPageElement.PHOTO, 2)
        self.photo = Button(driver, photo_element)
        self.next_button = Button(driver, PhotoPageElement.NEXT_BUTTON)
        super(PhotoPage, self).__init__(driver, self.photo)

    def choose_photo(self, *args):
        for _, arg in enumerate(args):
            photo_element = construct_locator(PhotoPageElement.PHOTO, int(arg) + 1)
            photo = Button(self.driver, photo_element)
            photo.click()
        return PASSED

    def click_next_button(self):
        return self.next_button.click()
