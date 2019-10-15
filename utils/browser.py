from splinter.browser import Browser as SplinterBrowser

from settings import DRIVERS


def Browser(driver_name: str = 'firefox', executable_path: str = None, *args, **kwargs):
    additional_kwargs = {}
    if not executable_path:
        if driver_name == 'firefox' and 'firefox' in DRIVERS:
            executable_path = DRIVERS['firefox']
        elif driver_name == 'chrome' and 'chrome' in DRIVERS:
            executable_path = DRIVERS['chrome']

    if executable_path:
        additional_kwargs['executable_path'] = executable_path
    browser = SplinterBrowser(driver_name, *args, **kwargs, **additional_kwargs)
    return browser
