from os import getenv

from dotenv import load_dotenv

load_dotenv()


DRIVERS = {
    "firefox": getenv('FIREFOX'),
    "chrome": getenv('CHROME'),
}

# max timeout to wait for something to happen
WAIT_TIME = 1

# poll for something at a default rate of 1/10 of a second
POLL_FREQUENCY = 1 / 10
