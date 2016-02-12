import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.HomePage import HomePage
from builtins import classmethod
from selenium.webdriver.common.by import By
import http.client
import requests as req
import time


class HomePageTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        # create a new Chrome session and maximize the window
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

        # Open Olyve website
        cls.driver.get("https://test@olyveinc.com:k0sh@ry1@olyve.olyveinc.com")

        # Wait till the Home page is loaded
        locator = "html/body/div[1]/div/div/div[1]/nav/div[1]/div[2]/a/img"
        homepage = HomePage(cls.driver)
        homepage.home_page_load(40, By.XPATH, locator)

    # The following test case verifies header items(logo, shop button, track button and ribbon message).
    def test_header_items(self):
        try:
            homepage = HomePage(self.driver)
            self.assertEqual(True, homepage.is_logo_displayed)
            self.assertEqual(True, homepage.is_header_shop_button_enabled)
            self.assertEqual(True, homepage.is_header_track_button_enabled)

            expected_header_message_ribbon = "GIFT BOX & DELIVERY ALWAYS INCLUDED"
            self.assertEqual(expected_header_message_ribbon, homepage.get_header_ribbon_message)

        except:
            raise Exception("Header Assertions Failed")

    # Assert navigating between products slides
    def test_navigating_between_products_slide(self):
        try:
            homepage = HomePage(self.driver)
            selected_slide = homepage.click_on_second_slide()
            self.assertEqual(True, homepage.verify_slide_is_active(selected_slide), "Second Slide is not active")

            self.driver.implicitly_wait(20)
            selected_slide = homepage.click_on_third_slide()
            self.assertEqual(True, homepage.verify_slide_is_active(selected_slide), "Third Slide is not active")

            self.driver.implicitly_wait(30)
            selected_slide = homepage.click_on_first_slide()
            self.driver.implicitly_wait(5)
            self.assertEqual(True, homepage.verify_slide_is_active(selected_slide), "First Slide is not active")

        except:
            raise Exception("There is an issue in navigating between the slides")

    # The following test case verifies footer items(copyright text, privacy terms, conde of conduct, phone number and email).
    def test_footer_items_text(self):
        try:
            homepage = HomePage(self.driver)

            # [Kholoud - 8Feb2016] expected footer text and expected url's hardcoded till finding another way to capture it.
            expected_footer_copyright_text = "Copyright 2015, Olyve, Inc."
            expected_footer_privacyterms_text = "Privacy Terms"
            expected_footer_codeofconducts_text = "Code Of Conduct"
            expected_footer_phonenumber_text = "844-35-OLYVE"
            expected_footer_servicemail_text = "Service@olyve.com"

            # Footer text assertions
            self.assertEqual(expected_footer_copyright_text,homepage.get_footer_copyright_text)
            self.assertEqual(expected_footer_privacyterms_text,homepage.get_footer_privacyterms_text)
            self.assertEqual(expected_footer_codeofconducts_text,homepage.get_footer_codeofconduct_text)
            self.assertEqual(expected_footer_phonenumber_text,homepage.get_footer_phonenumber_text)
            self.assertEqual(expected_footer_servicemail_text,homepage.get_footer_serviceemail_text)

        except:
            raise Exception("Footer Text Assertions Failed")

    # Test privacy terms navigation
    def test_footer_privacyterms_navigation(self):
        try:
            homepage = HomePage(self.driver)
            expected_privacyterms_url = "https://test%40olyveinc.com:k0sh%40ry1@olyve.olyveinc.com/privacy"
            self.assertEqual(expected_privacyterms_url,homepage.get_privacyterms_url)

        except:
            raise Exception("Privacy Terms Navigation Failed")

    # Test code of conduct navigation
    def test_footer_codeofconduct_navigtion(self):
        try:
            homepage = HomePage(self.driver)
            expected_codeofconduct_url = "https://test%40olyveinc.com:k0sh%40ry1@olyve.olyveinc.com/codeofconduct"
            self.assertEqual(expected_codeofconduct_url,homepage.get_codeofconduct_url)

        except:
            raise Exception("Privacy Terms Navigation Failed")

    # check that phone number can be called by clicking on it.
    def test_assert_phonenumber_href(self):
        try:
            homepage = HomePage(self.driver)
            self.assertEqual(True,homepage.verify_phonenumber_href)

        except:
            raise Exception ("Phone number href is not correct")

    # check that service email can be used to send email by clicking on it
    def test_assert_servicemail_href(self):
        try:
            homepage = HomePage(self.driver)
            self.assertEqual(True,homepage.verify_serviceamil_href)

        except:
            raise Exception ("Service email href is not correct")

    def test_facebook_social_info(self):
        try:
            # Instance from homepage class
            homepage = HomePage(self.driver)
            homepage.facebook_social_info()

            # Switch focus to the new tab
            main_window = self.driver.current_window_handle
            self.driver.switch_to.window(main_window)

            locator = "//*[@id='blueBarDOMInspector']/div/div/div[1]/div/div[1]/a/i"
            homepage.home_page_load(20, By.XPATH, locator)

           # self.assertEqual("https://www.facebook.com/olyveflowers?_rdr=p", self.driver.current_url,"Not My link")
        except:
            raise Exception("Facebook link not correct")

    def test_instgram_social_info(self):
        try:
            # Instance from homepage class
            homepage = HomePage(self.driver)
            # Call the instgram_social_info function
            self.assertEqual("https://www.instagram.com/olyveflowers/", homepage.instgram_social_info(),"Instgram link not correct")
        except:
            raise Exception("Instgram link not correct")

    def test_pinterest_social_info(self):
        try:
            # Instance from homepage class
            homepage = HomePage(self.driver)
            # Call the pinterest_social_info function
            self.assertEqual("https://www.pinterest.com/olyveflowers/", homepage.pinterest_social_info(),"Pinterest link not correct")
        except:
            raise Exception("Pinterest link not correct")

    def test_twitter_social_info(self):
        try:
            # Instance from homepage class
            homepage = HomePage(self.driver)
            # Call the twitter_social_info function
            self.assertEqual("https://twitter.com/olyveflowers", homepage.twitter_social_info(),"Twitter link not correct")
        except:
            raise Exception("Twitter link not correct")

    @classmethod
    def tearDown(cls):
        # close the browser window
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
