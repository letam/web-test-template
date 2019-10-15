from os import getenv
from dotenv import load_dotenv

load_dotenv()


DRIVERS = {
    "firefox": getenv('FIREFOX'),
    "chrome": getenv('CHROME'),
}
