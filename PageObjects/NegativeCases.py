from selenium.webdriver.common.by import By

class NegativeCases(object):
    product_image = (By.XPATH, 'html/body/div[1]/div/div/div[2]/div[1]/div[1]/div/div/div/div[1]/olv-image/div/img')
    pick_me_button = (By.XPATH, 'html/body/div[1]/div/div/div[2]/div[2]/div[5]/div/div')
    close_pick_me_dialog = (By.CSS_SELECTOR, '.ngdialog-close')
    name_field = (By.XPATH, 'html/body/div[1]/div/div/div[2]/div[2]/div[6]/div/div[1]/form/div[2]/div/div[2]/div/input')
    zip_code_field = (By.XPATH, 'html/body/div[1]/div/div/div[2]/div[2]/div[6]/div/div[1]/form/div[4]/div/div[2]/div/input')
    Go_button = (By.XPATH,'html/body/div[1]/div/div/div[2]/div[2]/div[6]/div/div[1]/form/div[5]/div/a')
    error_zip_code_message_body = (By.XPATH, 'html/body/div[3]/div[2]/div/div/div[2]/div/p')
    error_zip_code_message_header = (By.XPATH, 'html/body/div[3]/div[2]/div/div/div[1]/div')
    error_zip_code_message_OK = (By.XPATH, 'html/body/div[3]/div[2]/div/div/div[3]/div/a')
    error_message_invalid_zip_code = (By.XPATH, 'html/body/div[1]/div/div/div[2]/div[2]/div[6]/div/div[1]/form/div[4]/div/div[2]/div/span')
    error_message_missing_name_zipcode = (By.CSS_SELECTOR, '.errormsg')
    error_message_invalid_name = (By.XPATH, 'html/body/div[1]/div/div/div[2]/div[2]/div[6]/div/div[1]/form/div[2]/div/div[2]/div/span')

    def __init__(self, driver):
        self._driver = driver

    def product_image_click(self):
        if self._driver.find_element(*NegativeCases.pick_me_button).is_displayed():
            self._driver.find_element(*NegativeCases.product_image).click()
            if not (self._driver.find_element(*NegativeCases.pick_me_button).is_displayed()):
                self._driver.find_element(*NegativeCases.close_pick_me_dialog).click()
                if self._driver.find_element(*NegativeCases.pick_me_button).is_displayed():
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def no_name_zipdode(self, error_missing_name_zipcode, error_missing_name):
        self._driver.find_element(*NegativeCases.zip_code_field).click()
        self._driver.find_element(*NegativeCases.name_field).click()
        if (self._driver.find_element(*NegativeCases.error_message_missing_name_zipcode).is_displayed()) and (self._driver.find_element(*NegativeCases.error_message_missing_name_zipcode).text == error_missing_name):
            return True
        else:
            return False

    def invalid_name(self, valid_zipcode, invalid_name, error_invalid_name):
        self._driver.find_element(*NegativeCases.zip_code_field).clear()
        self._driver.find_element(*NegativeCases.name_field).clear()
        self._driver.find_element(*NegativeCases.name_field).send_keys(invalid_name)
        self._driver.find_element(*NegativeCases.zip_code_field).send_keys(valid_zipcode)
        self._driver.find_element(*NegativeCases.Go_button).click()
        if self._driver.find_element(*NegativeCases.error_message_invalid_zip_code).text == error_invalid_name:
            return True
        else:
            return False

    def invalid_zip_code(self, valid_name, invalid_zip_code, error_invalid_zip_code):
        self._driver.find_element(*NegativeCases.zip_code_field).clear()
        self._driver.find_element(*NegativeCases.name_field).clear()
        self._driver.find_element(*NegativeCases.name_field).send_keys(valid_name)
        self._driver.find_element(*NegativeCases.zip_code_field).send_keys(invalid_zip_code)
        if self._driver.find_element(*NegativeCases.error_message_invalid_zip_code).text == error_invalid_zip_code:
            return True
        else:
            return False

    def unsupported_zip_code(self, valid_name, unsupported_zip_code, errormessageheader, errormessagebody):
        self._driver.find_element(*NegativeCases.zip_code_field).clear()
        self._driver.find_element(*NegativeCases.name_field).clear()
        self._driver.find_element(*NegativeCases.name_field).send_keys(valid_name)
        self._driver.find_element(*NegativeCases.zip_code_field).send_keys(unsupported_zip_code)
        self._driver.find_element(*NegativeCases.Go_button).click()
        if self._driver.find_element(*NegativeCases.error_zip_code_message_header).is_displayed():
            if (self._driver.find_element(*NegativeCases.error_zip_code_message_header).text == errormessageheader) and (self._driver.find_element(*NegativeCases.error_zip_code_message_body).text == errormessagebody):
                self._driver.find_element(*NegativeCases.error_zip_code_message_OK).click()
                return True
            else:
                return False
        else:
            return False