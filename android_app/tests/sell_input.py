from android_app.constants import ItemCondition


class SellInput(object):

    valid_user = {
        'username': 'dimasaryoprakoso',
        'password': '123456'
    }

    item_detail = {
        'title': 'Baby shoes',
        'price': '120000',
        'description': 'This is test data',
        'item_condition': ItemCondition.new,
        'mailing_and_delivery': True,
        'mailing_detail': 'This is mailing detail',
        'category': 'Everything Else',
        'sub_category': 'Others'
    }

    listing_input = {
        'positive_test_listing_valid_item': [valid_user, item_detail]
    }
