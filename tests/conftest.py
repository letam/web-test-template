from pytest import fixture

from utils.browser import Browser


@fixture
def browser():
    with Browser() as browser:  # default driver is firefox
        yield browser


@fixture
def headless_browser():
    with Browser(headless=True) as browser:
        yield browser


@fixture
def chrome_browser():
    with Browser("chrome") as browser:
        yield browser


@fixture
def safari_browser():
    with Browser("safari") as browser:
        yield browser
