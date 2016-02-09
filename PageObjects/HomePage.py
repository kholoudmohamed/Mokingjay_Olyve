import http.client
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self._driver = driver

        # All home page variables
        global header_olyve_logo
        header_olyve_logo = self._driver.find_element_by_xpath('html/body/div[1]/div/div/div[1]/nav/div[1]/div[2]/a/img')
        global header_shop_button
        header_shop_button = self._driver.find_element_by_xpath('html/body/div[1]/div/div/div[1]/nav/div[1]/div[1]/ul/li/a')
        global header_track_button
        header_track_button = self._driver.find_element_by_xpath('html/body/div[1]/div/div/div[1]/nav/div[1]/div[4]/ul/li/a')
        global header_message_ribbon
        header_message_ribbon = self._driver.find_element_by_xpath('//*[@id="home-container"]/div/div[1]/div')
        global footer_copyright
        footer_copyright = self._driver.find_element_by_xpath('html/body/div[1]/div/div/div[6]/div/div[1]/div[1]')
        global footer_privacyterms
        footer_privacyterms = self._driver.find_element_by_xpath('html/body/div[1]/div/div/div[6]/div/div[2]/div[1]/a')
        global footer_codeofconduct
        footer_codeofconduct = self._driver.find_element_by_xpath('html/body/div[1]/div/div/div[6]/div/div[3]/div[1]/a')
        global footer_phonenumber
        footer_phonenumber = self._driver.find_element_by_xpath('html/body/div[1]/div/div/div[6]/div/div[1]/div[2]/a')
        global footer_serviceemail
        footer_serviceemail = self._driver.find_element_by_xpath('html/body/div[1]/div/div/div[6]/div/div[2]/div[2]/a')


    # wait till home page logo is displayed
    def home_page_load(self,time_to_wait,by_method,locator):
        element = WebDriverWait(self._driver, time_to_wait).until(EC.presence_of_element_located((by_method, locator)))

    # Find olyve logo and check if it's displayed
    @property
    def is_logo_displayed(self):
        return header_olyve_logo.is_displayed()

    # Find header shop button and check if it's enabled
    @property
    def is_header_shop_button_enabled(self):
        return header_shop_button.is_enabled()

    # Find track button and check if it's enabled
    @property
    def is_header_track_button_enabled(self):
        return header_track_button.is_enabled()

    # Find and return header ribbon message
    @property
    def get_header_ribbon_message(self):
        actual_header_message_ribbon = header_message_ribbon.text
        return actual_header_message_ribbon

    # Find and return footer copyright text
    @property
    def get_footer_copyright_text(self):
        actual_footer_copyright_text = footer_copyright.text
        return actual_footer_copyright_text

    # Find and return footer privacy terms text
    @property
    def get_footer_privacyterms_text(self):
        actual_footer_privacyterms_text = footer_privacyterms.text
        return actual_footer_privacyterms_text

    # Assert privacy terms url
    @property
    def get_privacyterms_url(self):
        footer_privacyterms.click()
        WebDriverWait(self._driver, 40).until(EC.title_contains("privacy"))
        return self._driver.current_url

    # Find and return footer code of conduct text
    @property
    def get_footer_codeofconduct_text(self):
        actual_footer_codeofconduct_text = footer_codeofconduct.text
        return actual_footer_codeofconduct_text

    # Assert code of conduct url
    @property
    def get_codeofconduct_url(self):
        footer_codeofconduct.click()
        WebDriverWait(self._driver, 40).until(EC.title_contains("codeofconduct"))
        return self._driver.current_url

    # Find and return footer phone number
    @property
    def get_footer_phonenumber_text(self):
        actual_footer_phonenumber_text = footer_phonenumber.text
        return actual_footer_phonenumber_text

    @property
    def verify_phonenumber_href(self):
        phonenumber_href = footer_phonenumber.get_attribute('href')
        phonenumber = "tel:"
        if phonenumber in phonenumber_href:
            return True
        else:
            return False

    # Find and return footer email
    @property
    def get_footer_serviceemail_text(self):
        actual_footer_serviceemail_text = footer_serviceemail.text
        return actual_footer_serviceemail_text

    @property
    def verify_serviceamil_href(self):
        servicemail_href = footer_serviceemail.get_attribute('href')
        servicemail = "mailto:"
        if servicemail in servicemail_href:
            return True
        else:
            return False

    def get_page_status(self):
        try:
            while httplib.HTTPS_PORT != 200:
                self._driver.implicitly_wait(10)
            return self._driver.current_url
        except:
            return None

    def facebook_social_info(self):
        # Find the Facebook link in the home page then click on the link found
        self._driver.find_element_by_xpath("html/body/div[1]/div/div/div[4]/div/div[2]/div/a[1]/i").click()
        # Wait till Facebook page is loaded
        current_url = HomePage.get_page_status(self)
        # Retrun the Facebook link
        return current_url

    def instgram_social_info(self):
        # Find the Instgram link in the home page then click on it
        self._driver.find_element_by_xpath("html/body/div[1]/div/div/div[4]/div/div[2]/div/a[2]/i").click()
        # Wait till Instgram page is loaded
        current_url = HomePage.get_page_status(self)
        # Return the Instgram link
        return current_url

    def pinterest_social_info(self):
        # Find the Pinterest link in the home page then click on it
        self._driver.find_element_by_xpath("html/body/div[1]/div/div/div[4]/div/div[2]/div/a[3]/i").click()
        # Wait till Pinterest page is loaded
        current_url = HomePage.get_page_status(self)
        # Return the Pinterest link
        return current_url

    def twitter_social_info(self):
        # Find the Twitter link in the home page then click on it
        self._driver.find_element_by_xpath("html/body/div[1]/div/div/div[4]/div/div[2]/div/a[4]/i").click()
        # Wait till Twitter page is loaded
        current_url = HomePage.get_page_status(self)
        # Return the Twitter link
        return current_url
