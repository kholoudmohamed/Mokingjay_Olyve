class HomePage:
    def __init__(self,driver):
        self._driver = driver

    # Find olyve logo and check if it's displayed
    @property
    def is_logo_displayed(self):
        header_olyve_logo = self._driver.find_element_by_xpath('html/body/div[1]/div/div/div[1]/nav/div[1]/div[2]/a/img')
        return header_olyve_logo.is_displayed()

    # Find header shop button and check if it's enabled
    @property
    def is_header_shop_button_enabled(self):
        header_shop_button = self._driver.find_element_by_xpath('html/body/div[1]/div/div/div[1]/nav/div[1]/div[1]/ul/li/a')
        return header_shop_button.is_enabled()

    # Find track button and check if it's enabled
    @property
    def is_header_track_button_enabled(self):
        header_track_button = self._driver.find_element_by_xpath('html/body/div[1]/div/div/div[1]/nav/div[1]/div[4]/ul/li/a')
        return header_track_button.is_enabled()

    # Find and return header ribbon message
    @property
    def get_header_ribbon_message(self):
        header_message_ribbon = self._driver.find_element_by_xpath('//*[@id="home-container"]/div/div[1]/div')
        actual_header_message_ribbon = header_message_ribbon.text
        return actual_header_message_ribbon

    # Find and return footer copyright text
    @property
    def get_footer_copyright_text(self):
        footer_copyright = self._driver.find_element_by_xpath('html/body/div[1]/div/div/div[6]/div/div[1]/div[1]')
        actual_footer_copyright_text = footer_copyright.text
        return actual_footer_copyright_text

    # Find and return footer privacy terms text
    @property
    def get_footer_privacyterms_text(self):
        footer_privacyterms = self._driver.find_element_by_xpath('html/body/div[1]/div/div/div[6]/div/div[2]/div[1]/a')
        actual_footer_privacyterms_text = footer_privacyterms.text
        return actual_footer_privacyterms_text

    # Find and return footer code of conduct text
    @property
    def get_footer_codeofconduct_text(self):
        footer_codeofconduct = self._driver.find_element_by_xpath('html/body/div[1]/div/div/div[6]/div/div[3]/div[1]/a')
        actual_footer_codeofconduct_text = footer_codeofconduct.text
        return actual_footer_codeofconduct_text

    # Find and return footer phone number
    @property
    def get_footer_phonenumber_text(self):
        footer_phonenumber = self._driver.find_element_by_xpath('html/body/div[1]/div/div/div[6]/div/div[1]/div[2]/a')
        actual_footer_phonenumber_text = footer_phonenumber.text
        return actual_footer_phonenumber_text

    # Find and return footer email
    @property
    def get_footer_serviceemail_text(self):
        footer_serviceemail = self._driver.find_element_by_xpath('html/body/div[1]/div/div/div[6]/div/div[2]/div[2]/a')
        actual_footer_serviceemail_text = footer_serviceemail.text
        return actual_footer_serviceemail_text
