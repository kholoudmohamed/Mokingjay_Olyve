from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


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

    # Fill the required data in the message page
    def fill_gift_message(self, message, signature, photolocation, videolocation):
        # Write Gift Message if required
        if message != "":
            self._driver.find_element_by_xpath("html/body/div[1]/div/div/div[2]/div/div/textarea").send_keys(message)
        # Sign the Gift Message if required
        if signature != "":
            self._driver.find_element_by_xpath("html/body/div[1]/div/div/div[2]/div/div/input").send_keys(signature)
        # Upload Photo in case that Photo Location is not empty
        if photolocation != "":
            self._driver.execute_script("document.getElementById('photoFile').style.display='block'")
            self._driver.find_element_by_id("photoFile").send_keys(photolocation)
            self._driver.execute_script("document.getElementById('photoFile').style.display='none'")

            imagelocator = 'html/body/div[1]/div/div/div[5]/div[2]/div[2]/div/div/img'
            WebDriverWait(self._driver, 500).until(EC.visibility_of_element_located((By.XPATH, imagelocator)))

        # Upload Video  in case that Photo Location is not empty
        if videolocation != "":
            self._driver.execute_script("document.getElementById('videoFile').style.display='block'")
            self._driver.find_element_by_id("videoFile").send_keys(videolocation)
            self._driver.execute_script("document.getElementById('videoFile').style.display='none'")

            videolocator = './/*[@id="azureplayer"]'
            WebDriverWait(self._driver, 800).until(EC.visibility_of_element_located((By.XPATH, videolocator)))

        # Click on Review and Checkout button
        self._driver.find_element_by_xpath("html/body/div/div/div/div[6]/div/a").click()

    # Fill and check the data in the checkout page
    def checkout(self, accessory, notification, phonenumber, addressoptional, addressline1, addressline2, deliverydate, firstandlastname,
                 billingzipcode, billingaddressl1, billingaddressl2, emailaddress, billingphonenumber, smsnotification,olyvepremierecode,
                 creditcardnumber, creditcardmonth, creditcardyear, creditcardccv):
        #Proudct Name
        element1 = self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[1]/div[2]/span[1]")
        #Also the product name down
        self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[10]/div[1]/div[2]/div[1]")
        # Product Price
        element2 = self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[1]/div[2]/span[2]")
        # Also Product Price down
        self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[10]/div[1]/div[2]/div[2]")
        # The following part is checked only if accessory is selected and available for the product
        if accessory == "Yes":
            # Accesorry Text
            element3 = self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[2]/div[2]/span[1]")
            #Also the Accessory Text down
            self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[10]/div[1]/div[3]/div[1]")
            # Accessory Price
            element4 = self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[2]/div[2]/span[2]")
            #Also the Accessory Price down
            self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[10]/div[1]/div[3]/div[2]")
        # Notification Text
        element5 = self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[3]/div[2]/span")
        # Also the notification text down
        self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[10]/div[1]/div[5]/div")
        # Subtotal
        element6 = self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[3]/div[2]/div/div[1]")
        # Sales Taxes
        element7 = self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[3]/div[2]/div/div[2]")
        # Also Sales Taxes down
        self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[10]/div[1]/div[6]/div[2]")
        # Total
        element8 = self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[3]/div[2]/div/div[3]")
        # Also Subtotal down
        self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[10]/div[1]/div[7]/div")
        # Name
        element9 = self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[7]/div/div[2]/div/div/input")
        # Also name down
        self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[10]/div[2]/div[2]/div")
        # Phone Number
        if phonenumber != "":
            self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[7]/div/div[3]/div/div/input").send_keys(phonenumber)
            # Also Phone Number down
            self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[10]/div[2]/div[6]/div")
        # Address Optional
        if addressoptional != "":
            self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[7]/div/div[5]/div/span/a").send_keys(addressoptional)
            # Also optional address down
            self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[10]/div[2]/div[8]/div")
        # Zip Code
        element12 = self._driver.find_element_by_xpath(".//*[@id='recipientZipcode']")
        # Also Zip Code down
        self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[10]/div[2]/div[5]/div")
        # Address Line 1
        if addressline1 != "":
            self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[7]/div/div[5]/div/span/a").send_keys(addressline1)
            # Also Address Line 1 down
            self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[10]/div[2]/div[3]/div")
        # Address Line 2
        if addressline2 != "":
            self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[7]/div/div[5]/div/span/a").send_keys(addressline2)
            # Also Address Line 2 down
            self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[10]/div[2]/div[4]/div")
        # Delivery Date
        if deliverydate != "":
            # Send the Delivery Date
            return True
            # Also Delivery Date Down
            self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[10]/div[2]/div[7]/div")
        if firstandlastname != "":
            self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[7]/div/div[5]/div/span/a").send_keys(firstandlastname)
            # Also first and last name down
            self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[10]/div[4]/div[2]/div")
        if billingzipcode != "":
            self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[7]/div/div[5]/div/span/a").send_keys(billingzipcode)
            # Also billing Zip Code down
            self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[10]/div[4]/div[5]/div")
        if billingaddressl1 != "":
            self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[7]/div/div[5]/div/span/a").send_keys(billingaddressl1)
            # Also billing address 1 down
            self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[10]/div[4]/div[3]/div")
        if billingaddressl2 != "":
            self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[7]/div/div[5]/div/span/a").send_keys(billingaddressl2)
            # Also billing address 2 down
            self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[10]/div[4]/div[4]/div")
        if emailaddress != "":
            self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[7]/div/div[5]/div/span/a").send_keys(emailaddress)
            # Also billing email address
            self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[10]/div[4]/div[7]/div")
        if billingphonenumber != "":
            self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[7]/div/div[5]/div/span/a").send_keys(billingphonenumber)
            # Also billing phone number down
            self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[10]/div[4]/div[6]/div")
        if smsnotification == "Yes":
            # Check the checkbox
            return True
        if olyvepremierecode != "":
            self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[9]/div/div[9]/div/div[1]/div/a/i").click
            self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[9]/div/div[9]/div/div[2]/div[1]/input").send_keys(olyvepremierecode)
        if creditcardnumber != "":
            if creditcardmonth != "":
                if creditcardyear != "":
                    if creditcardccv != "":
                        self._driver.find_element_by_xpath(".//*[@id='creditCardNumberRow']/div/div/input").send_keys(creditcardnumber)
                        self._driver.find_element_by_xpath(".//*[@id='creditCardNumberDetailsRow']/div[1]/div/input").send_keys(creditcardmonth)
                        self._driver.find_element_by_xpath(".//*[@id='creditCardExpYearId']").send_keys(creditcardyear)
                        self._driver.find_element_by_xpath(".//*[@id='creditCardNumberDetailsRow']/div[3]/div/input").send_keys(creditcardccv)
        # Also check the message
        self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[10]/div[3]/div[2]")
        # Also check the signature
        self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[10]/div[3]/div[3]/div")
        # Also check the image and video
        self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[10]/div[3]/div[4]/div/a").click()
        # Need to call special function to check the video
        self._driver.find_element_by_xpath("xhtml:html/xhtml:body/xhtml:video")
        # How could we check the content of the video?????
        self._driver.find_element_by_xpath(".//*[@id='completeForm']/div[11]/div/a").click()

    # Check Order Details
    def checkorderdetails(self, name, addressline1, addressline2, zipcode, deliverydate, questionsandconcerns, updatesviatext):
        # Confirmation Number
        self._driver.find_element_by_xpath("html/body/div[1]/div/div/div[2]/div[2]/div")
        # Name
        self._driver.find_element_by_xpath("html/body/div[1]/div/div/div[2]/div[3]/div")
        # Address Line 1
        self._driver.find_element_by_xpath("html/body/div[1]/div/div/div[2]/div[4]/div")
        # Address Line 2
        self._driver.find_element_by_xpath("html/body/div[1]/div/div/div[2]/div[5]/div")
        # Zip Code
        self._driver.find_element_by_xpath("html/body/div[1]/div/div/div[2]/div[8]/div")
        # Delivery Date
        self._driver.find_element_by_xpath("html/body/div[1]/div/div/div[2]/div[9]/div")
        # Questions & Concerns
        self._driver.find_element_by_xpath("html/body/div[1]/div/div/div[2]/div[10]/div")
        if updatesviatext == "Yes":
            # Updates Via Text
            self._driver.find_element_by_xpath("html/body/div[1]/div/div/div[2]/div[13]/div/input")
            # Submit
            self._driver.find_element_by_xpath("html/body/div[1]/div/div/div[2]/div[14]/div/input").click()
        else:
            # Return to Home Page
            self._driver.find_element_by_xpath("html/body/div[1]/div/olv-header/nav/div[1]/a[1]/i").click()