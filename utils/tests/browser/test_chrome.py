from pytest import fixture

from utils.browser import Browser


driver_name = "chrome"


@fixture(scope="module")
def browser():
    with Browser(driver_name) as browser:
        yield browser


from ._tests import *
