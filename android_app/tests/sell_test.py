from ctest.functional_test.constants import PASSED
from android_app.tests.base_android_app_test import BaseAndroidAppTest
from android_app.app.common.alert_page import AlertPage
from android_app.app.startup.startup_page import StartupPage
from android_app.app.login.login_page import LoginPage
from android_app.app.collection.collection_page import CollectionPage
from android_app.app.collection.category_collection_page import CategoryCollectionPage
from android_app.app.sell.photo_page import PhotoPage
from android_app.app.sell.category_page import CategoryPage
from android_app.app.sell.listing_detail_page import ListingDetailPage
from android_app.app.sell.post_listing_page import PostListingPage
from android_app.app.collection.filter_and_sort_page import FilterAndSortPage
from android_app.constants import SortBy

from android_app.tests.sell_input import SellInput


class TestSell(BaseAndroidAppTest):

    def setUp(self):
        super(TestSell, self).setUp()

    def tearDown(self):
        super(TestSell, self).tearDown()

    def test_listing_valid_item(self):
        """
        Test listing with valid item.
        
        :return: PASSED or WebdriverException raised.
        """
        for data in SellInput.listing_input.items():
            self.listing_valid_item(data[1][0], data[1][1])

    def listing_valid_item(self, user, item_detail):
        """
        Listing valid item.
        
        :param user: Username and password.
        :param item_detail: Item detail.
        :return: PASSED or WebdriverException raised.
        """
        alert_page = AlertPage(self.driver)
        alert_page.dismiss()
        startup_page = StartupPage(self.driver)
        startup_page.open_login_page()

        login_page = LoginPage(self.driver)
        login_page.login(
            username=user['username'],
            password=user['password'])
        self.skip_get_google_play_service()

        collection_page = CollectionPage(self.driver)
        collection_page.open_sell_form()

        photo_page = PhotoPage(self.driver)
        photo_page.choose_photo(1, 2)
        photo_page.click_next_button()

        category_page = CategoryPage(self.driver)
        category_page.search(item_detail['category'])
        category_page.choose_category(
            item_detail['category'],
            item_detail['sub_category'])
        listing_detail_page = ListingDetailPage(self.driver)
        listing_detail_page.fill_out_form(
            title=item_detail['title'],
            price=item_detail['price'],
            item_condition=item_detail['item_condition'],
            mailing_and_delivery=item_detail['mailing_and_delivery'],
            mailing_detail=item_detail['mailing_detail'],
            description=item_detail['description'])
        listing_detail_page.click_list_it_button()

        post_listing_page = PostListingPage(self.driver)
        post_listing_page.click_may_be_next_time_button()

        collection_page = CollectionPage(self.driver)
        collection_page.header.switch_to_browse()
        collection_page.open_everything_else_category()

        category_collection_page = CategoryCollectionPage(self.driver)
        category_collection_page.change_filter()

        filter_and_sort_page = FilterAndSortPage(self.driver)
        filter_and_sort_page.choose_sorting_method(SortBy.recent)
        filter_and_sort_page.apply()

        category_collection_page = CategoryCollectionPage(self.driver)
        result = category_collection_page.listing_is_exists(
            username=user['username'],
            title=item_detail['title'],
            price=item_detail['price'],
            item_condition=item_detail['item_condition'],
            description=item_detail['description']
        )
        assert result is PASSED



