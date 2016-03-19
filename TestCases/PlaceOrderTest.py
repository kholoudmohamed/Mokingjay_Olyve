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

        # Open Olyve website
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
        self.driver.implicitly_wait(20)
        # Following locator is for Pick Me button.
        locator3 = "html/body/div[1]/div/div/div[2]/div[2]/div[5]/div/div"
        if placeorder.page_load_special(40, By.XPATH, locator3):
            # Get Price of the Product
            product_price= placeorder.get_product_price()
            # Click on the Pick Me button
            placeorder.click_on_pickme_button()
            # Fill the Name and Zipcode in the Pick Me popup then click on GO button
            action = ActionChains(self.driver)
            action.send_keys(DataReader.get_data("OrderInfo", 2, 1))
            action.send_keys(Keys.TAB)
            action.send_keys(DataReader.get_data("OrderInfo", 3, 1))
            action.send_keys(Keys.ENTER)
            # Wait until the next page is opened
            self.driver.implicitly_wait(100)
            # Check if the Page opened is the Accessory page
            if(self.driver.current_url == DataReader.get_data("General Info", 1, 1)):
                # Check if the user required to click on yes button if accessory is required
                if (DataReader.get_data("OrderInfo", 4, 1)== 'Yes'):
                    placeorder.click_yesplease()
                    accessory_price= placeorder.get_accessory_price()
                # Check if the user required to click on No button if not accessory is required
                else:
                    placeorder.click_nothanks()
            # Check if the current page is message page
            if(self.driver.current_url == DataReader.get_data("General Info", 2, 1)):
                return  True

    @classmethod
    def tearDown(cls):
        # close the browser window
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
