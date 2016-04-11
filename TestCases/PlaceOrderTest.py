import unittest
from builtins import classmethod
from PageObjects.PlaceOrder import PlaceOrder
from Utilities import FileLocator
from Utilities.Browser import Browser
from Utilities.PageActions import BasicActions
from Utilities.ExcelDataReader import ExcelDataReader
from Configurations import ConfigReader
import time


class PlaceOrderTest(unittest.TestCase):

    # Get the file location of the Excel Input File
    _fileLocation = FileLocator.read_config_get_file_location('ExcelConfiguration', 'DataSourcefileLocation')

    # In the Configuration File with the Key 'ExcelConfiguration' - Sheet Name 'OrderInfoSheetName'
    orderinfo_sheetName = ConfigReader.readconfig('ExcelConfiguration', 'OrderInfoSheetName')
    # Fill the result of the selected sheet in the 2 dimensional array with the values in 'OrderInfoSheetName'
    OrderInforesult = ExcelDataReader.get_data(_fileLocation, orderinfo_sheetName, HDR=True)

    # In the Configuration File with the Key 'ExcelConfiguration' - Sheet Name 'GeneralInfoSheetName'
    generalinfo_sheetName = ConfigReader.readconfig('ExcelConfiguration', 'GeneralInfoSheetName')
    # Fill the result of the selected sheet in the 2 dimensional array with the values in 'GeneralInfoSheetName'
    GeneralInforesult = ExcelDataReader.get_data(_fileLocation, generalinfo_sheetName, HDR=True)

    @classmethod
    def setUp(cls):
        # Create a new Browser session and maximize the window
        Browser.initialize_driver()  # default FireFox
        BasicActions.maximize_window()

        # Go to Olyve Home Page URL
        BasicActions.navigate(ConfigReader.readconfig('ConfigurationSettings','OlyveHomeURL'))

        # Wait till the Home page is loaded
        placeorder = PlaceOrder(Browser._driver)
        placeorder.wait_for_header_olyve_logo()

    # The following test case order a selected product
    def test_place_product_order(self):
        placeorder = PlaceOrder(Browser._driver)
        for row_index in range(len(self.OrderInforesult[0])):
            # Find the selected proudct and click on it
            placeorder.findproductandclick(self.OrderInforesult[0][row_index])
            # Wait till the Proudct Details page is loaded
            BasicActions.implicit_wait(50)
            if placeorder.wait_for_product_page():
                # Get Price of the Product as it will be required in the Review page
                product_price = placeorder.get_product_price()
                # Click on the Pick Me button
                placeorder.click_on_pickme_button()
                # Wait till The "WHO ARE WE DELIVERING TO" popup is displayed
                BasicActions.implicit_wait(20)
                # Fill the "WHO ARE WE DELIVERING TO" popup with data set in the input excel file
                placeorder.fill_pickme_popup(self.OrderInforesult[1][row_index], self.OrderInforesult[2][row_index])
                # Wait until the next page is opened
                if (placeorder.wait_for_accessory_page())or (placeorder.wait_for_message_page()):
                    # Get the URL of the current page
                    current_url = Browser._driver.current_url
                    # Check if the Page opened is the Accessory page
                    if current_url == self.GeneralInforesult[1][0]:
                        # Check if the user required to click on yes button if accessory is required
                        if self.OrderInforesult[3][row_index] == 'Yes':
                            # Get the Accessory Price from the page as it will be required in the Review Order Page
                            accessory_price = placeorder.get_accessory_price()
                            # Click on Yes Please button
                            placeorder.click_yesplease()
                        # Check if the user required to click on No button if accessory is not required
                        else:
                            # Set accessory price to zero in case no accessory is required
                            accessory_price = 0
                            # Click on No Thanks button
                            placeorder.click_nothanks()
                    else:
                        raise Exception("Invalid Page")
                    # Wait till the Message page is loaded
                    BasicActions.implicit_wait(30)
                    if placeorder.wait_for_message_page():
                        # Get the URL of the current page
                        current_url = Browser._driver.current_url
                        # Check if the current page is message page
                        if current_url == self.GeneralInforesult[1][1]:
                            # Fill the gift Message and Signature
                            placeorder.fill_gift_message(self.OrderInforesult[4][row_index], self.OrderInforesult[5][row_index])
                            # Upload the Photo from given location
                            placeorder.upload_photo(self.OrderInforesult[6][row_index])
                            # Upload Video from given location
                            placeorder.upload_video(self.OrderInforesult[7][row_index])
                            # Click on the Review and Checkout button
                            placeorder.click_review_and_checkout()
                            # Wait till the Checkout page is loaded
                            if placeorder.wait_for_checkout_page():
                                current_url = Browser._driver.current_url
                                if current_url == self.GeneralInforesult[1][2]:
                                        # Verified the Product Name
                                        self.assertTrue(placeorder.check_product_name(self.OrderInforesult[0][row_index]), "Product Name doesn't match the selected product name")
                                        self.assertTrue(placeorder.check_product_name_review(self.OrderInforesult[0][row_index]), "Product Name doesn't match the selected product name")
                                        # Verify the Product Price
                                        self.assertTrue(placeorder.check_product_price(product_price), "Product Price doesn't match the selected product")
                                        self.assertTrue(placeorder.check_product_price_review(product_price), "Product Price doesn't match the selected product")
                                        # Verify the Accessory Message
                                        self.assertTrue(placeorder.check_accessory_details(self.OrderInforesult[3][row_index], self.OrderInforesult[8][row_index], accessory_price),"Accessory Text or Accessory Price is not correct")
                                        self.assertTrue(placeorder.check_accessory_details_review(self.OrderInforesult[3][row_index], self.OrderInforesult[8][row_index], accessory_price),"Accessory Text or Accessory Price is not correct")
                                        # Verify the Notification Message
                                        self.assertTrue(placeorder.check_notification_text(self.OrderInforesult[9][row_index]),"Notification Text is not correct")
                                        self.assertTrue(placeorder.check_notification_text_review(self.OrderInforesult[9][row_index]),"Notification Text is not correct")
                                        # Verify the Price of the product + accessory if requested
                                        self.assertTrue(placeorder.check_subtotal(accessory_price, product_price),"Subtotal is not correct")
                                        self.assertTrue(placeorder.check_sales_taxes(self.OrderInforesult[10][row_index]),"Sales Tax is not correct")
                                        # Verify the Sales Tax on the selected Product
                                        self.assertTrue(placeorder.check_sales_taxes_review(self.OrderInforesult[10][row_index]),"Sales Tax is not correct")
                                        self.assertTrue(placeorder.check_total_price(self.OrderInforesult[10][row_index],accessory_price, product_price), "Total is not correct")
                                        # Verify the Total Price
                                        self.assertTrue(placeorder.check_total_price_review(self.OrderInforesult[10][row_index],accessory_price, product_price), "Total is not correct")
                                        # Verify the Customer Name ordering the selected Product
                                        placeorder.check_name(self.OrderInforesult[1][row_index])
                                        self.assertTrue(placeorder.check_name_review(self.OrderInforesult[1][row_index]), "Customer Name is not correct")
                                        # Verify The Phone number of the customer odering the selected Product
                                        placeorder.fill_phone_number(self.OrderInforesult[11][row_index])
                                        self.assertTrue(placeorder.check_phone_number_review(self.OrderInforesult[11][row_index]), "Phone Number doesn't match the entered phone number")
                                        # Verify the Address of the Customer ordering the selected Product
                                        placeorder.fill_address_optional(self.OrderInforesult[12][row_index], self.OrderInforesult[13][row_index])
                                        self.assertTrue(placeorder.check_address_optional(self.OrderInforesult[12][row_index], self.OrderInforesult[13][row_index]), "Optional Address doesn't match the selected Optional Address")
                                        # Verify the Zip Code of the Customer ordering the selected Product
                                        placeorder.check_zip_code(self.OrderInforesult[2][row_index])
                                        self.assertTrue(placeorder.check_zip_code_review(self.OrderInforesult[2][row_index]), "Zip Code doesn't match the entered Zip Code")
                                        # Verify the details address Line1 of the Customer ordering the selected Product
                                        placeorder.fill_address_line1(self.OrderInforesult[14][row_index])
                                        self.assertTrue(placeorder.check_address_line1_review(self.OrderInforesult[14][row_index]), "Address Line 1 doesn't match the entered Address Line 1")
                                        # Verify the details address Line2 of the Customer ordering the selected Product
                                        placeorder.fill_address_line2(self.OrderInforesult[15][row_index])
                                        self.assertTrue(placeorder.check_address_line2_review(self.OrderInforesult[15][row_index]), "Address Line 2 doesn't match the entered Address Line 2")
                                        # Verify the delivery date of the order of the selected Product
                                        placeorder.fill_delivery_date(self.OrderInforesult[16][row_index])
                                        self.assertTrue(placeorder.check_delivery_date_review(self.OrderInforesult[16][row_index]), "Delivery Date doesn't match the selected Delivery Date")
                                        # Verify the first and last name of the recipient of  the selected Product
                                        placeorder.fill_first_and_last_name(self.OrderInforesult[17][row_index])
                                        self.assertTrue(placeorder.check_first_and_last_name_review(self.OrderInforesult[17][row_index]), "First and last names don't match the entered first and last names")
                                        # Verify the Zip Code of the recipient of  the selected Product
                                        placeorder.fill_billing_zip_code(self.OrderInforesult[18][row_index])
                                        self.assertTrue(placeorder.check_billing_zip_code_review(self.OrderInforesult[18][row_index]), "Billing Zip Code doesn't match the entered billing Zip Code")
                                        # Verify the detailed address line 1 of the recipient of  the selected Product
                                        placeorder.fill_billing_address_l1(self.OrderInforesult[19][row_index])
                                        self.assertTrue(placeorder.check_billing_address_l1(self.OrderInforesult[19][row_index]), "Billing Address Line 1 doesn't match the entered Billing Address Line 1")
                                        # Verify the detailed address line 2 of the recipient of  the selected Product
                                        placeorder.fill_billing_address_l2(self.OrderInforesult[20][row_index])
                                        self.assertTrue(placeorder.check_billing_address_l2(self.OrderInforesult[20][row_index]), "Billing Address Line 2 doesn't match the entered Billing Address Line 2")
                                        # Verify the email of the customer ordering the selected Product
                                        placeorder.fill_email_address(self.OrderInforesult[21][row_index])
                                        self.assertTrue(placeorder.check_email_address(self.OrderInforesult[21][row_index]), "The email address doesn't match the entered email address")
                                        # Verify the phone number of the customer ordering the selected Product
                                        placeorder.fill_billing_phone_number(self.OrderInforesult[22][row_index])
                                        self.assertTrue(placeorder.check_billing_phone_number(self.OrderInforesult[22][row_index]), "The Billing Phone number doesn't match the entered Billing Phone number")
                                        # Verify if the customer required notification via sms for the order of the selected Product
                                        placeorder.check_sms_notification(self.OrderInforesult[23][row_index])
                                        # Verify if the customer has a promotion code for the order of the selected Product
                                        placeorder.fill_olyve_premiere_code(self.OrderInforesult[24][row_index])
                                        # Verify The creddit card of customer ordering the selected Product
                                        placeorder.fill_credit_card_details(self.OrderInforesult[25][row_index], self.OrderInforesult[26][row_index], self.OrderInforesult[27][row_index], self.OrderInforesult[28][row_index])
                                        # Verify the message sent with the order of the selected Product
                                        self.assertTrue(placeorder.check_message_review(self.OrderInforesult[4][row_index]), "The Message doesn't match the entered message")
                                        # Verify the signature of the message sent with the order of the selected Product
                                        self.assertTrue(placeorder.check_signature_review(self.OrderInforesult[4][row_index]), "The Signature doesn't match the entered signature")
                                        # Verify the Video/Photo sent with the order of the selected Product
                                        self.assertTrue(placeorder.check_videophoto_review(self.OrderInforesult[6][row_index], self.OrderInforesult[7][row_index], self.GeneralInforesult[1][4]), "The Video/Photo uploaded not found")
                                        # Returns back to the Checkout Page
                                        BasicActions.go_back()
                                        placeorder.wait_for_checkout_page()
                                        # Click on the Buy button to proceed to the Order Details Page
                                        placeorder.Buy_click(self.OrderInforesult[4][row_index], self.OrderInforesult[16][row_index])
                                        # Problem in waiting for Order Details Screen, Use time.sleep instead
                                        time.sleep(60)
                                        if placeorder.wait_for_order_details_page:
                                            current_url = Browser._driver.current_url
                                            if current_url == self.GeneralInforesult[1][3]:
                                                # Check the Order ID
                                                placeorder.check_confirmation_number()
                                                # Verify the customer name ordering of the selected Product
                                                self.assertTrue(placeorder.check_name_order_details(self.OrderInforesult[1][row_index]), "Customer Name is not correct")
                                                # Verify the detailed address line 1 of the recipient of the selected Product
                                                self.assertTrue(placeorder.check_address_line1_order_details(self.OrderInforesult[14][row_index]), "Address Line 1 doesn't match the entered Address Line 1")
                                                # Verify the detailed address line 2 of the recipient of the selected Product
                                                self.assertTrue(placeorder.check_address_line2_order_details(self.OrderInforesult[15][row_index]), "Address Line 2 doesn't match the entered Address Line 2")
                                                # Verify Zip Code of the the customer ordering of the selected Product
                                                self.assertTrue(placeorder.check_zip_code_order_details(self.OrderInforesult[2][row_index]), "Zip Code doesn't match the entered Zip Code")
                                                # Verify the Delivery Date of the order
                                                self.assertTrue(placeorder.check_delivery_date_order_details(self.OrderInforesult[16][row_index]), "Delivery Date doesn't match the selected Delivery Date")
                                                # Verify the Questions and Concerns Contacts for OLYVE
                                                self.assertTrue(placeorder.check_questions_and_concerns_oder_details(self.OrderInforesult[29][row_index]), "The number of Questions and Concerns is not correct")
                                                # Updates via text using PIN the order if required
                                                placeorder.check_updates_via_text_order_details(self.OrderInforesult[30][row_index])
                                            else:
                                                raise Exception("Invalid Page")
                            else:
                                raise Exception("Invalid Page")
                        else:
                            raise Exception("Invalid Page")


    @classmethod
    def tearDown(cls):
        # close the browser window(s)
        Browser.quit_driver()

if __name__ == '__main__':
    unittest.main()
