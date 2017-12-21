from ctest.functional_test.Elements import BaseElement


class TextField(BaseElement):

    def __init__(self, driver, locator):
        super(TextField, self).__init__(driver, locator)

    def set_text(self, value, key=None):
        element = self.wait_for_visible(timeout=10)
        element.send_keys(value)
        if key is not None:
            element.send_keys(key)