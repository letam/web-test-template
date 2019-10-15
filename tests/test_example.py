import pytest

from utils.browser import Browser


@pytest.fixture
def browser():
#    driver_name = "chrome"
#    with Browser(driver_name) as browser:
    with Browser() as browser:
        yield browser


def test_example(browser):
    url = "http://example.org"
    browser.visit(url)
    assert browser.find_by_tag("h1").first.value == "Example Domain"


def test_visiting_google_com_returns_a_page_with_Google_in_title(browser):
    browser.visit("http://www.google.com/")
    assert "Google" in browser.title


def test_filling_Splinter_in_the_search_box_returns_Splinter_website(browser):
    browser.visit("http://www.google.com/")
    browser.fill("q", "python splinter")
    search_button = browser.find_by_name("btnK").first
    while not search_button.visible:
        # waits for the JavaScript to put the button on the page
        pass
    search_button.click()
    assert browser.is_text_present("splinter.readthedocs.io")
