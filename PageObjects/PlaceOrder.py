from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from datetime import date
from Utilities import PageActions
from Utilities import FileLocator
from decimal import *
import time

class PlaceOrder(object):
    # Olyve Logo located in the Header of the Home page
    header_olyve_logo = (By.ID, 'header-logo')
    # Pick Me button located in the selected Product
    pick_me_button = (By.XPATH, "html/body/div[1]/div/div/div[2]/div[2]/div[5]/div/div")
    # Explicit Wait Objects to be loaded
    accessory_load = (By.XPATH, "html/body/div/div/div/div[2]/div[1]/div[1]/div/olv-image/div/img")
    message_load = (By.XPATH, "html/body/div/div/div/div[6]/div/a")
    checkout_load = (By.ID, "buy-loader")
    orderdetails_load = (By.ID, "ordernumber")
    videophoto_load = (By.XPATH, "html/body/div[1]/div/div/div[4]/div/img")
    promo_code_load = (By.CSS_SELECTOR, "#promo-code>a>olv-loader>img")
    # Product Price located in the selected Product
    product_price = (By.XPATH, 'html/body/div[1]/div/div/div[2]/div[2]/div[3]/div/div')
    # The Name of the customer ordering the Product located in the pick me pop-up
    customer_name = (By.XPATH, ".//*[@id='ngdialog1']/div/div[1]/form/div[2]/div/div[2]/div/input")
    # The Zip Code of the customer that will oder the Product located in the pick me pop-up
    zip_code = (By.XPATH, ".//*[@id='ngdialog1']/div/div[1]/form/div[4]/div/div[2]/div/input")
    # The GO button that will be clicked to continue the order of the selected Product located in the pick me pop-up
    go_button = (By.XPATH, ".//*[@id='ngdialog1']/div/div[1]/form/div[5]/div/a")
    # The option to click on the YES button to add Accessory to the selected Product
    yes_please_button = (By.XPATH, 'html/body/div/div/div/div[2]/div[2]/div[3]/div')
    # The option to click on the NO button to order the selected Product ONLY
    no_thanks_button = (By.XPATH, 'html/body/div[1]/div/div/div[2]/div[2]/div[4]/div')
    # The price of the accessory requested with the selected product
    accessory_price = (By.XPATH, 'html/body/div/div/div/div[2]/div[2]/div[2]/div/div')
    # The option to send a message with the selected Product
    message_body = (By.XPATH, "html/body/div[1]/div/div/div[2]/div/div/textarea")
    # The option to sign the message sent with the selected Product
    message_sign = (By.XPATH, "html/body/div[1]/div/div/div[2]/div/div/input")
    # The option to add a photo to be send with the selected Product
    # The location of the Photo File
    photo_file = (By.ID, "photoFile")
    # The field that will be filled with the Photo File Location
    imagelocator = (By.XPATH, 'html/body/div[1]/div/div/div[5]/div[2]/div[2]/div/div/img')
    # The option to add a video to be send with the selected Product
    # The location of the Video  File
    video_file = (By.ID, "videoFile")
    # The field that will be filled with the Video File Location
    videolocator = (By.XPATH, './/*[@id="azureplayer"]')
    # The review and Checkout button to be clicked to proceed to the Checkout page with the order
    review_and_checkout_button = (By.CSS_SELECTOR, '.col-xs-12.text-center>a')
    # The name of the selected Product
    product_name = (By.XPATH, ".//*[@id='completeForm']/div[1]/div[2]/span[1]")
    # The review of the name of the selected Product
    product_name_review = (By.XPATH, ".//*[contains(@class,'row final-review')]/div[1]/div[2]/div[1]")
    # The price of the selected Product
    product_price_review1 = (By.XPATH, ".//*[@id='completeForm']/div[1]/div[2]/span[2]")
    # The review of the price of the selected Product
    product_price_review2 = (By.XPATH, ".//*[contains(@class,'row final-review')]/div[1]/div[2]/div[2]")
    # The accessory section in checkout page.
    accessory_section = (By.XPATH,".//*[@id='completeForm']/div[2]")
    # The accessory text "Olyve + Elbow Chocolates"
    accessory_text = (By.XPATH, ".//*[@id='completeForm']/div[2]/div[2]/span[1]")
    # The price of the selected accessory
    accessory_price_review1 = (By.XPATH, ".//*[@id='completeForm']/div[2]/div[2]/span[2]")
    # The review of the price of the selected accessory at the top of the Checkout page
    accessory_text_review = (By.XPATH, ".//*[@id='completeForm']/div[10]/div[1]/div[3]/div[1]")
    # The review of the price of the selected accessory at the bottom of the Checkout page
    accessory_price_review2 = (By.XPATH, ".//*[@id='completeForm']/div[10]/div[1]/div[3]/div[2]")
    # The notification message "gift box and delivery included"
    notification_text = (By.CSS_SELECTOR, ".name-container>span")
    # The review of the notification message "gift box and delivery included"
    notification_text_review = (By.CSS_SELECTOR, ".col-xs-12.text-center.address-line.up")
    # The price of the accessory if requested + the price of the selected Product
    # The taxes applied on this product in the region of the selected Zip Code
    # The total price of the product selected + accessory if request + taxes
    subtotal_And_salestaxes_And_totalprice = (By.CSS_SELECTOR, ".subtotal.desktop-view>div")
    # The review of taxes applied on this product in the region of the selected Zip Code
    sales_taxes_review = (By.CSS_SELECTOR, ".col-xs-4.text-right.address-line.up")
    # The review of total price of the product selected + accessory if request + taxes
    total_price_review = (By.CSS_SELECTOR, ".col-xs-12.text-center.address-line.up")
    # The name of the customer that will order the Product
    name_review1 = (By.XPATH, ".//*[contains(@class,'row recipient-info')]/div/div[2]/div/div/input")
    # The review of the name of the customer ordering the Product
    name_review2 = (By.XPATH, ".//*[contains(@class,'row final-review')]/div[2]/div[2]/div")
    # The Phone number of the customer ordering the selected Product
    phone_number = (By.XPATH, ".//*[contains(@class,'row recipient-info')]/div/div[3]/div/div/input")
    # The review of the phone number of the customer ordering the selected Product
    phone_number_review = (By.XPATH, ".//*[contains(@class,'row final-review')]/div[2]/div[6]/div")
    # The address tag of the customer ordering the selected Product
    address_optional = (By.XPATH, ".//*[contains(@class,'row recipient-info')]/div/div[5]/div/span/a")
    # The review of the address tag of the customer ordering the selected Product
    address_optional_review = (By.XPATH, ".//*[contains(@class,'row final-review')]/div[2]/div[8]/div")
    # The Zip Code of the customer ordering the selected Product
    zip_code_review1 = (By.ID, "recipientZipcode")
    # The review of the Zip Code of the customer ordering the selected Product
    zip_code_review2 = (By.XPATH, ".//*[contains(@class,'row final-review')]/div[2]/div[5]/div")
    # The detailed address line 1 of the customer ordering the selected Product
    address_line1 = (By.ID, "recipientAddressLine1")
    # The review of detailed address of the customer ordering the selected Product
    address_line1_review = (By.XPATH, ".//*[contains(@class,'row final-review')]/div[2]/div[3]/div")
    # The detailed address line 2 of the customer ordering the selected Product
    address_line2 = (By.ID, "recipientAdressLine2")
    # The review of detailed address line 2 of the customer ordering the selected Product
    address_line2_review = (By.XPATH, ".//*[contains(@class,'row final-review')]/div[2]/div[4]/div")
    # The review of the delivery date of the order
    delivery_date_review = (By.XPATH, ".//*[contains(@class,'row final-review')]/div[2]/div[7]/div")
    # The First and Last Name of the recipient
    first_and_last_name = (By.XPATH, ".//*[contains(@class,'row billing-info')]/div/div[2]/div/div/input")
    # The review of the First and Last Name of the recipient
    first_and_last_name_review = (By.XPATH, ".//*[contains(@class,'row final-review')]/div[4]/div[2]/div")
    # The Zip Code of the recipient
    billing_zip_code = (By.ID, "billingZipcode")
    # The review of the Zip Code of the recipient
    billing_zip_code_review = (By.XPATH, ".//*[contains(@class,'row final-review')]/div[4]/div[5]/div")
    # The detailed address line 1 of the recipient
    billing_address_l1 = (By.ID, "billingAddressLine1")
    # The review of detailed address line 1 of the recipient
    billing_address_l1_review = (By.XPATH, ".//*[contains(@class,'row final-review')]/div[4]/div[3]/div")
    # The detailed address line 2 of the recipient
    billing_address_l2 = (By.XPATH, ".//*[contains(@class,'row billing-info')]/div/div[5]/div/div/input")
    # The review of detailed address line 2 of the recipient
    billing_address_l2_review = (By.XPATH, ".//*[contains(@class,'row final-review')]/div[4]/div[4]/div")
    # The email address of the customer ordering the selected Product
    email_address = (By.XPATH, ".//*[contains(@class,'row billing-info')]/div/div[6]/div/div/input")
    # The review of the email address of the customer ordering the selected Product
    email_address_review = (By.XPATH, ".//*[contains(@class,'row final-review')]/div[4]/div[7]/div")
    # The phone number of the customer ordering the selected Product
    billing_phone_number = (By.XPATH, ".//*[contains(@class,'row billing-info')]/div/div[7]/div/div/input")
    # The review of the phone number of the customer ordering the selected Product
    billing_phone_number_review = (By.XPATH, ".//*[contains(@class,'row final-review')]/div[4]/div[6]/div")
    # If an sms is required to be send to the customer ordering the selected Product
    sms_notification = (By.XPATH, ".//*[contains(@class,'row billing-info')]/div/div[8]/div/div/div[1]/button")
    # If there is a promotion code for the customer ordering the selected Product
    olyve_premiere_code = (By.XPATH, ".//*[contains(@class,'row promo-code')]/div/div[1]/div/a/i")
    # The code provided to get a discount on the order of the selected Product
    code = (By.XPATH, ".//*[contains(@class,'row promo-code')]/div/div[2]/div[1]/input")
    # The apply button to apply the discount on the order of the selected Product
    apply_olyve_premeier_code = (By.XPATH, ".//*[@id='promo-code']/a")
    # The promotion code 'Premiere discount was applied!'
    promo_code_applied = (By.CSS_SELECTOR, '.col-xs-12.text-center.codeMessage')
    # Discount in the Review Section
    discount_review = (By.CSS_SELECTOR, ".col-xs-8.address-line.up")
    # Discount Value in the Review Section
    discount_value_review = (By.CSS_SELECTOR, '.col-xs-4.text-right.address-line.up')
    # The credit card number used to pay the order of the selected Product
    credit_card_number = (By.XPATH, ".//*[@id='creditCardNumberRow']/div/div/input")
    # The credit card expiry month of the credit card used to pay the order of the selected Product
    credit_card_month = (By.XPATH, ".//*[@id='creditCardNumberDetailsRow']/div[1]/div/input")
    # The credit card expiry year of the credit card used to pay the order of the selected Product
    credit_card_year = (By.ID, "creditCardExpYearId")
    # The credit card CCV number of the credit card used to pay the order of the selected Product
    credit_card_ccv = (By.XPATH, ".//*[@id='creditCardNumberDetailsRow']/div[3]/div/input")
    # The review of the message sent with the order
    message_review = (By.XPATH, ".//*[contains(@class,'row final-review')]/div[3]/div[2]")
    # The review of the signature of the customer ordering the selected Product
    signature_review = (By.XPATH, ".//*[contains(@class,'row final-review')]/div[3]/div[3]/div")
    # In the Checkout Page there should be a link to detect if a photo/video is sent with the order of the selected Product
    gift_image_video = (By.XPATH, ".//*[contains(@class,'row final-review')]/div[3]/div[4]/div/a")
    # The video is displayed in the page that check video uploaded is sent with the order
    video_upload_review = (By.XPATH, "xhtml:html/xhtml:body/xhtml:video")
    # The image is displayed in the page that check image uploaded is sent with the order
    image_upload_review = (By.XPATH, "html/body/div[1]/div/div/div[3]/div/img")
    # The Buy button that should be clicked to proceed to the Order Details Page
    Buy_button = (By.XPATH, ".//*[contains(@class,'row buy')]/div/a")
    # The Alert displayed if there is no message sent with the order and to make sure that the user didn't forgot to add it
    CardMessageDialog = (By.XPATH, ".//*[@id='ngdialog2-aria-describedby']")
    # The Alert displayed if the selected delivery date is not available
    DeliveryDateNotAvailable = (By.XPATH, ".//*[@id='ngdialog3']/div[2]/div/div/div[1]/div")
    # The Order ID displayed in the Order Details Page
    confirmation_number = (By.XPATH, "html/body/div[1]/div/div/div[2]/div[2]/div")
    # The Customer Name ordering the Product displayed in the Order Details Page
    name_review_order_details = (By.XPATH, "html/body/div[1]/div/div/div[2]/div[3]/div")
    # The detailed address line 1 of the recipient of the order in the Order Details Page
    address_line1_review_order_details = (By.ID, "recipientaddressLine1")
    # The City of the recipient of the order in the Order Details Page
    address_line1_review_order_details_city = (By.ID, "recipientcity")
    # The State of the recipient of the order in the Order Details Page
    address_line1_review_order_details_state = (By.ID, "recipientstate")
    # The detailed address line 2 of the recipient of the order in the Order Details Page
    address_line2_review_order_details = (By.ID, "recipientaddressLine2")
    # The Zip Code of the customer ordering the Product in the Order Details Page
    zip_code_review_order_details = (By.ID, "recipientzipcode")
    # The delivery date of the order in the Order Details Page
    delivery_date_review_order_details = (By.ID, "deliverydate")
    # The Contact information for OLYVE
    questions_and_concenrs = (By.XPATH, "html/body/div[1]/div/div/div[2]/div[10]/div")
    # If and upates required via text
    updates_via_text = (By.XPATH, "html/body/div[1]/div/div/div[2]/div[13]/div/input")
    # Submit the updates required using PIN
    submit = (By.XPATH, "html/body/div[1]/div/div/div[2]/div[14]/div/input")
    # Click to return to the Home Page after completion of the oder
    return_home = (By.XPATH, "html/body/div[1]/div/olv-header/nav/div[1]/a[1]/i")

    def __init__(self, driver):
        self._driver = driver

    # The following function finds a Product in Olyve and make sure that this product is clickable
    def findproductandclick(self, product):
        try:
            WebDriverWait(driver=self._driver, timeout=5).until(
                EC.presence_of_all_elements_located(locator=(By.CLASS_NAME, "name")))
            changeproductnamereview = product.replace("-", " + ").upper()
            product_link = self._driver.find_element_by_link_text(changeproductnamereview)
            product_link.click()
        except:
            raise Exception("Product Not Found")

    # The following function clicks on Pick Me button inside the selected Product
    def click_on_pickme_button(self):
        self._driver.find_element(*PlaceOrder.pick_me_button).click()

    # The following function gets the price of the selected product
    def get_product_price(self):
        return self._driver.find_element(*PlaceOrder.product_price).text

    # The following function fills info of the pick me pop up
    def fill_pickme_popup(self, Name, Zipcode):
        # Fill Customer Name
        self._driver.find_element(*PlaceOrder.customer_name).clear()
        self._driver.find_element(*PlaceOrder.customer_name).send_keys(Name)
        # Fill Zip Code
        self._driver.find_element(*PlaceOrder.zip_code).send_keys(Zipcode)
        self._driver.find_element(*PlaceOrder.zip_code).send_keys(Zipcode)
        # Click Go Button
        self._driver.find_element(*PlaceOrder.go_button).click()

    # The following function clicks on Yes, Please button to add Accessory to the order
    def click_yesplease(self):
        self._driver.find_element(*PlaceOrder.yes_please_button).click()

    # The following function clicks on No, Thanks button and the Accessory won't be added to the order
    def click_nothanks(self):
        self._driver.find_element(*PlaceOrder.no_thanks_button).click()

    # The following function gets the price of the selected accessory
    def get_accessory_price(self):
        return self._driver.find_element(*PlaceOrder.accessory_price).text

    # The following function fills the required data in the message page
    def fill_gift_message(self, message, signature):
        # Write Gift Message if required
        if message is not None:
            self._driver.find_element(*PlaceOrder.message_body).clear()
            self._driver.find_element(*PlaceOrder.message_body).send_keys(message)

        # Sign the Gift Message if required
        if signature is not None:
            self._driver.find_element(*PlaceOrder.message_sign).clear()
            self._driver.find_element(*PlaceOrder.message_sign).send_keys(signature)

    # The following function uploads Photo in case that Photo Location is not empty
    def upload_photo(self, filephotolocation):
        if filephotolocation is not None:
            photolocation = FileLocator.get_file_location(filephotolocation)
            self._driver.execute_script("document.getElementById('photoFile').style.display='block'")
            self._driver.find_element(*PlaceOrder.photo_file).send_keys(photolocation)
            self._driver.execute_script("document.getElementById('photoFile').style.display='none'")
            WebDriverWait(self._driver, 500).until(EC.visibility_of_element_located(locator=self.imagelocator))
            # (image_location).locator

    # The following function uploads Video  in case that Photo Location is not empty
    def upload_video(self, filevideolocation):
        if filevideolocation is not None:
            videolocation = FileLocator.get_file_location(filevideolocation)
            self._driver.execute_script("document.getElementById('videoFile').style.display='block'")
            self._driver.find_element(*PlaceOrder.video_file).send_keys(videolocation)
            self._driver.execute_script("document.getElementById('videoFile').style.display='none'")
            WebDriverWait(self._driver, 800).until(EC.visibility_of_element_located(locator=self.videolocator))

    # The following function clicks on Review and Checkout button
    def click_review_and_checkout(self):
        self._driver.find_element(*PlaceOrder.review_and_checkout_button).click()

    # The following function verifies that the name of the product at the checkout page is name of the selected product
    def check_product_name(self, productname):
        # Get Product Name
        changeproductname = productname.replace("-", " + ").upper()
        if self._driver.find_element(*PlaceOrder.product_name).text == changeproductname:
            return True
        else:
            return False

    # The following function verifies that of the product name at the checkout page review section is name of the selected product
    def check_product_name_review(self, productname):
        # Also the Product name in the review section
        changeproductnamereview = productname.replace("-", " + ").upper()
        if self._driver.find_element(*PlaceOrder.product_name_review).text == changeproductnamereview:
            return True
        else:
            return False

    # The following function verifies the price of the product at the checkout page is the price of the selected product
    def check_product_price(self, productprice):
        # Product Price
        changeproductprice = productprice+".00"
        if self._driver.find_element(*PlaceOrder.product_price_review1).text == changeproductprice:
            return True
        else:
            return False

    # The following function verifies the price of the product at the checkout page review section is the price of the selected product
    def check_product_price_review(self, productprice):
        # Also the Product price in the review section
        changeproductprice = productprice+".00"
        if self._driver.find_element(*PlaceOrder.product_price_review2).text == changeproductprice:
            return True
        else:
            return False

    # The following function verifies the accessory details at the checkout page is the accessory details of the selected product
    def check_accessory_details(self, accessory, accessorytext, accessoryprice):
        # The following part is checked only if accessory is selected and available for the product
        if accessory == "Yes":
            changeaccessoryprice = accessoryprice+".00"
            changeaccessorytext = accessorytext.upper()
            # Accesorry Text
            if self._driver.find_element(*PlaceOrder.accessory_text).text == changeaccessorytext:
                # Accessory Price
                if self._driver.find_element(*PlaceOrder.accessory_price_review1).text == changeaccessoryprice:
                    return True
            else:
                return False

    # The following function verifies the accessory details at the checkout page is the accessory details in the review section of the selected product
    def check_accessory_details_review(self, accessory, accessorytext, accessoryprice):
        if accessory == "Yes":
            changeaccessoryprice = accessoryprice+".00"
            changeaccessorytext = accessorytext.upper()
            # Also the Accessory Text in the review section
            if self._driver.find_element(*PlaceOrder.accessory_text_review).text == changeaccessorytext:
                # Also the Accessory Price in the review section
                if self._driver.find_element(*PlaceOrder.accessory_price_review2).text == changeaccessoryprice:
                    return True
            else:
                return False

    # The following function verifies the notification text at the checkout page is the notification text of the selected product
    def check_notification_text(self, notificationtext):
        # Notification Text
        changenotificationtext = notificationtext.upper()
        if self._driver.find_elements(*PlaceOrder.notification_text)[-1].text == changenotificationtext:
            return True
        else:
            return False

    # The following function verifies the notification text at the checkout page is the notification text in the review section of the selected product
    def check_notification_text_review(self, notificationtext):
        # Also the notification text in the review section
        changenotificationtext = notificationtext.upper()
        if self._driver.find_elements(*PlaceOrder.notification_text_review)[0].text == changenotificationtext:
            return True
        else:
            return False

    # The following function verifies the subtotal at the checkout page is the subtotal of the selected product
    def check_subtotal(self, accessoryprice, productprice):
        changeproductprice = productprice.split("$")
        if accessoryprice != 0:
            changeaccessoryprice = accessoryprice.split("$")
            subtotalnumber = int(float(changeaccessoryprice[1]) + float(changeproductprice[1]))
        else:
            subtotalnumber = int(float(changeproductprice[1]))
        subtotal = "SUBTOTAL $" + str(subtotalnumber) + ".00"
        if self._driver.find_elements(*PlaceOrder.subtotal_And_salestaxes_And_totalprice)[0].text == subtotal:
            return True
        else:
            return False

    # The following function verifies the sales tax at the checkout page is the sales tax of the selected product
    def check_sales_taxes(self, salestax, productprice):
        # Sales Taxes
        changeproductprice = productprice.split("$")
        subtotalnumber = int(float(changeproductprice[1]))
        changesalestax = round((subtotalnumber * salestax),2)
        changesalestax = "SALES TAX: $" + str(changesalestax)
        if self._driver.find_elements(*PlaceOrder.subtotal_And_salestaxes_And_totalprice)[1].text == changesalestax:
            return True
        else:
            return False

    # The following function verifies the sales tax at the checkout page is the sales tax in the review section of the selected product
    def check_sales_taxes_review(self, salestax, productprice):
        # Also Sales Taxes in the review section
        changeproductprice = productprice.split("$")
        subtotalnumber = int(float(changeproductprice[1]))
        changesalestax = round((subtotalnumber * salestax), 2)
        changesalestax = "$" + str(changesalestax)
        if self._driver.find_elements(*PlaceOrder.sales_taxes_review)[-1].text == changesalestax:
            return True
        else:
            return False

    # The following function verifies the total price at the checkout page is the total price of the selected product
    def check_total_price(self, salestax, accessoryprice, productprice):
        changeproductprice = productprice.split("$")
        if accessoryprice != 0:
            changeaccessoryprice = accessoryprice.split("$")
            subtotalnumber = int(float(changeaccessoryprice[1]) + float(changeproductprice[1]))
        else:
            subtotalnumber = int(float(changeproductprice[1]))
        changesalestax = round((float(changeproductprice[1]) * salestax), 2)
        Totalnumber = changesalestax + subtotalnumber
        Total = "TOTAL: $" + str(Totalnumber)
        if self._driver.find_elements(*PlaceOrder.subtotal_And_salestaxes_And_totalprice)[2].text == Total:
            return True
        else:
            return False

    # The following function verifies the total price at the checkout page is the total price in the review section of the selected product
    def check_total_price_review(self, salestax, accessoryprice, productprice):
        # Also total in the review section
        changeproductprice = productprice.split("$")
        if accessoryprice != 0:
            changeaccessoryprice = accessoryprice.split("$")
            subtotalnumber = int(float(changeaccessoryprice[1]) + float(changeproductprice[1]))
        else:
            subtotalnumber = int(float(changeproductprice[1]))
        changesalestax = round((float(changeproductprice[1]) * salestax), 2)
        Totalnumber = changesalestax + subtotalnumber
        Total = "TOTAL: $" + str(Totalnumber)
        if self._driver.find_elements(*PlaceOrder.total_price_review)[1].text == Total:
            return True
        else:
            return False

    # The following function fills the customer name at the checkout page
    def check_name(self, customername):
        # Name
        self._driver.find_element(*PlaceOrder.name_review1).clear()
        self._driver.find_element(*PlaceOrder.name_review1).send_keys(customername)

    # The following function verifies the customer name at the checkout page is the customer name in the review section of the selected product
    def check_name_review(self, customername):
        # Also name in the review section
        if self._driver.find_element(*PlaceOrder.name_review2).text == customername.upper():
            return True
        else:
            return False

    # The following function fills the phone number at the checkout page
    def fill_phone_number(self, phonenumber):
        # Phone Number
        if phonenumber is not None:
            self._driver.find_element(*PlaceOrder.phone_number).clear()
            self._driver.find_element(*PlaceOrder.phone_number).send_keys(phonenumber)

    # The following function verifies the phone number at the checkout page is the phone number in the review section of the selected product
    def check_phone_number_review(self, phonenumber):
        # Phone Number in the review section
        if phonenumber is not None:
            # Also Phone Number down
            if self._driver.find_element(*PlaceOrder.phone_number_review).text == phonenumber:
                return True
            else:
                return False

    # The following function fills the address at the checkout page
    def fill_address_optional(self, addressoptional, addressoptionalvalue):
        # Address Optional
        if addressoptional is not None:
            self._driver.find_element(*PlaceOrder.address_optional).click()
            addressoptionalvalue_link = self._driver.find_element_by_link_text(addressoptionalvalue)
            addressoptionalvalue_link.click()

    # The following function verifies the address at the checkout page is the address of the selected product
    def check_address_optional(self, addressoptional, addressoptionalvalue):
        # Address Optional
        if addressoptional is not None:
            # Also optional address in the review section
            changeaddressoptional = "address type: " + addressoptionalvalue
            if self._driver.find_element(*PlaceOrder.address_optional_review).text == changeaddressoptional.lower():
                return True
            else:
                return False

    # The following function fills the Zip Code at the checkout page
    def check_zip_code(self, zipcode):
        # Zip Code
        if zipcode is not None:
            self._driver.find_element(*PlaceOrder.zip_code_review1).clear()
            self._driver.find_element(*PlaceOrder.zip_code_review1).send_keys(str(zipcode))

    # The following function verifies the Zip Code at the checkout page is the Zip Code in the review section of the selected product
    def check_zip_code_review(self, zipcode):
        # Also Zip Code in the review section
        if self._driver.find_element(*PlaceOrder.zip_code_review2).text == str(zipcode):
            return True
        else:
            return False

    # The following function fills the address line 1 at the checkout page
    def fill_address_line1(self, addressline1):
        # Address Line 1
        if addressline1 is not None:
            self._driver.find_element(*PlaceOrder.address_line1).clear()
            self._driver.find_element(*PlaceOrder.address_line1).send_keys(addressline1)
            action = ActionChains(self._driver)
            action.send_keys(Keys.ESCAPE)
            action.perform()

    # The following function verifies the address line 1 at the checkout page is the address line 1 in the review section of the selected product
    def check_address_line1_review(self, addressline1):
        if addressline1 is not None:
            # Also Address Line 1 in the review section
            if self._driver.find_element(*PlaceOrder.address_line1_review).text == addressline1:
                return True
            else:
                return False

    # The following function fills the address line 2 at the checkout page
    def fill_address_line2(self, addressline2):
        # Address Line 2
        if addressline2 is not None:
            self._driver.find_element(*PlaceOrder.address_line2).clear()
            self._driver.find_element(*PlaceOrder.address_line2).send_keys(addressline2)

    # The following function verifies the address line 2 at the checkout page is the address line 2 in the review section of the selected product
    def check_address_line2_review(self, addressline2):
        # Address Line 2
        if addressline2 is not None:
            # Also Address Line 2 in the review section
            if self._driver.find_element(*PlaceOrder.address_line2_review).text == addressline2:
                return True
            else:
                return False

    # The following function fills the delivery day at the checkout page of the selected product
    def fill_delivery_date(self, deliveryday):
        # Delivery Date
        if deliveryday is not None:
            Calendar_days = self._driver.find_elements_by_tag_name("span")
            for dayselected in Calendar_days:
                if dayselected.text == str(deliveryday):
                    parentdayselect = dayselected.find_element(By.XPATH, "..")
                    if not parentdayselect.get_attribute("disabled"):
                        dayselected.click()
                        break
                    else:
                        deliveryday = deliveryday +1
            return deliveryday

    # The following function verifies the delivery date at the checkout page is the delivery date in the review section of the selected product
    def check_delivery_date_review(self, deliveryday):
        # Delivery Date
        if deliveryday is not None:
            dateoftoday = date.today()
            changedeliverydate = "delivery date: " + dateoftoday.strftime("%B") + " " + str(deliveryday)
            # Also Delivery Date in the review section
            if self._driver.find_element(*PlaceOrder.delivery_date_review).text == changedeliverydate:
                return True
            else:
                return False

    # The following function fills the first and last names at the checkout page
    def fill_first_and_last_name(self, firstandlastname):
        if firstandlastname is not None:
            self._driver.find_element(*PlaceOrder.first_and_last_name).clear()
            self._driver.find_element(*PlaceOrder.first_and_last_name).send_keys(firstandlastname)

    # The following function verifies the first and last names at the checkout page are the first and last names in the review section of the selected product
    def check_first_and_last_name_review(self, firstandlastname):
        if firstandlastname is not None:
            # Also first and last name in the review section
            if self._driver.find_element(*PlaceOrder.first_and_last_name_review).text == firstandlastname.upper():
                return True
            else:
                return False

    # The following function fills the delivery Zip Code at the checkout page
    def fill_billing_zip_code(self, billingzipcode):
        # Zip Code
        if billingzipcode is not None:
            self._driver.find_element(*PlaceOrder.billing_zip_code).clear()
            self._driver.find_element(*PlaceOrder.billing_zip_code).send_keys(billingzipcode)

    # The following function verifies the delivery Zip Code at the checkout page is the delivery Zip Code in the review section of the selected product
    def check_billing_zip_code_review(self, billingzipcode):
        # Zip Code
        if billingzipcode is not None:
            # Also billing Zip Code in the review section
            if self._driver.find_element(*PlaceOrder.billing_zip_code_review).text == str(billingzipcode):
                return True
            else:
                return False

    # The following function fills the delivery address line 1 at the checkout page
    def fill_billing_address_l1(self, billingaddressl1):
        if billingaddressl1 is not None:
            self._driver.find_element(*PlaceOrder.billing_address_l1).clear()
            self._driver.find_element(*PlaceOrder.billing_address_l1).send_keys(billingaddressl1)

    # The following function verifies the delivery address line 1 at the checkout page is the delivery address line 1 in the review section of the selected product
    def check_billing_address_l1(self, billingaddressl1):
        if billingaddressl1 is not None:
            # Also billing address 1 in the review section
            if self._driver.find_element(*PlaceOrder.billing_address_l1_review).text == billingaddressl1:
                return True
            else:
                return False

    # The following function fills the delivery address line 2 at the checkout page
    def fill_billing_address_l2(self, billingaddressl2):
        if billingaddressl2 is not None:
            self._driver.find_element(*PlaceOrder.billing_address_l2).clear()
            self._driver.find_element(*PlaceOrder.billing_address_l2).send_keys(billingaddressl2)

    # The following function verifies the delivery address line 2 at the checkout page is the delivery address line 2 in the review section of the selected product
    def check_billing_address_l2(self, billingaddressl2):
        if billingaddressl2 is not None:
            # Also billing address 2 in the review section
            if self._driver.find_element(*PlaceOrder.billing_address_l2_review).text == billingaddressl2:
                return True
            else:
                return False

    # The following function fills the email address at the checkout page
    def fill_email_address(self, emailaddress):
        # Billing Email Address
        if emailaddress is not None:
            self._driver.find_element(*PlaceOrder.email_address).clear()
            self._driver.find_element(*PlaceOrder.email_address).send_keys(emailaddress)

    # The following function verifies the email address at the checkout page is the email address in the review section of the selected product
    def check_email_address(self, emailaddress):
        if emailaddress is not None:
            # Also billing email address in the review section
            if self._driver.find_element(*PlaceOrder.email_address_review).text == emailaddress:
                return True
            else:
                return False

    # The following function fills the phone number at the checkout page
    def fill_billing_phone_number(self, billingphonenumber):
        # Billing Phone Number
        if billingphonenumber is not None:
            self._driver.find_element(*PlaceOrder.billing_phone_number).clear()
            self._driver.find_element(*PlaceOrder.billing_phone_number).send_keys(billingphonenumber)

    # The following function verifies the phone number at the checkout page is the phone number in the review section of the selected product
    def check_billing_phone_number(self, billingphonenumber):
        if billingphonenumber is not None:
            # Also billing phone number in the review section
            if self._driver.find_element(*PlaceOrder.billing_phone_number_review).text == billingphonenumber:
                return True
            else:
                return False

    # The following function verifies if the sms notification required and check it at the checkout page
    def check_sms_notification(self, smsnotification):
        if smsnotification == "Yes":
            # Check the checkbox
            self._driver.find_element(*PlaceOrder.sms_notification).click()

    # The following function verifies if there is a promotion code and apply it  at the checkout page
    def fill_olyve_premiere_code(self, olyvepremierecode, promotioncodetext, accessoryprice, salestax, productprice, discounttext):
        if olyvepremierecode is not None and (olyvepremierecode == 'nope' or olyvepremierecode == 'beauty10' or olyvepremierecode == 'Bonkers!'):
            getcontext().rounding = ROUND_DOWN
            TWOPLACES = Decimal(10) ** -2
            changeproductprice = productprice.split("$")
            if accessoryprice != 0:
                changeaccessoryprice = accessoryprice.split("$")
                subtotalnumber = int(float(changeaccessoryprice[1]) + float(changeproductprice[1]))
            else:
                subtotalnumber = int(float(changeproductprice[1]))

            changesalestax = Decimal(float(changeproductprice[1]) * salestax).quantize(TWOPLACES)
            Totalnumber = changesalestax + subtotalnumber
            Total = "TOTAL: $" + str(Totalnumber)
            self._driver.find_element(*PlaceOrder.olyve_premiere_code).click()
            self._driver.find_element(*PlaceOrder.code).send_keys(olyvepremierecode)
            self._driver.find_element(*PlaceOrder.apply_olyve_premeier_code).click()
            time.sleep(15)
            if olyvepremierecode == 'nope':
                if self._driver.find_element(*PlaceOrder.promo_code_applied).text == promotioncodetext:
                    if self._driver.find_elements(*PlaceOrder.total_price_review)[1].text == Total:
                        return True
                    else:
                        return False
                else:
                    return False
            elif olyvepremierecode == 'beauty10':
                if self._driver.find_element(*PlaceOrder.promo_code_applied).text == promotioncodetext:
                    if self._driver.find_elements(*PlaceOrder.discount_review)[-2].text == discounttext.upper():
                        discountvalue = Decimal(subtotalnumber * 0.1).quantize(TWOPLACES)
                        salestaxafterdiscount = Decimal(float(changesalestax) * 0.9).quantize(TWOPLACES)
                        subtotalnumberafterdiscount = subtotalnumber - discountvalue
                        totalnumberafterdiscount = subtotalnumberafterdiscount + salestaxafterdiscount
                        changesubtotalnumber = '- $' + str(discountvalue)
                        if self._driver.find_elements(*PlaceOrder.discount_value_review)[-2].text == changesubtotalnumber:
                            changetotalafterdiscount = "TOTAL: $" + str(totalnumberafterdiscount)
                            if self._driver.find_elements(*PlaceOrder.total_price_review)[1].text == changetotalafterdiscount:
                                return True
                            else:
                                return False
                        return False
                    return False
                return False
            else:
                if self._driver.find_element(*PlaceOrder.promo_code_applied).text == promotioncodetext:
                    if self._driver.find_elements(*PlaceOrder.discount_review)[-2].text == discounttext.upper():
                        discountvalue = Decimal(subtotalnumber).quantize(TWOPLACES)
                        discountvalueonsalestax = Decimal(changesalestax).quantize(TWOPLACES)
                        changesubtotalnumber = '- $' + str(discountvalue)
                        if self._driver.find_elements(*PlaceOrder.discount_value_review)[-2].text == changesubtotalnumber:
                            changeTotalvalue = Totalnumber - discountvalue - discountvalueonsalestax
                            changeTotal = "TOTAL: $" + str(changeTotalvalue)
                            if self._driver.find_elements(*PlaceOrder.total_price_review)[1].text == changeTotal:
                                if not (self._driver.find_element(*PlaceOrder.credit_card_number).is_displayed() and
                                        self._driver.find_element(*PlaceOrder.credit_card_month).is_displayed() and
                                        self._driver.find_element(*PlaceOrder.credit_card_year).is_displayed() and
                                        self._driver.find_element(*PlaceOrder.credit_card_ccv).is_displayed()):
                                    return True
                                else:
                                    return False
                            else:
                                return False
                        return False
                    return False
                return False
        else:
            return True

    # The following function fills the Credit Card Number, Month, Year, CCV at the checkout page
    def fill_credit_card_details(self, creditcardnumber, creditcardmonth, creditcardyear, creditcardccv):
        if creditcardnumber is not None and creditcardmonth is not None and creditcardyear is not None and creditcardccv is not None:
            self._driver.find_element(*PlaceOrder.credit_card_number).clear()
            self._driver.find_element(*PlaceOrder.credit_card_number).send_keys(creditcardnumber)

            self._driver.find_element(*PlaceOrder.credit_card_month).clear()
            self._driver.find_element(*PlaceOrder.credit_card_month).send_keys(creditcardmonth)

            self._driver.find_element(*PlaceOrder.credit_card_year).clear()
            self._driver.find_element(*PlaceOrder.credit_card_year).send_keys(creditcardyear)

            self._driver.find_element(*PlaceOrder.credit_card_ccv).clear()
            self._driver.find_element(*PlaceOrder.credit_card_ccv).send_keys(creditcardccv)

    # The following function verifies the message at the checkout page is the message in the review section of the selected product
    def check_message_review(self, message):
        # Also check the message in the review section
        if self._driver.find_element(*PlaceOrder.message_review).text == message:
            return True
        else:
            return False

    # The following function verifies the message signature at the checkout page is the message signature in the review section of the selected product
    def check_signature_review(self, signature):
        # Also check the signature in the review section
        if self._driver.find_element(*PlaceOrder.message_review).text == signature:
            return True
        else:
            return False

    # The following function verifies the Video/Photo uploaded at the checkout page
    def check_videophoto_review(self, videolocation, photolocation, videophotopageurl):
        # Also check the image and video in the review section
        if videolocation is not None or photolocation is not None:
            # Clicks the Link of the Photo/Video uploaded in the checkout page
            self._driver.find_element(*PlaceOrder.gift_image_video).click()
            # Wait for the Gift Photo/Video Page to load
            PageActions.BasicActions.explicit_wait(self, 40, PlaceOrder.videophoto_load)
            current_url = self._driver.current_url
            if current_url == videophotopageurl:
                # Check the video uploaded in the Message Page is the Video displayed in the Gift Photo/Video Page
                if videolocation is not None:
                    iframe = self._driver.find_elements_by_tag_name('iframe')[0]
                    self._driver.switch_to_frame(iframe)
                    if self._driver.find_element(*PlaceOrder.video_upload_review).is_displayed():
                        self._driver.switch_to_default_content()
                        return True
                    else:
                        return False
                else:
                    # Check the photo uploaded in the Message Page is the photo displayed in the Gift Photo/Video Page
                    if photolocation is not None:
                        if self._driver.find_element(*PlaceOrder.image_upload_review).is_displayed():
                            return True
                        else:
                            return False
            else:
                return False
        else:
            return True

    # The following function clicks on the Buy button and check the alerts that could be displayed
    def Buy_click(self, message, deliveryday):
        self._driver.find_element(*PlaceOrder.Buy_button).click()
        # Check if the message is empty an alert is displayed and the user in this case is not forgotting the message
        if message is None:
            if self._driver.find_element(*PlaceOrder.CardMessageDialog).is_displayed():
                self._driver.switch_to_alert()
                PageActions.BasicActions.dismiss_alert()
                PageActions.BasicActions.implicit_wait(50)

    # The following function verifies that there is an Order ID generated
    def check_confirmation_number(self):
        # Confirmation Number
        self._driver.find_element(*PlaceOrder.confirmation_number)

    # The following function verifies the customer name ordering the selected product in the Order Details Page
    def check_name_order_details(self, name):
        # Name
        if self._driver.find_element(*PlaceOrder.name_review_order_details).text == name:
            return True
        else:
            return False

    # The following function verifies the detailed address line 1 for recipient of the selected product in the Order Details Page
    def check_address_line1_order_details(self, addressline1):
        changeaddressline1 = addressline1.split(",")
        # Address doesn't contain any comma
        if len(changeaddressline1) == 1:
            if self._driver.find_element(*PlaceOrder.address_line1_review_order_details).text == addressline1:
                return True
            else:
                return False
        # Address Contains 3 Commas and we only check on the first part of the address
        if len(changeaddressline1) == 4:
            if self._driver.find_element(*PlaceOrder.address_line1_review_order_details).text == changeaddressline1[0]:
                return True
            else:
                return False

    # The following function verifies the detailed address line 2 for recipient of the selected product in the Order Details Page
    def check_address_line2_order_details(self, addressline2):
        if self._driver.find_element(*PlaceOrder.address_line2_review_order_details).text == addressline2:
            return True
        else:
            return False

    # The following function verifies the Zip Code for the order of the selected product in the Order Details Page
    def check_zip_code_order_details(self, zipcode):
        if self._driver.find_element(*PlaceOrder.zip_code_review_order_details).text == str(zipcode):
            return True
        else:
            return False

    # The following function verifies the delivery date for the order of the selected product in the Order Details Page
    def check_delivery_date_order_details(self, deliveryday):
        dateoftoday = date.today()
        changedeliverydate = "Delivery Date: " + dateoftoday.strftime("%B") + " " + str(deliveryday) + ", " + dateoftoday.strftime("%G")
        if self._driver.find_element(*PlaceOrder.delivery_date_review_order_details).text == changedeliverydate:
            return True
        else:
            return False

    # The following function verifies the Questions/Concerns Contact of OLYVE
    def check_questions_and_concerns_oder_details(self, questionsandconcerns):
        # Questions & Concerns
        changequestionsandconcerns = "Questions/Concerns: " + questionsandconcerns
        if self._driver.find_element(*PlaceOrder.questions_and_concenrs).text == changequestionsandconcerns:
            return True
        else:
            return False

    # The following function verifies if and updates required via text using PIN for the order of the selected product in the Order Details Page
    def check_updates_via_text_order_details (self, updatesviatext):
        if updatesviatext == "Yes":
            # Updates Via Text
            self._driver.find_element(*PlaceOrder.updates_via_text)
            # Submit
            self._driver.find_element(*PlaceOrder.submit).click()
        else:
            # Return to Home Page
            self._driver.find_element(*PlaceOrder.return_home).click()

    # Home Page Load should wait for Header Olyve Logo to be loaded in the Home Page
    def wait_for_header_olyve_logo(self):
        return PageActions.BasicActions.explicit_wait(self, 40, PlaceOrder.header_olyve_logo)

    # Product check should wait for Product Page to be loaded
    def wait_for_product_page(self):
        return PageActions.BasicActions.explicit_wait(self, 40, PlaceOrder.pick_me_button)

    # Accessory check should wait for Accessory Page to be loaded
    def wait_for_accessory_page(self):
        return PageActions.BasicActions.explicit_wait(self, 40, PlaceOrder.accessory_load)

    # Message check should wait for Message Page to be loaded
    def wait_for_message_page(self):
        return PageActions.BasicActions.explicit_wait(self, 40, PlaceOrder.message_load)

    # Checkout check should wait for Checkout Page to be loaded
    def wait_for_checkout_page(self):
        return PageActions.BasicActions.explicit_wait(self, 40, PlaceOrder.checkout_load)

    # Order Details check should wait for Order Details Page to be loaded
    def wait_for_order_details_page(self):
        return PageActions.BasicActions.explicit_wait(self, 40, PlaceOrder.orderdetails_load)

    # Wait for Accessory text in checkout Page in case order has accessory
    def wait_for_accessory_text(self):
        return PageActions.BasicActions.explicit_wait(self, 40, PlaceOrder.accessory_text)

    # Go to Home Page.
    def go_to_hompage(self):
        self._driver.find_element(*PlaceOrder.return_home).click()


    # This function checks if there is an accessory section in checkout page or not
    def is_accessory_section_exist_checkout_page(self):
        if self._driver.find_element(*PlaceOrder.accessory_section).get_attribute('data-item-is-accessory') == "true":
            return True
