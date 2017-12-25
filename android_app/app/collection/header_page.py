from ctest.functional_test.base_page import BasePage
from ctest.functional_test.elements.tab import Tab

BROWSE = 'BROWSE'
GROUPS = 'GROUPS'
ACTIVITY = 'ACTIVITY'
ME = 'ME'


class HeaderPage(BasePage):

    def __init__(self, driver):
        self.browse_tab = Tab(driver, BROWSE)
        self.groups_tab = Tab(driver, GROUPS)
        self.activity_tab = Tab(driver, ACTIVITY)
        self.me_tab = Tab(driver, ME)
        super(HeaderPage, self).__init__(driver, self.browse_tab)

    def switch_to_browse(self):
        return self.browse_tab.click()

    def switch_to_groups(self):
        return self.groups_tab.click()

    def switch_to_activity(self):
        return self.activity_tab.click()

    def switch_to_me(self):
        return self.me_tab.click()
