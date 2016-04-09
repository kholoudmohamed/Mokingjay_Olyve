from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Utilities import PageActions


class HomePage(object):
    # Olyve Logo located in the Header of the Home page
    header_olyve_logo = (By.XPATH, 'html/body/div[1]/div/olv-header/nav/div[1]/div[2]/a/img')
    # Olyve Shop Button located in the Header of the Home page
    header_shop_button = (By.XPATH, 'html/body/div[1]/div/olv-header/nav/div[1]/div[1]/ul/li/a')
    # Olyve Track Button located in the Header of the Home page
    header_track_button = (By.XPATH, 'html/body/div[1]/div/olv-header/nav/div[1]/div[4]/ul/li/a')
    # Olyve Message Ribbon located under the Olyve Logo "gift box & delivery always included"
    header_message_ribbon = (By.XPATH, 'html/body/div[1]/div/div/div[1]/div')
    # Olyve 3 Slides located at the top of the Home page
    first_products_slide = (By.XPATH, '//*[@id="products-slider"]/div/div/ol/li[1]')
    second_products_slide = (By.XPATH, '//*[@id="products-slider"]/div/div/ol/li[2]')
    third_products_slide = (By.XPATH, '//*[@id="products-slider"]/div/div/ol/li[3]')
    # Shop Button located at the Home page's sildes
    shop_bottn_second_slide = (By.XPATH, '//*[@id="products-slider"]/div/div/div/div[2]/div/a')
    shop_bottn_third_slide = (By.XPATH, '//*[@id="products-slider"]/div/div/div/div[3]/div/a')
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
    facebook_link = (By.XPATH, "html/body/div[1]/div/olv-social/div/div[2]/div/a[1]")
    instgram_link = (By.XPATH, "html/body/div[1]/div/olv-social/div/div[2]/div/a[2]/i")
    pinterest_link = (By.XPATH, "html/body/div[1]/div/olv-social/div/div[2]/div/a[3]/i")
    twitter_link = (By.XPATH, "html/body/div[1]/div/olv-social/div/div[2]/div/a[4]/i")
    # Explicit Wait Objects to be loaded
    product_image = (By.XPATH, "html/body/div/div/div/div[4]/div/div/div/div[5]/a/olv-image/div/img")
    facebook_load = (By.ID, "pagelet_bluebar")
    instgram_load = (By.XPATH, ".//*[@id='react-root']/section/main/article/header/div[2]/div[1]/span/button")
    pinterest_load = (By.XPATH, "html/body/div[1]/div[3]/div[1]/div[2]/div[2]/div/div/div[3]/div/div/h1/div")
    twitter_load = (By.XPATH, ".//*[@id='page-container']/div[1]/div/div[1]/div[2]/div[1]/div/a/img")
    pick_me_button = (By.XPATH, "html/body/div[1]/div/div/div[2]/div[2]/div[5]/div/div")

    def __init__(self, driver):
        self._driver = driver

    # The following function checks if Olyve logo is displayed
    def is_logo_displayed(self):
        return self._driver.find_element(*HomePage.header_olyve_logo).is_displayed()

    # The following function checks if header shop button is enabled
    def is_header_shop_button_enabled(self):
        return self._driver.find_element(*HomePage.header_shop_button).is_enabled()

    # The following function checks if Track button is enabled
    def is_header_track_button_enabled(self):
        return self._driver.find_element(*HomePage.header_track_button).is_enabled()

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
