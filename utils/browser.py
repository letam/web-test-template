from typing import Callable
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (
    WebDriverException,
    InvalidSelectorException,
    NoSuchElementException,
)

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

    def find_by_text(self, text: str, timeout=0):
        return self.wait_for_element_by_xpath(
            f'//*[contains(string(), "{text}")]', timeout
        )

    def find_button_by_text(self, text: str, timeout=0):
        return self.wait_for_element_by_xpath(
            f'//button[contains(string(), "{text}")]', timeout
        )

    def find_by_name(self, name: str, timeout=0):
        return self.wait_for(lambda: self.driver.find_element_by_name(name), timeout)

    def fill(self, field_name: str, value: str):
        self.find_by_name(field_name).send_keys(value)


def Browser(driver_name: str = "firefox", *args, **kwargs):

    if not driver_name:
        driver_name = "firefox"

    if "executable_path" not in kwargs:
        if driver_name == "firefox" and "firefox" in DRIVERS:
            kwargs["executable_path"] = DRIVERS["firefox"]
        elif driver_name == "chrome" and "chrome" in DRIVERS:
            kwargs["executable_path"] = DRIVERS["chrome"]

    Driver = getattr(webdriver, driver_name.capitalize())

    class BrowserClass(BrowserFunctionsMixin, Driver):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.driver = self

    browser = BrowserClass(*args, **kwargs)
    return browser
