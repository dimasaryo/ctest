import unittest

from appium import webdriver as appium_driver
from selenium.common.exceptions import WebDriverException

from ctest.functional_test.constants import Platform
from ctest.functional_test.config import TestConfig


class BaseTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.driver = None

    def setUp(self):
        super(BaseTest, self).setUp()
        try:
            self.get_driver()
            self.driver.launch_app()
        except WebDriverException:
            self.cleanup_driver()

    def tearDown(self):
        super(BaseTest, self).tearDown()
        self.cleanup_driver()

    def cleanup_driver(self):
        if self.driver is not None:
            self.remove_app()
            self.driver.quit()

    def remove_app(self):
        if TestConfig['remove_app'] == 'True' and \
            (TestConfig['platform'] == Platform['android'] or
             TestConfig['platform'] == Platform['ios']):
            self.driver.remove_app(TestConfig['caps'].get('appPackage', ''))

    def get_driver(self):
        if TestConfig['platform'] == Platform['android'] or \
                TestConfig['platform'] == Platform['ios'] or \
                TestConfig['platform'] == Platform['mobile_web']:
            self.driver = appium_driver.Remote(
                command_executor=TestConfig['remote_url'],
                desired_capabilities=TestConfig['caps']
            )
