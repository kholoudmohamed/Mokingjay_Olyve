import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.HomePage import HomePage
from builtins import classmethod
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class HomePageTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        # create a new Chrome session and maximize the window
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

        # Open Olyve website
        cls.driver.get("https://test@olyveinc.com:k0sh@ry1@olyve.olyveinc.com")

        # Wait till the Home page is loaded
        locator = "html/body/div/div/div/div[1]/nav/div[1]/div[2]/a/img"
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

    # Check that Olyve Facebook icon is clickable and direct the user to Olyve Facebook Page
    def test_facebook_social_info(self):
        try:
            # Instance from homepage class
            homepage = HomePage(self.driver)

            # Variables
            locator1 = ".//*[@id='home-container']/div/div[4]/div/div/div/div[5]/a/div/img"
            locator2 = ".//*[@id='u_0_b']/div/div/div/div/div/ul/li[1]/a/div"

            # Wait till home page is loaded before clicking on Facebook link
            if homepage.home_page_load_special(40, By.XPATH, locator1):
                # Call the facebook_social_info function
                homepage.facebook_social_info()
                # Wait till home page is loaded after clicking on Facebook link
                self.driver.implicitly_wait(10)
                # Switch to the newly opened window
                self.driver.switch_to.window(self.driver.window_handles[1])
                # Make sure the newly opened window is loaded in order to get the URL
                if homepage.home_page_load_special(40,By.XPATH, locator2):
                    url_name = self.driver.current_url
                    # Verify that the URL of the newly opened page is the URL of Olyve Facebook Social Link
                    self.assertEqual('https://www.facebook.com/OlyveFlowers/', url_name, "Error in asserting the Facebook link")
        except:
            raise Exception("Facebook link not correct")

    # Check that Olyve Instgram icon is clickbale and direct the user to Olyve Instgram Page
    def test_instgram_social_info(self):
        try:
            # Instance from homepage class
            homepage = HomePage(self.driver)

            # Variables
            locator1 = ".//*[@id='home-container']/div/div[4]/div/div/div/div[5]/a/div/img"
            locator2 = ".//*[@id='react-root']/section/main/article/header/div[2]/div[1]/span/button"

            # Wait till home page is loaded before clicking on Instgram link
            if homepage.home_page_load_special(40, By.XPATH, locator1):
                # Call the instgram_social_info function
                homepage.instgram_social_info()
                # Wait till home page is loaded after clicking on Instgram link
                self.driver.implicitly_wait(30)
                # Switch to the newly opened window
                self.driver.switch_to.window(self.driver.window_handles[1])
                # Make sure the newly opened window is loaded in order to get the URL
                if homepage.home_page_load_special(40,By.XPATH, locator2):
                    url_name = self.driver.current_url
                    # Verify that the URL of the newly opened page is the URL of Olyve Instgram Social Link
                    self.assertEqual('https://www.instagram.com/olyveflowers/', self.driver.current_url, "Error in asserting the Instgram link")
        except:
            raise Exception("Instgram link not correct")

    # Check that Olyve Pinterest icon is clickbale and direct the user to Olyve Pinterest Page
    def test_pinterest_social_info(self):
        try:
            # Instance from homepage class
            homepage = HomePage(self.driver)

            # Variables
            locator1 = ".//*[@id='home-container']/div/div[4]/div/div/div/div[5]/a/div/img"
            locator2 = "html/body/div[1]/div[1]/div/div[2]/div[2]"

            # Wait till home page is loaded before clicking on Pinterest link
            if homepage.home_page_load_special(40, By.XPATH, locator1):
                # Call the pinterest_social_info function
                homepage.pinterest_social_info()
                # Wait till home page is loaded after clicking on Pinterest link
                self.driver.implicitly_wait(20)
                # Switch to the newly opened window
                self.driver.switch_to.window(self.driver.window_handles[1])
                # Make sure the newly opened window is loaded in order to get the URL
                if homepage.home_page_load_special(40,By.XPATH, locator2):
                    url_name = self.driver.current_url
                    # Verify that the URL of the newly opened page is the URL of Olyve Pinterest Social Link
                    self.assertEqual('https://www.pinterest.com/olyveflowers', self.driver.current_url, "Error in asserting the Pinterest link")
        except:
            raise Exception("Pinterest link not correct")

    # Check that Olyve Twitter icon is clickbale and direct the user to Olyve Twitter Page
    def test_twitter_social_info(self):
        try:
            # Instance from homepage class
            homepage = HomePage(self.driver)

            # Variables
            locator1 = ".//*[@id='home-container']/div/div[4]/div/div/div/div[5]/a/div/img"
            locator2 = ".//*[@id='page-container']/div[1]/div/div[1]/div[2]/div[1]/div/a/img"

            # Wait till home page is loaded before clicking on Twitter link
            if homepage.home_page_load_special(40, By.XPATH, locator1):
                # Call the twitter_social_info function
                homepage.twitter_social_info()
                # Wait till home page is loaded after clicking on Twitter link
                self.driver.implicitly_wait(20)
                # Switch to the newly opened window
                self.driver.switch_to.window(self.driver.window_handles[1])
                # Make sure the newly opened window is loaded in order to get the URL
                if homepage.home_page_load_special(40,By.XPATH, locator2):
                    url_name = self.driver.current_url
                    # Verify that the URL of the newly opened page is the URL of Olyve Twitter Social Link
                    self.assertEqual('https://twitter.com/olyveflowers', self.driver.current_url, "Error in asserting the Twitter link")
        except:
            raise Exception("Twitter link not correct")

    @classmethod
    def tearDown(cls):
        # close the browser window
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()