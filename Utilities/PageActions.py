from selenium.webdriver.common.alert import *
from selenium.webdriver.common.action_chains import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from Utilities.Browser import Browser
from selenium.common.exceptions import TimeoutException


class BasicActions(Browser):

    def __init__(self):
        super(BasicActions, self).__init__()

    # The following common function is used in different classes to open the URL of a page using the selected driver
    @staticmethod
    def navigate(url):
        Browser._driver.get(url)

    # The following common function is used in different classes to maximize the window size of the driver
    @staticmethod
    def maximize_window():
        Browser._driver.maximize_window()

    # The following common function is used in different classes to accept any displayed alert
    @staticmethod
    def accept_alert():
        Alert(Browser._driver).accept()

    # The following common function is used in different classes to dismiss any displayed alert
    @staticmethod
    def dismiss_alert():
        Alert(Browser._driver).accept().dismiss()

    # The following common function is used in different classes to return to the previous page of the browser
    @staticmethod
    def go_back():
        Browser._driver.back()

    # The following common function is used in different classes to refresh the current page of the browser
    @staticmethod
    def refresh_page():
        Browser._driver.refresh()

    # The following common function is used in different classes to implicitly wait for defined time
    @staticmethod
    def implicit_wait(time_to_wait):
        Browser._driver.implicitly_wait(time_to_wait)

    # The following common function is used in different classes to return the current URL of the browser
    @staticmethod
    def get_current_url():
        return Browser._driver.current_url

    @staticmethod
    # The following common function is used in different classes to explicit wait until presence of configurable element
    # With return as conditional action dependency
    def explicit_wait(self, time_to_wait, locator):
        try:
            element = WebDriverWait(self._driver, time_to_wait).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def wait_until_element_clickable(self, time_to_wait, locator):
        WebDriverWait(self._driver, time_to_wait).until(EC.element_to_be_clickable(locator))

    @staticmethod
    # The following common function is used to get the scroll top value of the window
    def window_scroll_top(self):
        """
        Gets the top of the scrolling area for ``window``.

        :returns: The top of the scrolling area.
        """
        return self._driver.execute_script("""
        return window.scrollY;
        """)

