from money import Money
from ctest.functional_test.config import TestConfig


def construct_locator(locator, *args):
    """
    Format the locator using the given arguments.
    
    :param locator: Targeted locator.
    :param args: Arguments.
    :return: Formatted locator.
    """
    temp = list(locator)
    temp[1] = temp[1].format(*args)
    return tuple(temp)


def format_currency(value):
    """
    Format currency.
    
    :param value: Targeted value.
    :return: Formatted value.
    """
    money = Money(value, TestConfig['currency'])
    return money.format(TestConfig['locale'], TestConfig['currency_format'])
