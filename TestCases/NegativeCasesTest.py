import unittest
from PageObjects.PlaceOrder import PlaceOrder
from PageObjects.NegativeCases import NegativeCases
from Utilities import FileLocator
from Utilities.Browser import Browser
from Utilities.PageActions import BasicActions
from Utilities.ExcelDataReader import ExcelDataReader
from Configurations import ConfigReader


class NegativeCasesTest(unittest.TestCase):
    # Get the file location of the Excel Input File
    _fileLocation = FileLocator.read_config_get_file_location('ExcelConfiguration', 'DataSourcefileLocation')

    # In the Configuration File with the Key 'ExcelConfiguration' - Sheet Name 'OrderInfoSheetName'
    orderinfo_sheetName = ConfigReader.readconfig('ExcelConfiguration', 'OrderInfoSheetName')
    # Fill the result of the selected sheet in the 2 dimensional array with the values in 'OrderInfoSheetName'
    OrderInforesult = ExcelDataReader.get_data(_fileLocation, orderinfo_sheetName, HDR=True)

    # In the Configuration File with the Key 'ExcelConfiguration' - Sheet Name 'GeneralInfoSheetName'
    Negative_sheetName = ConfigReader.readconfig('ExcelConfiguration', 'GeneralInfoSheetName')
    # Fill the result of the selected sheet in the 2 dimensional array with the values in 'GeneralInfoSheetName'
    Negativeresult = ExcelDataReader.get_data(_fileLocation, Negative_sheetName, HDR=True)

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
    def test_productimage_with_pick_me_button(self):
        placeorder = PlaceOrder(Browser._driver)
        negativecases = NegativeCases(Browser._driver)
        # Find the selected product and click on it
        placeorder.findproductandclick(self.OrderInforesult[0][0])
        # Wait till the Product Details page is loaded
        BasicActions.implicit_wait(50)
        if placeorder.wait_for_product_page():
            self.assertTrue(negativecases.product_image_click(),"Clicking on Product image and pick me button are not correct")

    def test_missing_name_zipcode(self):
        placeorder = PlaceOrder(Browser._driver)
        negativecases = NegativeCases(Browser._driver)
        # Find the selected product and click on it
        placeorder.findproductandclick(self.OrderInforesult[0][0])
        # Wait till the Product Details page is loaded
        BasicActions.implicit_wait(50)
        if placeorder.wait_for_product_page():
            self.assertTrue(negativecases.no_name_zipdode(self.Negativeresult[4][0]), "Missing Name or Zip Code are accepted")

    def test_invalid_name(self):
        placeorder = PlaceOrder(Browser._driver)
        negativecases = NegativeCases(Browser._driver)
        # Find the selected product and click on it
        placeorder.findproductandclick(self.OrderInforesult[0][0])
        # Wait till the Product Details page is loaded
        BasicActions.implicit_wait(50)
        if placeorder.wait_for_product_page():
            self.assertTrue(negativecases.invalid_name(self.Negativeresult[8][0],self.Negativeresult[3][0],self.Negativeresult[6][0]), "Invalid Name is accepted")

    def test_invalid_zipcode(self):
        placeorder = PlaceOrder(Browser._driver)
        negativecases = NegativeCases(Browser._driver)
        # Find the selected product and click on it
        placeorder.findproductandclick(self.OrderInforesult[0][0])
        # Wait till the Product Details page is loaded
        BasicActions.implicit_wait(50)
        if placeorder.wait_for_product_page():
            self.assertTrue(negativecases.invalid_zip_code(self.Negativeresult[7][0],self.Negativeresult[2][0],self.Negativeresult[5][0]),"Invalid Zip Code is accepted")

    def test_usupported_zipcode(self):
        placeorder = PlaceOrder(Browser._driver)
        negativecases = NegativeCases(Browser._driver)
        # Find the selected product and click on it
        placeorder.findproductandclick(self.OrderInforesult[0][0])
        # Wait till the Product Details page is loaded
        BasicActions.implicit_wait(50)
        if placeorder.wait_for_product_page():
            self.assertTrue(negativecases.unsupported_zip_code(self.Negativeresult[7][0],self.Negativeresult[3][0],self.Negativeresult[9][0],self.Negativeresult[10][0]),"Unsupported Zip Code is accepted")

if __name__ == '__main__':
    unittest.main()
