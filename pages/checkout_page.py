from selenium.webdriver.common.by import By
from utils.generator_function import generate_nick
from utils.generator_function import numbers_generator


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.checkout_btn = '.btn_action'
        self.first_name_input = '#first-name'
        self.last_name_input = '#last-name'
        self.postal_code_input = '#postal-code'
        self.btn_continue = '.btn_primary'
        self.btn_cancel = '//*[@id="checkout_info_container"]/div/form/div[2]/a'
        self.cancel_cart = (By.CSS_SELECTOR, '.subheader')

    def person_data(self):
        self.driver.find_element_by_css_selector(self.checkout_btn).click()
        self.driver.find_element_by_css_selector(self.first_name_input).send_keys(generate_nick(6, 2))
        self.driver.find_element_by_css_selector(self.last_name_input).send_keys(generate_nick(8, 4))
        self.driver.find_element_by_css_selector(self.postal_code_input).send_keys(numbers_generator(6))
        self.driver.find_element_by_css_selector(self.btn_continue).click()

    def cancel_person_data(self):
        self.driver.find_element_by_css_selector(self.checkout_btn).click()
        self.driver.find_element_by_xpath(self.btn_cancel).click()

    def cancel_cart_finder(self):
        cart_header = self.driver.find_element(*self.cancel_cart)
        return cart_header.text
