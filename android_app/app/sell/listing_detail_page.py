from selenium.common.exceptions import WebDriverException
from ctest.functional_test.constants import PASSED
from ctest.functional_test.base_page import BasePage
from ctest.functional_test.elements.text_field import TextField
from ctest.functional_test.elements.button import Button
from ctest.functional_test.elements.radio_button import RadioButton
from ctest.functional_test.elements.switch import Switch
from android_app.constants import ItemCondition, MeetUpOrDelivery
from android_app.app.sell.listing_detail_page_element import ListingDetailPageElement


class ListingDetailPage(BasePage):

    def __init__(self, driver):
        self.title_field = TextField(driver, ListingDetailPageElement.TITLE_FIELD)
        self.price = TextField(driver, ListingDetailPageElement.PRICE_FIELD)
        self.new_radio_button = RadioButton(driver, ItemCondition.new)
        self.used_radio_button = RadioButton(driver, ItemCondition.used)
        self.meet_up_switch = Switch(driver, MeetUpOrDelivery.meet_up)
        self.choose_preferred_location = Button(driver, ListingDetailPageElement.PREFERRED_LOCATION)
        self.meet_up_detail_field = TextField(driver, ListingDetailPageElement.MEETUP_DETAIL_FIELD)
        self.mailing_and_delivery_switch = Switch(driver, MeetUpOrDelivery.mailing_and_delivery)
        self.mailing_detail_field = TextField(driver, ListingDetailPageElement.MAILING_DETAIL_FIELD)
        self.description_field = TextField(driver, ListingDetailPageElement.DESCRIPTION_FIELD)
        self.list_it_button = Button(driver, ListingDetailPageElement.LIST_IT_BUTTON)
        super(ListingDetailPage, self).__init__(driver, self.title_field)

    def fill_out_form(self, title=None, price=None, item_condition=None, meet_up=False,
                      preferred_location=None, meet_up_detail=None, mailing_and_delivery=False,
                      mailing_detail=None, description=None):
        if title is not None:
            self.title_field.set_text(title)
        if price is not None:
            self.price.set_text(price)
        if item_condition is not None:
            self.choose_item_condition(item_condition)
        if meet_up:
            self.meet_up_switch.click()
            self.fill_out_meet_up_detail(preferred_location, meet_up_detail)
        if mailing_and_delivery:
            self.mailing_and_delivery_switch.click()
            self.fill_out_mailing_detail(mailing_detail)
        if description is not None:
            self.description_field.set_text(description)
        return PASSED

    def choose_item_condition(self, value):
        if value == ItemCondition.new:
            return self.new_radio_button.click()
        if value == ItemCondition.used:
            return self.used_radio_button.click()
        else:
            raise WebDriverException('Invalid value {0}'.format(value))

    def fill_out_meet_up_detail(self, preferred_location=None, meet_up_detail=None):
        if preferred_location is not None:
            pass
        if meet_up_detail is not None:
            return self.meet_up_detail_field.set_text(meet_up_detail)

    def fill_out_mailing_detail(self, mailing_detail=None):
        if mailing_detail is not None:
            return self.mailing_detail_field.set_text(mailing_detail)

    def click_list_it_button(self):
        return self.list_it_button.click()
