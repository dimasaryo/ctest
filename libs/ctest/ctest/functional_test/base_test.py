import unittest
from appium import webdriver as appium_driver
from selenium.common.exceptions import WebDriverException

from ctest.functional_test.constants import Platform
from ctest.functional_test.config import TestConfig


class BaseTest(unittest.TestCase):
    """
    BaseTest
    """

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.driver = None

    def setUp(self):
        """
        Setup method. This method will be executed before each test.
        
        :return: None.
        """
        super(BaseTest, self).setUp()
        try:
            self.get_driver()
            self.driver.launch_app()
        except WebDriverException:
            self.cleanup_driver()

    def tearDown(self):
        """
        Tear down method. This method will be executed after each test.
        
        :return: None.
        """
        super(BaseTest, self).tearDown()
        self.cleanup_driver()

    def cleanup_driver(self):
        """
        Clean up webdriver.
        
        :return: None.
        """
        if self.driver is not None:
            self.remove_app()
            self.driver.quit()

    def remove_app(self):
        """
        Remove app (Android & iOS only).
        
        :return: None.
        """
        if TestConfig['remove_app'] == 'True' and \
            (TestConfig['platform'] == Platform['android'] or
             TestConfig['platform'] == Platform['ios']):
            self.driver.remove_app(TestConfig['caps'].get('appPackage', ''))

    def get_driver(self):
        """
        Get webdriver.
        
        :return: Webdriver.
        """
        if TestConfig['platform'] == Platform['android'] or \
                TestConfig['platform'] == Platform['ios'] or \
                TestConfig['platform'] == Platform['mobile_web']:
            self.driver = appium_driver.Remote(
                command_executor=TestConfig['remote_url'],
                desired_capabilities=TestConfig['caps']
            )
