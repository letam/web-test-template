# Website Test Runner

A starter project for creating automated tests for websites and web applications.

## Tech Stack

- [Python 3.8+](https://www.python.org/downloads/release/python-380rc1/)
- [Selenium](https://github.com/SeleniumHQ/selenium/)
- [Pytest](https://docs.pytest.org/en/latest/)
- [Splinter](https://splinter.readthedocs.io/en/latest/)

## Installation
1. Install Python 3.8+ from [python.org](https://www.python.org)
2. Download and unzip the project from [https://github.com/letam/web-test-template/archive/master.zip](https://github.com/letam/web-test-template/archive/master.zip)
3. Open up a terminal and change your present directory to be the project directory.
4. Create and activate python virtual environment for the project:
```
python3 -m venv venv
source venv/bin/activate
```
5. Install project requirements:
```
pip install -U pip
pip install -r requirements.txt
```
6. Install web drivers (Optional):

   You can place binary web driver files either in `/usr/local/bin` or `./webdriver_bin`.

7. Create env file:

   Copy `.env.sample` to `.env` and modify paths to drivers as needed.

8. Run tests:
```
sh test.sh
```

## FAQ

### On macOS I get a dialog saying: "...can’t be opened because Apple cannot check it for malicious software."

You may need to explicitly open the driver one time in order to authorize its execution on your machine. You can do this by right-clicking on the binary file and selecting "Open" in the menu and then "Open" in the dialog that pops up. You can close the terminate the terminal that opens.

### I get an error saying: "selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version ..."

Ensure that your version of Chrome webdriver matches the version of the Chrome browser that you have installed on your machine.
