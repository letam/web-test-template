from pytest import fixture

from utils.browser import Browser

driver_name = "firefox"


@fixture(scope="module")
def browser():
    with Browser(headless=True) as browser:  # default driver is firefox
        yield browser


from ._tests import *
