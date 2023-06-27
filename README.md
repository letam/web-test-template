# Website Test Runner

A starter project for creating automated tests for websites and web applications.

---

<!-- TOC { -->

- [Tech Stack](#tech-stack)
- [Setup](#setup)
- [Test Command Options](#test-command-options)
  - [Usage](#usage)
  - [Options](#options)
- [Example Commands](#example-commands)
- [FAQ](#faq)

<!-- } TOC -->

---

## Tech Stack

- [Python 3.8+](https://www.python.org)
- [Selenium](https://github.com/SeleniumHQ/selenium/)
- [Pytest](https://docs.pytest.org/en/latest/)

## Setup

1. Install Python 3.8+ from [python.org](https://www.python.org)

2. Download and unzip the project from [https://github.com/letam/web-test-template/archive/master.zip](https://github.com/letam/web-test-template/archive/master.zip)

3. Open up a terminal and change your present directory to be the project directory

4. Create and activate python virtual environment for the project

   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

5. Install project requirements

   ```
   pip install -U pip
   pip install -r requirements.txt
   ```

6. Install web drivers (Optional)

   You can place binary web driver files either in `/usr/local/bin` or `./webdriver_bin`.

7. Create env file

   Copy `.env.sample` to `.env` and modify paths to drivers as needed:

   ```
   cp .env.sample .env
   ```

8. Run tests located in the the `./tests` directory located in the root
   ```
   pytest tests
   ```

## Test Command Options

**Remember to activate project's virtual environment in the project directory first:**

```
source venv/bin/activate
```

**To list all test command options, execute:**

```
pytest -h
```

### Usage

```
pytest [options] [file_or_dir] [file_or_dir] [...]
```

### Options

##### -x

Exit instantly on first error or failed test.

##### -k _EXPRESSION_

Only run tests which match the given substring expression. An
expression is a python evaluatable expression where all names
are substring-matched against test names and their parent
classes. Example: `-k 'test_method or test_other'` matches all
test functions and classes whose name contains `'test_method'` or
`'test_other'`, while `-k 'not test_method'` matches those that
don't contain `'test_method'` in their names. `-k 'not test_method
and not test_other'` will eliminate the matches. Additionally
keywords are matched to classes and functions containing extra
names in their `'extra_keyword_matches'` set, as well as functions
which have names assigned directly to them.

## Example Commands

Run tests located in utils directory and exit instantly on first error or failed test:

```
pytest -x utils
```

Run all tests which include firefox in file name or test name:

```
pytest -k 'firefox'
```

Run all tests which include firefox in file name or test name **and** contained in the tests directory:

```
pytest -k 'firefox' tests
```

Run all tests which do not include **safari** in file name nor test name:

```
pytest -k 'not safari'
```

Run all tests which do not include safari in file name nor test name **_and_** only include tests that have the **fill** word in the test name:

```
pytest -k 'not safari and fill'
```

Run tests located in **tests/example** directory:

```
pytest tests/example
```

Run tests located in **tests/example/test_chrome.py** file:

```
pytest tests/example/test_chrome.py
```

Run tests located in **tests/example/test_chrome.py** file and include **fill** word in the test name:

```
pytest tests/example/test_chrome.py -k 'fill'
```

## FAQ

##### On macOS I get a dialog saying: "...can’t be opened because Apple cannot check it for malicious software."

You may need to explicitly open the driver one time in order to authorize its execution on your machine. You can do this by right-clicking on the binary file and selecting "Open" in the menu and then "Open" in the dialog that pops up. You can close the terminate the terminal that opens.

##### I get an error saying: "selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version ..."

Ensure that your version of Chrome webdriver matches the version of the Chrome browser that you have installed on your machine.
