from ctest.functional_test.Elements import BaseElement


class Text(BaseElement):

    def __init__(self, driver, locator):
        super(Text, self).__init__(driver, locator)

    def get_text(self):
        element = self.wait_for_visible(timeout=10)
        return element.text
