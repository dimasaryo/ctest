#!/usr/bin/python
# -*- coding: utf-8 -*-
from ctest.functional_test.constants import Platform

TestConfig = {
    'caps': {
        'app': '/Users/dimasaryo/Carousell/Carousell-Android-App.apk',
        'platformVersion': '5.1',
        'platformName': 'Android',
        'deviceName': 'Android',
        'appPackage': 'com.thecarousell.Carousell',
        'appActivity': 'com.thecarousell.Carousell.activities.WelcomeActivity'
    },
    'page_load_timeout': 20,
    'element_load_timeout': 10,
    'platform': Platform['android'],
    'remote_url': 'http://localhost:4444/wd/hub',
    'remove_app': 'False',
    'currency': 'IDR',
    'locale': 'en_US',
    'currency_format': u'¤ #,##0'
}