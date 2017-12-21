from selenium.common.exceptions import WebDriverException


class BasePage(object):

    def __init__(self, driver, identifier):
        self.driver = driver
        self.identifier = identifier

    def wait_for_page_load(self):
        try:
            self.identifier.wait_for_visible(timeout=10)
        except WebDriverException as e:
            raise Exception("Failed load page. Error: {0}".format(e.__str__()))
