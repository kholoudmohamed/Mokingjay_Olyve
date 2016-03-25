from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class PlaceOrder:
    def __init__(self, driver):
        self._driver = driver

    # explicit wait until presence of configurable element
    def page_load(self, time_to_wait, by_method, locator):
        element = WebDriverWait(self._driver, time_to_wait).until(EC.presence_of_element_located((by_method, locator)))

    # explicit wait until presence of configurable element with return as conditional action dependency
    def page_load_special(self, time_to_wait, by_method, locator):
        element = WebDriverWait(self._driver, time_to_wait).until(EC.presence_of_element_located((by_method, locator)))
        return True

    # Find Product in Olyve and make sure that this product is clickable
    def findproductandclick(self, product):
        try:
            WebDriverWait(driver=self._driver, timeout=5).until(
                EC.presence_of_all_elements_located(locator=(By.CLASS_NAME, "name")))
            doubleqoute = '"'
            productxpath = ".//div[1]/div/a[contains(@href," + doubleqoute + product + doubleqoute + ")]"
            # Find the product
            product_link = self._driver.find_element_by_xpath(productxpath)
            # Click on the Product found
            product_link.click()
        except:
            raise Exception("Product Not Found")

    # Click on Pick Me button inside the selected Product
    def click_on_pickme_button(self):
        pick_me = self._driver.find_element_by_xpath('html/body/div/div/div/div[2]/div[2]/div[5]/div/div')
        pick_me.click()

    # Get the price of the selected product
    def get_product_price(self):
        product_price = self._driver.find_element_by_xpath('html/body/div[1]/div/div/div[2]/div[2]/div[3]/div/div')
        return product_price.text

    # Check if the Pick me pop up exists
    def pickmepopupexists(self):
        try:
            self._driver.find_element_by_xpath(".//*[@id='ngdialog2']/div/div[1]/form/div[5]/div/a")
        except NoSuchElementException:
            return False
        return True

    # Fill info from the excel sheet into the pick me pop up
    def fill_pickme_popup(self, name, zipcode):
        self._driver.find_element_by_name('recipientName').send_keys(name)
        self._driver.find_element_by_name('recipientzipCode').send_keys(zipcode)
        self._driver.find_element_by_xpath(".//*[@id='ngdialog1']/div/div[1]/form/div[5]/div/a").click()

    # Click on Yes, Please button in the Accessory Page
    def click_yesplease(self):
        yesplease = self._driver.find_element_by_xpath('html/body/div/div/div/div[2]/div[2]/div[3]/div')
        yesplease.click()

    # Click on No, Thanks button in the Accessory Page
    def click_nothanks (self):
        nothanks = self._driver.find_element_by_xpath('html/body/div[1]/div/div/div[2]/div[2]/div[4]/div')
        nothanks.click()

    # Get the price of the selected accessory
    def get_accessory_price(self):
        accessoryprice = self._driver.find_element_by_xpath('html/body/div/div/div/div[2]/div[2]/div[2]/div/div')
        return accessoryprice.text