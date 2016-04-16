from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Utilities import PageActions


class HomePage(object):
    # Olyve Logo located in the Header of the Home page
    header_olyve_logo = (By.ID, 'header-logo')
    # Shop Button located in the Header of the Home page
    header_shop_button = (By.CSS_SELECTOR, '.olyve-nav.nav-left>ul>li:first-child')
     # The Olyve Experience Button located in the Header of the Home page
    header_theOlyveExperience_button = (By.CSS_SELECTOR, '.olyve-nav.nav-left>ul>li:nth-child(2n)')
    # From Our Customer Button in the Olyve Exprience Page
    from_our_customer_button = (By.XPATH, 'html/body/div[1]/div[5]/div/div/a[1]/div')
    # Shop Collection button in the Olyve Exprience Page
    shop_the_collection_button = (By.XPATH, 'html/body/div[1]/div[5]/div/div/a[2]/div')
    # Shop Collection button in the From Our Customer Page
    shop_the_collection_button_customer = (By.XPATH, 'html/body/div/div[6]/div/div/a[2]/div')
    # From Our Customers Button located in the Header of the Home page
    header_fromOurCustomers_button = (By.CSS_SELECTOR, '.olyve-nav.nav-left>ul>li:nth-child(3n)')
    # Track Button located in the Header of the Home page
    header_track_button = (By.CSS_SELECTOR, '.olyve-nav.nav-right>ul>li:last-child')
    # The Order ID field located in Track Page
    order_id_track = (By.CSS_SELECTOR, '.ng-pristine.ng-untouched.ng-invalid.ng-invalid-required.ng-valid-maxlength')
    # Service Button located in the Header of the Home page
    header_service_button = (By.CSS_SELECTOR, '.olyve-nav.nav-right>ul>li:nth-child(3n)')
    # The verify button located in the Service page
    verify_order_id = (By.XPATH, 'html/body/div[1]/div/div/div/div[3]/div[1]/div[2]/div/a')
    # The Order ID field located in Service Page
    order_id_service = (By.XPATH, 'html/body/div[1]/div/div/div/div[3]/div[1]/div[1]/div/input')
    # The Pin Code field located in Service Page
    pin_code_service = (By.XPATH, 'html/body/div[1]/div/div/div/div[3]/div[2]/div[1]/div/input')
    # The Confirm button located in Service Page
    confirm_order_id_service = (By.XPATH, 'html/body/div[1]/div/div/div/div[3]/div[2]/div[2]/div/a')
    # Workshops Button located in the Header of the Home page
    header_workshops_button = (By.CSS_SELECTOR, '.olyve-nav.nav-right>ul>li:nth-child(3n+2)')
    # Social Button located in the Header of the Home page
    header_social_button = (By.CSS_SELECTOR, '.olyve-nav.nav-right>ul>li:first-child')
    # Message Ribbon located under the Olyve Logo "gift box & delivery always included"
    header_message_ribbon = (By.XPATH, 'html/body/div[1]/div/div/div[1]/div')
    # Olyve 3 Slides located at the top of the Home page
    first_products_slide = (By.CSS_SELECTOR, '.carousel-indicators>li:first-child')
    second_products_slide = (By.CSS_SELECTOR, '.carousel-indicators>li:nth-child(2n)')
    third_products_slide = (By.CSS_SELECTOR, '.carousel-indicators>li:last-child')
    # Shop Button located at the Home page's sildes
    shop_button_second_slide = (By.XPATH, '//*[@id="products-slider"]/div/div/div/div[2]/div/a')
    shop_button_third_slide = (By.XPATH, '//*[@id="products-slider"]/div/div/div/div[3]/div/a')
    # Olyve Copyrigth link located at the bottom of the Home page
    footer_copyright = (By.XPATH, 'html/body/div[1]/div/olv-footer/div/div[2]/div/div[1]/div[1]/div')
    # Olyve Privacy Terms link located at the bottom of the Home page
    footer_privacyterms = (By.XPATH, 'html/body/div[1]/div/olv-footer/div/div[2]/div/div[1]/div[2]/div/a')
    # Olyve Code of Conduct link located at the bottom of the Home page
    footer_codeofconduct = (By.XPATH, 'html/body/div[1]/div/olv-footer/div/div[2]/div/div[1]/div[3]/div/a')
    # Olyve Contact Phone Number located at the bottom of the Home page
    footer_phonenumber = (By.XPATH, 'html/body/div[1]/div/olv-footer/div/div[2]/div/div[2]/div[1]/div/a')
    # Olyve Contact Service Email located at the bottom of the Home page
    footer_serviceemail = (By.XPATH, 'html/body/div[1]/div/olv-footer/div/div[2]/div/div[2]/div[2]/div/a')
    # Olyve Social Links located at the bottom of the Home page
    facebook_link = (By.CSS_SELECTOR, '.col-xs-12.text-center>a:first-child')
    instgram_link = (By.CSS_SELECTOR, '.col-xs-12.text-center>a:nth-child(3n+2)')
    pinterest_link = (By.CSS_SELECTOR, '.col-xs-12.text-center>a:nth-child(2n+3)')
    twitter_link = (By.CSS_SELECTOR, '.col-xs-12.text-center>a:last-child')
    # Explicit Wait Objects to be loaded
    product_image = (By.XPATH, "html/body/div/div/div/div[4]/div/div/div/div[5]/a/olv-image/div/img")
    facebook_load = (By.ID, 'pagelet_bluebar')
    instgram_load = (By.CSS_SELECTOR, '._jvpff._k2yal._csba8._i46jh._nv5lf')
    pinterest_load = (By.CSS_SELECTOR, '.nameInner')
    twitter_load = (By.CSS_SELECTOR, '.ProfileAvatar-image')
    pick_me_button = (By.XPATH, "html/body/div[1]/div/div/div[2]/div[2]/div[5]/div/div")
    track_load = (By.CSS_SELECTOR, '.goContainer>a')
    workshop_load = (By.CSS_SELECTOR, '#submitNewsletter')
    service_load = (By.XPATH, 'html/body/div[1]/div/div/div/div[3]/div[1]/div[2]/div/a')

    def __init__(self, driver):
        self._driver = driver

    # The following function checks if Olyve logo is displayed
    def is_logo_displayed(self):
        return self._driver.find_element(*HomePage.header_olyve_logo).is_displayed()

    # The following function checks if header shop button is enabled
    def is_header_shop_button_enabled(self):
        return self._driver.find_element(*HomePage.header_shop_button).is_enabled()

    # The following function checks if header The Olyve Experience button is enabled
    def is_header_theolyveexperience_button_enabled(self):
        return self._driver.find_element(*HomePage.header_theOlyveExperience_button).is_enabled()

    # The following function checks if header From Our Customers button is enabled
    def is_header_fromourcustomers_button_enabled(self):
        return self._driver.find_element(*HomePage.header_fromOurCustomers_button).is_enabled()

    # The following function checks if Track button is enabled
    def is_header_track_button_enabled(self):
        return self._driver.find_element(*HomePage.header_track_button).is_enabled()

    # The following function checks if header Service button is enabled
    def is_header_service_button_enabled(self):
        return self._driver.find_element(*HomePage.header_service_button).is_enabled()

    # The following function checks if header Workshops button is enabled
    def is_header_workshops_button_enabled(self):
        return self._driver.find_element(*HomePage.header_workshops_button).is_enabled()

    # The following function checks if header Social button is enabled
    def is_header_social_button_enabled(self):
        return self._driver.find_element(*HomePage.header_social_button).is_enabled()

    # The following function check if the page scroll down when click on Header Shop button in order to select a Product
    def shop_button_click(self):
        self._driver.find_element(*HomePage.header_shop_button).click()
        if PageActions.BasicActions.window_scroll_top(self) > 0:
            return True

    # The following function returns URL of the Olyve Exprience page opened
    def olyve_experience_button_click(self):
        self._driver.find_element(*HomePage.header_theOlyveExperience_button).click()
        PageActions.BasicActions.explicit_wait(self, 40,HomePage.shop_the_collection_button)
        return self._driver.current_url

    # The following function returns URL of the Our Customer page opened
    def from_our_customer_button_click(self):
        self._driver.find_element(*HomePage.header_fromOurCustomers_button).click()
        PageActions.BasicActions.explicit_wait(self, 40,HomePage.shop_the_collection_button_customer)
        return self._driver.current_url

    # The following function returns URL of the Track page opened and track an Order ID
    def track_button_click(self, OrderID):
        self._driver.find_element(*HomePage.header_track_button).click()
        if PageActions.BasicActions.explicit_wait(self, 40,HomePage.track_load):
            curent_url = self._driver.current_url
            self._driver.find_element(*HomePage.order_id_track).send_keys(OrderID)
            self._driver.find_element(*HomePage.track_load).click()
            return curent_url

    # The following function returns URL of the Service page opened
    def service_button_click(self, OrderID, PinCode):
        self._driver.find_element(*HomePage.header_service_button).click()
        PageActions.BasicActions.explicit_wait(self, 40, HomePage.service_load)
        curent_url = self._driver.current_url
        self._driver.find_element(*HomePage.order_id_service).send_keys(OrderID)
        self._driver.find_element(*HomePage.verify_order_id).click()
        #self._driver.find_element(*HomePage.pin_code_service).send_keys(PinCode)
        #self._driver.find_element(*HomePage.confirm_order_id_service).click()
        return curent_url

    # The following function returns URL of the Workshop page opened
    def workshop_button_click(self):
        self._driver.find_element(*HomePage.header_workshops_button).click()
        PageActions.BasicActions.explicit_wait(self, 40,HomePage.workshop_load)
        return self._driver.current_url

    # The following function check if the page scroll down when click on Header Social button in order to navigate to social links at the bottom of the page
    def social_button_click(self):
        self._driver.find_element(*HomePage.header_social_button).click()
        if PageActions.BasicActions.window_scroll_top(self) > 0:
            return True

    # The following function returns URL of the Ingram page opened when clicked on Shop button of the second slide
    def shop_button_second_slide_click(self):
        self._driver.find_element(*HomePage.second_products_slide).click()
        action = ActionChains(self._driver)
        action.key_down(Keys.SHIFT)
        action.click(self._driver.find_element(*HomePage.shop_button_second_slide))
        action.key_up(Keys.SHIFT)
        action.perform()

    # The following function check if the page scroll down when click on Shop button of the third slide in order to select a Product
    def shop_button_third_slide_click(self):
        self._driver.find_element(*HomePage.third_products_slide).click()
        self._driver.find_element(*HomePage.shop_button_third_slide).click()
        if PageActions.BasicActions.window_scroll_top(self) > 0:
            return True

    # The following function returns header ribbon message
    def get_header_ribbon_message(self):
        return self._driver.find_element(*HomePage.header_message_ribbon).text

    # The following function clicks on the first slide and return it
    def click_on_first_slide(self):
        self._driver.find_element(*HomePage.first_products_slide).click()
        return self._driver.find_element(*HomePage.first_products_slide)

    # The following function clicks on the second slide and return it
    def click_on_second_slide(self):
        self._driver.find_element(*HomePage.second_products_slide).click()
        return self._driver.find_element(*HomePage.second_products_slide)

    # The following function clicks on the third slide and return it
    def click_on_third_slide(self):
        self._driver.find_element(*HomePage.third_products_slide).click()
        return self._driver.find_element(*HomePage.third_products_slide)

    # The following function verifies that slides class tag contains "active"
    def verify_slide_is_active(self, selected_slide):
        slide_class = selected_slide.get_attribute('class')
        active_class = "active"
        if active_class == slide_class:
            return True
        else:
            return False

    # The following function returns footer copyright text
    def get_footer_copyright_text(self):
        return self._driver.find_element(*HomePage.footer_copyright).text

     # The following function returns footer privacy terms text
    def get_footer_privacyterms_text(self):
        return self._driver.find_element(*HomePage.footer_privacyterms).text

    # The following function returns URL of the privacy terms page opened
    def get_privacyterms_url(self):
        self._driver.find_element(*HomePage.footer_privacyterms).click()
        WebDriverWait(self._driver, 40).until(EC.title_contains("privacy"))
        return self._driver.current_url

    # The following function returns footer code of conduct text
    def get_footer_codeofconduct_text(self):
        return self._driver.find_element(*HomePage.footer_codeofconduct).text

    # The following function returns URL of the code of conduct
    def get_codeofconduct_url(self):
        self._driver.find_element(*HomePage.footer_codeofconduct).click()
        WebDriverWait(self._driver, 40).until(EC.title_contains("codeofconduct"))
        return self._driver.current_url

    # The following function returns the footer phone number
    def get_footer_phonenumber_text(self):
        return self._driver.find_element(*HomePage.footer_phonenumber).text

    # The following function verifies phone number tag contains "tel:"
    def verify_phonenumber_href(self):
        phonenumberhref = self._driver.find_element(*HomePage.footer_phonenumber).get_attribute('href')
        phonenumber = "tel:"
        if phonenumber in phonenumberhref:
            return True
        else:
            return False

    # The following function returns the footer service email
    def get_footer_serviceemail_text(self):
        return self._driver.find_element(*HomePage.footer_serviceemail).text

    # The following function verifies service mail tag contains "mailto:"
    def verify_serviceamil_href(self):
        servicemailhref = self._driver.find_element(*HomePage.footer_serviceemail).get_attribute('href')
        servicemail = "mailto:"
        if servicemail in servicemailhref:
            return True
        else:
            return False

    # The following function clicks on Facebook social link and opened the corresponding page in a new tab
    def facebook_social_info(self):
        # Create an Instance from ActionChains
        action = ActionChains(self._driver)
        # Find the Facebook link in the home page then click on the link found
        self._driver.find_element(*HomePage.facebook_link)
        # The below steps are used to open the facebook_link in a new window instead of a new tab
        action.key_down(Keys.SHIFT)
        action.click(self._driver.find_element(*HomePage.facebook_link))
        action.key_up(Keys.SHIFT)
        action.perform()

    # The following function clicks on Instgram social link and opened the corresponding page in a new tab
    def instgram_social_info(self):
        # Create an Instance from ActionChains
        action = ActionChains(self._driver)
        # Find the Instgram link in the home page then click on it
        self._driver.find_element(*HomePage.instgram_link)
        # The below steps are used to open the facebook_link in a new window instead of a new tab
        action.key_down(Keys.SHIFT)
        action.click(self._driver.find_element(*HomePage.instgram_link))
        action.key_up(Keys.SHIFT)
        action.perform()

    # The following function clicks on Pinterest social link and opened the corresponding page in a new tab
    def pinterest_social_info(self):
        # Create an Instance from ActionChains
        action = ActionChains(self._driver)
        # Find the Pinterest link in the home page then click on it
        self._driver.find_element(*HomePage.pinterest_link)
        # The below steps are used to open the facebook_link in a new window instead of a new tab
        action.key_down(Keys.SHIFT)
        action.click(self._driver.find_element(*HomePage.pinterest_link))
        action.key_up(Keys.SHIFT)
        action.perform()

    # The following function clicks on Twitter social link and opened the corresponding page in a new tab
    def twitter_social_info(self):
        # Create an Instance from ActionChains
        action = ActionChains(self._driver)
        # Find the Twitter link in the home page then click on it
        self._driver.find_element(*HomePage.twitter_link)
        # The below steps are used to open the facebook_link in a new window instead of a new tab
        action.key_down(Keys.SHIFT)
        action.click(self._driver.find_element(*HomePage.twitter_link))
        action.key_up(Keys.SHIFT)
        action.perform()

    # The following function finds available Products in Olyve and make sure that all products are clickable
    def findproductandclick(self, Index):
        try:
            res = []
            elem = WebDriverWait(driver=self._driver, timeout=5).until(
                EC.presence_of_all_elements_located(locator=(By.CLASS_NAME, "name")))
            res.append(elem[Index].text)
            product_link = self._driver.find_element_by_link_text(elem[Index].text)
            product_link.click()
        except:
            raise Exception("Product Not Found")

    # The following function gets count of all available Products in Olyve
    def get_product_count(self):
        elem = WebDriverWait(driver=self._driver, timeout=5).until(EC.presence_of_all_elements_located(locator=(By.CLASS_NAME, "name")))
        prod_count = len(elem)
        return prod_count

    # The following function waits for Header Olyve Logo to be loaded in the Home Page
    def wait_for_header_olyve_logo(self):
        return PageActions.BasicActions.explicit_wait(self, 40, HomePage.header_olyve_logo)

    # The following function waits for Product images to be loaded in the Home Page
    def wait_for_product_image_load(self):
        return PageActions.BasicActions.explicit_wait(self, 40, HomePage.product_image)

    # The following function waits for Facebook Page to be loaded
    def wait_for_facebook_page_load(self):
        return PageActions.BasicActions.explicit_wait(self, 40, HomePage.facebook_load)

    # The following function waits for Instgram Page to be loaded
    def wait_for_instgram_page_load(self):
        return PageActions.BasicActions.explicit_wait(self, 40, HomePage.instgram_load)

    # The following function waits for Pinterset Page to be loaded
    def wait_for_pinterstet_page_load(self):
        return PageActions.BasicActions.explicit_wait(self, 40, HomePage.pinterest_load)

    # The following function waits for Twitter Page to be loaded
    def wait_for_twitter_page_load(self):
        return PageActions.BasicActions.explicit_wait(self, 40, HomePage.twitter_load)

    # The following function waits for Product Page to be loaded
    def wait_for_product_page(self):
        return PageActions.BasicActions.explicit_wait(self, 40, HomePage.pick_me_button)
