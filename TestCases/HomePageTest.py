import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.HomePage import HomePage
from builtins import classmethod
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PageObjects.ExcelDataReader import DataReader
import xlrd
import time


class HomePageTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        # create a new Chrome session and maximize the window
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

        # Open Olyve website
        cls.driver.get("https://test@olyveinc.com:Amr<3skype@olyve.olyveinc.com")

        # Wait till the Home page is loaded
        locator = "html/body/div/div/olv-header/nav/div[1]/div[2]/a/img"
        homepage = HomePage(cls.driver)
        homepage.home_page_load(40, By.XPATH, locator)

    # The following test case verifies header items(logo, shop button, track button and ribbon message).
    def test_header_items(self):
        try:
            homepage = HomePage(self.driver)
            self.assertEqual(True, homepage.is_logo_displayed)
            self.assertEqual(True, homepage.is_header_shop_button_enabled)
            self.assertEqual(True, homepage.is_header_track_button_enabled)

            # Fetch the expected header from the excel sheet
            expected_header_message_ribbon = DataReader.get_data("Home", 1, 1)
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

    # The following test case verifies footer items(copyright text, privacy terms, code of conduct, phone number and email).
    def test_footer_items_text(self):
        try:
            homepage = HomePage(self.driver)

            # Fetch All the text values from the excel sheet
            expected_footer_copyright_text = DataReader.get_data("Home", 2, 1)
            expected_footer_privacyterms_text = DataReader.get_data("Home", 3, 1)
            expected_footer_codeofconducts_text = DataReader.get_data("Home", 4, 1)
            expected_footer_phonenumber_text = DataReader.get_data("Home", 5, 1)
            expected_footer_servicemail_text = DataReader.get_data("Home", 6, 1)

            # Footer text assertions
            self.assertEqual(expected_footer_copyright_text, homepage.get_footer_copyright_text)
            self.assertEqual(expected_footer_privacyterms_text, homepage.get_footer_privacyterms_text)
            self.assertEqual(expected_footer_codeofconducts_text, homepage.get_footer_codeofconduct_text)
            self.assertEqual(expected_footer_phonenumber_text, homepage.get_footer_phonenumber_text)
            self.assertEqual(expected_footer_servicemail_text, homepage.get_footer_serviceemail_text)

        except:
            raise Exception("Footer Text Assertions Failed")

    # Test privacy terms navigation
    def test_footer_privacyterms_navigation(self):
        try:
            homepage = HomePage(self.driver)
            expected_privacyterms_url = "https://olyve.olyveinc.com/privacy"
            self.assertEqual(expected_privacyterms_url, homepage.get_privacyterms_url)
            self.assertTrue(expected_privacyterms_url in homepage.get_privacyterms_url)

        except:
            raise Exception("Privacy Terms Navigation Failed")

    # Test code of conduct navigation
    def test_footer_codeofconduct_navigtion(self):
        try:
            homepage = HomePage(self.driver)
            expected_codeofconduct_url = "https://olyve.olyveinc.com/codeofconduct"
            self.assertEqual(expected_codeofconduct_url, homepage.get_codeofconduct_url)

        except:
            raise Exception("Privacy Terms Navigation Failed")

    # check that phone number can be called by clicking on it.
    def test_assert_phonenumber_href(self):
        try:
            homepage = HomePage(self.driver)
            self.assertEqual(True, homepage.verify_phonenumber_href)

        except:
            raise Exception ("Phone number href is not correct")

    # check that service email can be used to send email by clicking on it
    def test_assert_servicemail_href(self):
        try:
            homepage = HomePage(self.driver)
            self.assertEqual(True, homepage.verify_serviceamil_href)

        except:
            raise Exception ("Service email href is not correct")

    # Check that Olyve Facebook icon is clickable and direct the user to Olyve Facebook Page
    def test_facebook_social_info(self):
        try:
            # Instance from homepage class
            homepage = HomePage(self.driver)

            # Variables
            locator1 = "html/body/div/div/div/div[4]/div/div/div/div[5]/a/olv-image/div/img"
            locator2 = "pagelet_bluebar"

            # Wait till home page is loaded before clicking on Facebook link
            if homepage.home_page_load_special(40, By.XPATH, locator1):
                # Call the facebook_social_info function
                homepage.facebook_social_info()
                # Wait till home page is loaded after clicking on Facebook link
                self.driver.implicitly_wait(10)
                # Switch to the newly opened window
                self.driver.switch_to.window(self.driver.window_handles[1])
                # Make sure the newly opened window is loaded in order to get the URL
                if homepage.home_page_load_special(40, By.ID, locator2):
                    url_name = self.driver.current_url
                    # Verify that the URL of the newly opened page is the URL of Olyve Facebook Social Link
                    self.assertEqual(DataReader.get_data('Home', 7, 1), url_name, "Error in asserting the Facebook link")
        except:
            raise Exception("Facebook link not correct")

    # Check that Olyve Instgram icon is clickbale and direct the user to Olyve Instgram Page
    def test_instgram_social_info(self):
        try:
            # Instance from homepage class
            homepage = HomePage(self.driver)

            # Variables
            locator1 = "html/body/div/div/div/div[4]/div/div/div/div[5]/a/olv-image/div/img"
            locator2 = ".//*[@id='react-root']/section/main/article/header/div[2]/div[1]/span/button"

            # Wait till home page is loaded before clicking on Instgram link
            if homepage.home_page_load_special(40, By.XPATH, locator1):
                # Call the instgram_social_info function
                homepage.instgram_social_info()
                # Wait till home page is loaded after clicking on Instgram link
                self.driver.implicitly_wait(40)
                # Switch to the newly opened window
                self.driver.switch_to.window(self.driver.window_handles[1])
                # Make sure the newly opened window is loaded in order to get the URL
                if homepage.home_page_load_special(40,By.XPATH, locator2):
                    url_name = self.driver.current_url
                    # Verify that the URL of the newly opened page is the URL of Olyve Instgram Social Link
                    self.assertEqual(DataReader.get_data('Home', 8, 1), self.driver.current_url, "Error in asserting the Instgram link")
        except:
            raise Exception("Instgram link not correct")

    # Check that Olyve Pinterest icon is clickbale and direct the user to Olyve Pinterest Page
    def test_pinterest_social_info(self):
        try:
            # Instance from homepage class
            homepage = HomePage(self.driver)

            # Variables
            locator1 = "html/body/div/div/div/div[4]/div/div/div/div[5]/a/olv-image/div/img"
            locator2 = "html/body/div[1]/div[3]/div[1]/div[2]/div[2]/div/div/div[3]/div/div/h1/div"

            # Wait till home page is loaded before clicking on Pinterest link
            if homepage.home_page_load_special(40, By.XPATH, locator1):
                # Call the pinterest_social_info function
                homepage.pinterest_social_info()
                # Wait till home page is loaded after clicking on Pinterest link
                self.driver.implicitly_wait(30)
                # Switch to the newly opened window
                self.driver.switch_to.window(self.driver.window_handles[1])
                # Make sure the newly opened window is loaded in order to get the URL
                if homepage.home_page_load_special(40,By.XPATH, locator2):
                    url_name = self.driver.current_url
                    # Verify that the URL of the newly opened page is the URL of Olyve Pinterest Social Link
                    self.assertEqual(DataReader.get_data('Home', 9, 1), self.driver.current_url, "Error in asserting the Pinterest link")
        except:
            raise Exception("Pinterest link not correct")

    # Check that Olyve Twitter icon is clickbale and direct the user to Olyve Twitter Page
    def test_twitter_social_info(self):
        try:
            # Instance from homepage class
            homepage = HomePage(self.driver)

            # Variables
            locator1 = "html/body/div/div/div/div[4]/div/div/div/div[5]/a/olv-image/div/img"
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
                    self.assertEqual(DataReader.get_data('Home', 10, 1), self.driver.current_url, "Error in asserting the Twitter link")
        except:
            raise Exception("Twitter link not correct")

    def test_go_to_product(self):
        homepage = HomePage(self.driver)

        # Get the number of products
        for Index in range(0, homepage.get_product_count()):
            homepage.findproductandclick(Index)
            self.driver.implicitly_wait(20)

            # Following locator is for Pick Me button.
            locator3 = "html/body/div[1]/div/div/div[2]/div[2]/div[5]/div/div"
            if homepage.home_page_load_special(40, By.XPATH, locator3):
                url_name = self.driver.current_url
                url_name_from_excel = DataReader.get_data("Products", Index+1, 1)
                self.assertEqual(url_name, url_name_from_excel)
            self.driver.back()
            self.driver.refresh()
            self.driver.implicitly_wait(5)

    @classmethod
    def tearDown(cls):
        # close the browser window
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
