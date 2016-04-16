import unittest
from builtins import classmethod
from PageObjects.HomePage import HomePage
from Utilities import FileLocator
from Utilities.Browser import Browser
from Utilities.PageActions import BasicActions
from Utilities.ExcelDataReader import ExcelDataReader
from Configurations import ConfigReader


class HomePageTest(unittest.TestCase):

    # Get the file location of the Excel Input File
    _fileLocation = FileLocator.read_config_get_file_location('ExcelConfiguration', 'DataSourcefileLocation')

    # In the Configuration File with the Key 'ExcelConfiguration' - Sheet Name 'HomeSheetName'
    home_sheetName = ConfigReader.readconfig('ExcelConfiguration', 'HomeSheetName')
    # Fill the result of the selected sheet in the 2 dimensional array with the values in 'HomeSheetName'
    Homeresult = ExcelDataReader.get_data(_fileLocation, home_sheetName, HDR=True)

    # In the Configuration File with the Key 'ExcelConfiguration' - Sheet Name 'ProductsSheetName'
    product_sheetName = ConfigReader.readconfig('ExcelConfiguration', 'ProductsSheetName')
    # Fill the result of the selected sheet in the 2 dimensional array with the values in 'ProductsSheetName'
    Productresult = ExcelDataReader.get_data(_fileLocation, product_sheetName, HDR=True)

    @classmethod
    def setUp(cls):

        # create a new Browser session and maximize the window
        Browser.initialize_driver()  # default FireFox
        BasicActions.maximize_window()

        # Go to Olyve Home Page URL
        BasicActions.navigate(ConfigReader.readconfig('ConfigurationSettings', 'OlyveHomeURL'))

        # Wait till the Home page is loaded
        homepage = HomePage(Browser._driver)
        homepage.wait_for_header_olyve_logo()

    # The following test case verifies that Olyve logo is displayed, all header buttons are enabled and Ribbon Message Text is correct.
    def test_header_items(self):
        try:
            homepage = HomePage(Browser._driver)

            self.assertTrue(homepage.is_logo_displayed(), "Olyve Header Logo is not displayed")
            self.assertTrue(homepage.is_header_shop_button_enabled(), "Header Shop Button is not enabled")
            self.assertTrue(homepage.is_header_fromourcustomers_button_enabled(), "Header From Our Customers Button is not enabled")
            self.assertTrue(homepage.is_header_theolyveexperience_button_enabled(), "Header The Olyve Experience Button is not enabled")
            self.assertTrue(homepage.is_header_track_button_enabled(), "Header Track Button is not enabled")
            self.assertTrue(homepage.is_header_service_button_enabled(), "Header Service Button is not enabled")
            self.assertTrue(homepage.is_header_workshops_button_enabled(), "Header Workshops Button is not enabled")
            self.assertTrue(homepage.is_header_social_button_enabled(), "Header Social Button is not enabled")

            # Fetch the expected header from the excel sheet
            expected_header_message_ribbon = self.Homeresult[1][0]
            self.assertEqual(expected_header_message_ribbon, homepage.get_header_ribbon_message(), "Header Ribbon Message is not correct")

        except:
            raise Exception("Header Assertions Failed")

    # The following test case verifies the functionality of the Header items when clickec
    def test_shop_button_click(self):
        homepage = HomePage(Browser._driver)
        self.assertTrue(homepage.shop_button_click(), "By clicking on the Header Shop button, the user was not navigated to Products")

    def test_olyve_exprience_button_click(self):
        homepage = HomePage(Browser._driver)
        self.assertEqual(self.Homeresult[1][12], homepage.olyve_experience_button_click(), "Error in asserting the From Our Customer Page")

    def test_from_our_customer_button_click(self):
        homepage = HomePage(Browser._driver)
        self.assertEqual(self.Homeresult[1][13], homepage.from_our_customer_button_click(), "Error in asserting the From Our Customer Page")

    def test_track_button_click(self):
        homepage = HomePage(Browser._driver)
        self.assertEqual(self.Homeresult[1][14], homepage.track_button_click(self.Homeresult[1][15]), "Error in asserting the Track Page")

    def test_service_button_click(self):
        homepage = HomePage(Browser._driver)
        self.assertEqual(self.Homeresult[1][16], homepage.service_button_click(self.Homeresult[1][15], self.Homeresult[1][17]), "Error in asserting the Service Page")

    def test_workshop_button_click(self):
        homepage = HomePage(Browser._driver)
        self.assertEqual(self.Homeresult[1][18], homepage.workshop_button_click(), "Error in asserting the Workshop Page")

    def test_social_button_click(self):
        homepage = HomePage(Browser._driver)
        self.assertTrue(homepage.social_button_click(), "By clicking on the Social button, the user was not navigated to Social links")

    def test_shop_button_second_slide_click(self):
        homepage = HomePage(Browser._driver)
        selected_slide = homepage.click_on_second_slide()
        if homepage.verify_slide_is_active(selected_slide)== True:
            homepage.shop_button_second_slide_click()
            BasicActions.implicit_wait(40)
            # Switch to the newly opened window
            Browser._driver.switch_to.window(Browser._driver.window_handles[1])
            # Make sure the newly opened window is loaded in order to get the URL
            if homepage.wait_for_instgram_page_load():
                url_name = Browser._driver.current_url
                # Verify that the URL of the newly opened page is the URL of Olyve Instgram Social Link
                self.assertEqual(self.Homeresult[1][7], Browser._driver.current_url, "Error in asserting the Instgram link")

    def test_shop_button_third_slide_click(self):
        homepage = HomePage(Browser._driver)
        selected_slide = homepage.click_on_third_slide()
        if homepage.verify_slide_is_active(selected_slide) == True:
            self.assertTrue(homepage.shop_button_third_slide_click(), "By clicking on the Shop button of the third slide, the user was not navigated to Products")

    # The following test case verifies navigating between products slides
    def test_navigating_between_products_slide(self):
        try:

            homepage = HomePage(Browser._driver)
            selected_slide = homepage.click_on_second_slide()
            self.assertTrue(homepage.verify_slide_is_active(selected_slide), "Second Slide is not active")

            BasicActions.implicit_wait(20)
            selected_slide = homepage.click_on_third_slide()
            self.assertTrue(homepage.verify_slide_is_active(selected_slide), "Third Slide is not active")

            BasicActions.implicit_wait(30)
            selected_slide = homepage.click_on_first_slide()
            BasicActions.implicit_wait(5)
            self.assertTrue(homepage.verify_slide_is_active(selected_slide), "First Slide is not active")

        except:
            raise Exception("There is an issue in navigating between the slides")

    # The following test case verifies footer items(copyright text, privacy terms, code of conduct, phone number and email)
    def test_footer_items_text(self):
        try:
            homepage = HomePage(Browser._driver)

            # Footer text assertions
            self.assertEqual(self.Homeresult[1][1], homepage.get_footer_copyright_text())
            self.assertEqual(self.Homeresult[1][2], homepage.get_footer_privacyterms_text())
            self.assertEqual(self.Homeresult[1][3], homepage.get_footer_codeofconduct_text())
            self.assertEqual(self.Homeresult[1][4], homepage.get_footer_phonenumber_text())
            self.assertEqual(self.Homeresult[1][5], homepage.get_footer_serviceemail_text())

        except:
            raise Exception("Footer Text Assertions Failed")

    # The following test case verifies the privacy terms navigation
    def test_footer_privacyterms_navigation(self):
        try:
            homepage = HomePage(Browser._driver)
            self.assertEqual(self.Homeresult[1][11], homepage.get_privacyterms_url())

        except:
            raise Exception("Privacy Terms Navigation Failed")

    # The following test case verifies the code of conduct navigation
    def test_footer_codeofconduct_navigtion(self):
        try:
            homepage = HomePage(Browser._driver)
            self.assertEqual(self.Homeresult[1][10], homepage.get_codeofconduct_url())

        except:
            raise Exception("Privacy Terms Navigation Failed")

    # The following test case verifies that phone number can be called by clicking on it.
    def test_assert_phonenumber_href(self):
        try:
            homepage = HomePage(Browser._driver)
            self.assertTrue(homepage.verify_phonenumber_href())

        except:
            raise Exception ("Phone number href is not correct")

    # The following test case verifies that service email can be used to send email by clicking on it
    def test_assert_servicemail_href(self):
        try:
            homepage = HomePage(Browser._driver)
            self.assertTrue(homepage.verify_serviceamil_href())

        except:
            raise Exception ("Service email href is not correct")

    # The following test case verifies that Olyve Facebook icon is clickable and direct the user to Olyve Facebook Page
    def test_facebook_social_info(self):
        try:
            # Instance from homepage class
            homepage = HomePage(Browser._driver)
            # Wait till home page is loaded before clicking on Facebook link
            if homepage.wait_for_product_image_load():
                # Call the facebook_social_info function
                homepage.facebook_social_info()
                # Wait till home page is loaded after clicking on Facebook link
                BasicActions.implicit_wait(10)
                # Switch to the newly opened window
                Browser._driver.switch_to.window(Browser._driver.window_handles[1])
                # Make sure the newly opened window is loaded in order to get the URL
                if homepage.wait_for_facebook_page_load():
                    url_name = Browser._driver.current_url
                    # Verify that the URL of the newly opened page is the URL of Olyve Facebook Social Link
                    self.assertEqual(self.Homeresult[1][6], url_name, "Error in asserting the Facebook link")
        except:
            raise Exception("Facebook link not correct")

    # The following test case verifies that Olyve Instgram icon is clickbale and direct the user to Olyve Instgram Page
    def test_instgram_social_info(self):
        try:
            # Instance from homepage class
            homepage = HomePage(Browser._driver)
            # Wait till home page is loaded before clicking on Instgram link
            if homepage.wait_for_product_image_load():
                # Call the instgram_social_info function
                homepage.instgram_social_info()
                # Wait till home page is loaded after clicking on Instgram link
                BasicActions.implicit_wait(40)
                # Switch to the newly opened window
                Browser._driver.switch_to.window(Browser._driver.window_handles[1])
                # Make sure the newly opened window is loaded in order to get the URL
                if homepage.wait_for_instgram_page_load():
                    url_name = Browser._driver.current_url
                    # Verify that the URL of the newly opened page is the URL of Olyve Instgram Social Link
                    self.assertEqual(self.Homeresult[1][7], Browser._driver.current_url, "Error in asserting the Instgram link")
        except:
            raise Exception("Instgram link not correct")

    # The following test case verifies that Olyve Pinterest icon is clickbale and direct the user to Olyve Pinterest Page
    def test_pinterest_social_info(self):
        try:
            # Instance from homepage class
            homepage = HomePage(Browser._driver)
            # Wait till home page is loaded before clicking on Pinterest link
            if homepage.wait_for_product_image_load():
                # Call the pinterest_social_info function
                homepage.pinterest_social_info()
                # Wait till home page is loaded after clicking on Pinterest link
                BasicActions.implicit_wait(30)
                # Switch to the newly opened window
                Browser._driver.switch_to.window(Browser._driver.window_handles[1])
                # Make sure the newly opened window is loaded in order to get the URL
                if homepage.wait_for_pinterstet_page_load:
                    url_name = Browser._driver.current_url
                    # Verify that the URL of the newly opened page is the URL of Olyve Pinterest Social Link
                    self.assertEqual(self.Homeresult[1][8], Browser._driver.current_url, "Error in asserting the Pinterest link")
        except:
            raise Exception("Pinterest link not correct")

    # The following test case verifies that Olyve Twitter icon is clickbale and direct the user to Olyve Twitter Page
    def test_twitter_social_info(self):
        try:
            # Instance from homepage class
            homepage = HomePage(Browser._driver)
            # Wait till home page is loaded before clicking on Twitter link
            if homepage.wait_for_product_image_load():
                # Call the twitter_social_info function
                homepage.twitter_social_info()
                # Wait till home page is loaded after clicking on Twitter link
                BasicActions.implicit_wait(20)
                # Switch to the newly opened window
                Browser._driver.switch_to.window(Browser._driver.window_handles[1])
                # Make sure the newly opened window is loaded in order to get the URL
                if homepage.wait_for_twitter_page_load:
                    url_name = Browser._driver.current_url
                    # Verify that the URL of the newly opened page is the URL of Olyve Twitter Social Link
                    self.assertEqual(self.Homeresult[1][9], Browser._driver.current_url, "Error in asserting the Twitter link")
        except:
            raise Exception("Twitter link not correct")

    # The following test case verifies that all product items are loaded in the home page and they all are clickable
    def test_go_to_product(self):
        homepage = HomePage(Browser._driver)

        # Get the number of products
        for Index in range(0, homepage.get_product_count()):
            homepage.findproductandclick(Index)
            BasicActions.implicit_wait(20)
            # Wait for Product Page to load
            if homepage.wait_for_product_page():
                url_name = BasicActions.get_current_url()
                url_name_from_excel = self.Productresult[1][Index]
                self.assertEqual(url_name, url_name_from_excel)
            BasicActions.go_back()
            BasicActions.refresh_page()
            BasicActions.implicit_wait(5)

    @classmethod
    def tearDown(cls):
        # close the browser window(s)
        Browser.quit_driver()

if __name__ == '__main__':
    unittest.main()
