from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from Utilities import FileLocator


class Browser:

    _driver = None

    def __init__(self):
        self._driver = webdriver

    # The following function detects the driver type used (default driver is Firefox)
    # From Configuration File read the location of the driver in "DriverConfiguration" section
    @classmethod
    def initialize_driver(cls, driver_type=None):

        if driver_type is not None:
            if driver_type == 'chrome':
                _chrome_driver_file_location = FileLocator.read_config_get_file_location('DriverConfiguration',
                                                                                         'ChromeDriverLocation')
                cls._driver = webdriver.Chrome(_chrome_driver_file_location)
            elif driver_type == 'ie':
                _ie_driver_file_location = FileLocator.read_config_get_file_location('DriverConfiguration',
                                                                                     'IEdriverLocation')
                cls._driver = webdriver.Ie(_ie_driver_file_location)
            elif driver_type == 'firefox':
                cls._driver = webdriver.Firefox()
            else:
                raise WebDriverException("Please provide a valid web driver! options: chrome | ie")
        else:
            cls._driver = webdriver.Firefox()

    @classmethod
    # The following function closes the driver which will close the current opened page
    def close_driver(cls):
        cls._driver.close()

    @classmethod
    # The following function quites the driver which will close all the opened pages
    def quit_driver(cls):
        cls._driver.quit()