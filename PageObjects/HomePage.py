from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class HomePage:
    def __init__(self, driver):
        self._driver = driver

        # All home page variables
        global header_olyve_logo
        header_olyve_logo = self._driver.find_element_by_xpath('html/body/div[1]/div/olv-header/nav/div[1]/div[2]/a/img')
        global header_shop_button
        header_shop_button = self._driver.find_element_by_xpath('html/body/div[1]/div/olv-header/nav/div[1]/div[1]/ul/li/a')
        global header_track_button
        header_track_button = self._driver.find_element_by_xpath('html/body/div[1]/div/olv-header/nav/div[1]/div[4]/ul/li/a')
        global header_message_ribbon
        header_message_ribbon = self._driver.find_element_by_xpath('html/body/div[1]/div/div/div[1]/div')
        global first_products_slide
        first_products_slide = self._driver.find_element_by_xpath('//*[@id="products-slider"]/div/div/ol/li[1]')
        global second_products_slide
        second_products_slide = self._driver.find_element_by_xpath('//*[@id="products-slider"]/div/div/ol/li[2]')
        global third_products_slide
        third_products_slide = self._driver.find_element_by_xpath('//*[@id="products-slider"]/div/div/ol/li[3]')
        global shop_bottn_second_slide
        shop_bottn_second_slide = self._driver.find_element_by_xpath('//*[@id="products-slider"]/div/div/div/div[2]/div/a')
        global shop_bottn_third_slide
        shop_bottn_third_slide = self._driver.find_element_by_xpath('//*[@id="products-slider"]/div/div/div/div[3]/div/a')
        global footer_copyright
        footer_copyright = self._driver.find_element_by_xpath('html/body/div[1]/div/olv-footer/div/div[1]/div[1]')
        global footer_privacyterms
        footer_privacyterms = self._driver.find_element_by_xpath('html/body/div[1]/div/olv-footer/div/div[2]/div[1]/a')
        global footer_codeofconduct
        footer_codeofconduct = self._driver.find_element_by_xpath('html/body/div[1]/div/olv-footer/div/div[3]/div[1]/a')
        global footer_phonenumber
        footer_phonenumber = self._driver.find_element_by_xpath('html/body/div[1]/div/olv-footer/div/div[1]/div[2]/a')
        global footer_serviceemail
        footer_serviceemail = self._driver.find_element_by_xpath('html/body/div[1]/div/olv-footer/div/div[2]/div[2]/a')

    # explicit wait until presence of configurable element
    def home_page_load(self, time_to_wait, by_method, locator):
        element = WebDriverWait(self._driver, time_to_wait).until(EC.presence_of_element_located((by_method, locator)))

    # explicit wait until presence of configurable element with return as conditional action dependency
    def home_page_load_special(self, time_to_wait, by_method, locator):
        element = WebDriverWait(self._driver, time_to_wait).until(EC.presence_of_element_located((by_method, locator)))
        return True

    # Check if Olyve logo is displayed
    @property
    def is_logo_displayed(self):
        return header_olyve_logo.is_displayed()

    # Check if header shop button is enabled
    @property
    def is_header_shop_button_enabled(self):
        return header_shop_button.is_enabled()

    # Check if Track button is enabled
    @property
    def is_header_track_button_enabled(self):
        return header_track_button.is_enabled()

    # Return header ribbon message
    @property
    def get_header_ribbon_message(self):
        actual_header_message_ribbon = header_message_ribbon.text
        return actual_header_message_ribbon

    # click on a first slide and return it
    def click_on_first_slide(self):
        first_products_slide.click()
        return first_products_slide

    # click on a second slide and return it
    def click_on_second_slide(self):
        second_products_slide.click()
        return second_products_slide

    # click on a third slide and return it
    def click_on_third_slide(self):
        third_products_slide.click()
        return third_products_slide

    # Verify slides class tag contains "active"
    def verify_slide_is_active(self,selected_slide):
        slide_class = selected_slide.get_attribute('class')
        active_class = "ng-scope active"
        if active_class == slide_class:
            return True
        else:
            return False

    # Return footer copyright text
    @property
    def get_footer_copyright_text(self):
        actual_footer_copyright_text = footer_copyright.text
        return actual_footer_copyright_text

    # Return footer privacy terms text
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

    # Return footer code of conduct text
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

    # Return footer phone number
    @property
    def get_footer_phonenumber_text(self):
        actual_footer_phonenumber_text = footer_phonenumber.text
        return actual_footer_phonenumber_text

    # Verify phone number tag contains "tel:"
    @property
    def verify_phonenumber_href(self):
        phonenumber_href = footer_phonenumber.get_attribute('href')
        phonenumber = "tel:"
        if phonenumber in phonenumber_href:
            return True
        else:
            return False

    # Return footer email
    @property
    def get_footer_serviceemail_text(self):
        actual_footer_serviceemail_text = footer_serviceemail.text
        return actual_footer_serviceemail_text

    # Verify service mail tag contains "mailto:"
    @property
    def verify_serviceamil_href(self):
        servicemail_href = footer_serviceemail.get_attribute('href')
        servicemail = "mailto:"
        if servicemail in servicemail_href:
            return True
        else:
            return False

    # Click on Facebook icon in Olyve Home Page
    def facebook_social_info(self):
        # Create an Instance from ActionChains
        action = ActionChains(self._driver)
        # Find the Facebook link in the home page then click on the link found
        facebook_link = self._driver.find_element_by_xpath("html/body/div[1]/div/olv-social/div/div[2]/div/a[1]")
        # The below steps are used to open the facebook_link in a new window instead of a new tab
        action.key_down(Keys.SHIFT)
        action.click(facebook_link)
        action.key_up(Keys.SHIFT)
        action.perform()

    # Click on Instgram icon in Olyve Home Page
    def instgram_social_info(self):
        # Create an Instance from ActionChains
        action = ActionChains(self._driver)
        # Find the Instgram link in the home page then click on it
        instgram_link = self._driver.find_element_by_xpath("html/body/div[1]/div/olv-social/div/div[2]/div/a[2]/i")
        # The below steps are used to open the facebook_link in a new window instead of a new tab
        action.key_down(Keys.SHIFT)
        action.click(instgram_link)
        action.key_up(Keys.SHIFT)
        action.perform()

    # Click on Pinterest icon in Olyve Home Page
    def pinterest_social_info(self):
        # Create an Instance from ActionChains
        action = ActionChains(self._driver)
        # Find the Pinterest link in the home page then click on it
        pinterest_link = self._driver.find_element_by_xpath("html/body/div[1]/div/olv-social/div/div[2]/div/a[3]/i")
        # The below steps are used to open the facebook_link in a new window instead of a new tab
        action.key_down(Keys.SHIFT)
        action.click(pinterest_link)
        action.key_up(Keys.SHIFT)
        action.perform()

    # Click on Twitter icon in Olyve Home Page
    def twitter_social_info(self):
        # Create an Instance from ActionChains
        action = ActionChains(self._driver)
        # Find the Twitter link in the home page then click on it
        twitter_link = self._driver.find_element_by_xpath("html/body/div[1]/div/olv-social/div/div[2]/div/a[4]/i")
        # The below steps are used to open the facebook_link in a new window instead of a new tab
        action.key_down(Keys.SHIFT)
        action.click(twitter_link)
        action.key_up(Keys.SHIFT)
        action.perform()

    def findproductandclick(self, x):
        try:
            res = []
            elem = WebDriverWait(driver=self._driver, timeout=5).until(
                EC.presence_of_all_elements_located(locator=(By.CLASS_NAME, "name")))
            res.append(elem[x].text)
            product_link = self._driver.find_element_by_link_text(elem[x].text)
            product_link.click()
        except:
            raise Exception("Product Not Found")

    def get_product_count(self):
        elem = WebDriverWait(driver=self._driver, timeout=5).until(EC.presence_of_all_elements_located(locator=(By.CLASS_NAME, "name")))
        prod_count = len(elem)
        return prod_count