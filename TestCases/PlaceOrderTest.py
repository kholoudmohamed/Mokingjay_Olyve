import unittest
from selenium import webdriver
from PageObjects.PlaceOrder import PlaceOrder
from builtins import classmethod
from selenium.webdriver.common.by import By
from PageObjects.ExcelDataReader import DataReader
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class PlaceOrderTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        # create a new Chrome session and maximize the window
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()


        cls.driver.get("https://test@olyveinc.com:Amr<3skype@olyve.olyveinc.com")

        # Wait till the Home page is loaded
        locator = "html/body/div/div/olv-header/nav/div[1]/div[2]/a/img"
        placeorder = PlaceOrder(cls.driver)
        placeorder.page_load(40, By.XPATH, locator)

    # Place Order for Product
    def test_place_product_order(self):
        placeorder = PlaceOrder(self.driver)
        # Get the number of products
        placeorder.findproductandclick(DataReader.get_data("OrderInfo", 1, 1))
        self.driver.implicitly_wait(50)
        # Following locator is for Pick Me button.
        locator3 = "html/body/div[1]/div/div/div[2]/div[2]/div[5]/div/div"
        if placeorder.page_load_special(40, By.XPATH, locator3):
            # Get Price of the Product as it will be required in the Review page
            product_price = placeorder.get_product_price()
            # Click on the Pick Me button
            placeorder.click_on_pickme_button()
            # Wait till The "WHO ARE WE DELIVERING TO" popup is displayed
            self.driver.implicitly_wait(20)
            # Fill the "WHO ARE WE DELIVERING TO" popup with data set in the input excel file
            placeorder.fill_pickme_popup(DataReader.get_data("OrderInfo", 2, 1), DataReader.get_data("OrderInfo", 3, 1))
            # locators to be used in the explicit wait in order to proceed with the Order
            locator4 = "html/body/div/div/div/div[2]/div[1]/div[1]/div/olv-image/div/img"
            locator5 = "html/body/div/div/div/div[6]/div/a"
            # Wait until the next page is opened
            if (placeorder.page_load_special(100, By.XPATH, locator4))or (placeorder.page_load_special(100, By.XPATH, locator5)):
                # Get the URL of the current page
                current_url = self.driver.current_url
                # Check if the Page opened is the Accessory page
                if current_url == DataReader.get_data("General Info", 1, 1):
                    # Check if the user required to click on yes button if accessory is required
                    if DataReader.get_data("OrderInfo", 4, 1) == 'Yes':
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
                self.driver.implicitly_wait(30)
                if placeorder.page_load_special(100, By.XPATH, locator5):
                    # Get the URL of the current page
                    current_url = self.driver.current_url
                    # Check if the current page is message page
                    if current_url == DataReader.get_data("General Info", 2, 1):
                        print("we are here")
                    else:
                        raise Exception("Invalid Page")


    @classmethod
    def tearDown(cls):
        # close the browser window
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
