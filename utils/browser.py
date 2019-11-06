from typing import Callable
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (
    WebDriverException,
    InvalidSelectorException,
    NoSuchElementException,
)
from selenium.webdriver.support.ui import Select

from settings import DRIVERS, WAIT_TIME, POLL_FREQUENCY


class BrowserFunctionsMixin:
    """
    A set of handy methods built on top of the selenium WebDriver class.
    Reference the selenium API at: https://selenium-python.readthedocs.io/api.html
    """

    def visit(self, url):
        self.driver.get(url)

    @staticmethod
    def wait(timeout=WAIT_TIME):
        time.sleep(timeout)

    def wait_for(
        self,
        method: Callable,
        timeout=WAIT_TIME,
        poll_frequency=POLL_FREQUENCY,
        message="",
        **kwargs,
    ):
        return WebDriverWait(self.driver, timeout, poll_frequency, **kwargs).until(
            lambda x: method(), message
        )

    def wait_for_not(
        self,
        method: Callable,
        timeout=WAIT_TIME,
        poll_frequency=POLL_FREQUENCY,
        message="",
        **kwargs,
    ):
        return WebDriverWait(self.driver, timeout, poll_frequency, **kwargs).until_not(
            lambda x: method(), message
        )

    def wait_for_element_by_xpath(self, query: str, timeout=WAIT_TIME):
        return self.wait_for(lambda: self.driver.find_element_by_xpath(query), timeout)

    def xpath(self, expr: str):
        try:
            return self.driver.find_element_by_xpath(expr)
        except NoSuchElementException:
            return None

    def xpath_validate(self, expr: str):
        try:
            self.xpath(expr)
            return True
        except InvalidSelectorException:
            return False

    def find_by_text(self, text: str, timeout=0, tag_name: str = '*'):
        ''' Note: If tag name is not provided, then may not return the
            direct element containing text. '''
        return self.wait_for_element_by_xpath(
            f'//{tag_name}[contains(string(), "{text}")]', timeout
        )

    def find_button_by_text(self, text: str, timeout=0):
        return self.find_by_text(text, timeout, 'button')

    def find_a_by_text(self, text: str, timeout=0):
        return self.find_by_text(text, timeout, 'a')

    def find_by_name(self, name: str, timeout=0):
        return self.wait_for(lambda: self.driver.find_element_by_name(name), timeout)

    def fill(self, field_name: str, value: str):
        self.find_by_name(field_name).send_keys(value)

    def get_url_domain_name(self):
        return self.driver.current_url.split('//')[1].split('/', 1)[0]

    def get_url_path(self):
        return self.driver.current_url.split('//')[1].split('/', 1)[1]

    @property
    def browser_name(self):
        return self.driver.capabilities.get('browserName')

    def click(self, element):
        """ Tell driver to click provided element.
            If browser is Safari, click via javascript, since
            `element.click()` does not seem to work on safari
        """
        if self.browser_name == 'Safari':
            self.driver.execute_script('arguments[0].click()', element)
        else:
            element.click()

    def select_option_by_visible_text(self, element, option_text: str):
        select = Select(element)
        select.select_by_visible_text(option_text)

    def scroll_into_view(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView()', element)

    def click_checkbox(self, element):
        ''' Ensure that checkbox element appears so that we can indeeed click it. '''
        self.driver.execute_script(
            'arguments[0].style["-moz-appearance"] = "checkbox"', element
        )
        self.driver.execute_script(
            'arguments[0].style["-webkit-appearance"] = "checkbox"', element
        )
        self.click(element)


def Browser(driver_name: str = "firefox", *args, **kwargs):

    if not driver_name:
        driver_name = "firefox"

    if "executable_path" not in kwargs:
        if driver_name == "firefox" and "firefox" in DRIVERS:
            kwargs["executable_path"] = DRIVERS["firefox"]
        elif driver_name == "chrome" and "chrome" in DRIVERS:
            kwargs["executable_path"] = DRIVERS["chrome"]

    options = None
    headless = kwargs.pop("headless", False)
    if headless:
        if driver_name == "firefox":
            from selenium.webdriver.firefox.options import Options
        elif driver_name == "chrome":
            from selenium.webdriver.chrome.options import Options
        else:
            Options = None
        if Options:
            options = Options()
            options.add_argument("-headless")
    if options:
        kwargs["options"] = options

    Driver = getattr(webdriver, driver_name.capitalize())

    class BrowserClass(BrowserFunctionsMixin, Driver):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.driver = self

    browser = BrowserClass(*args, **kwargs)
    return browser
