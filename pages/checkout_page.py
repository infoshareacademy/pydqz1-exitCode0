from generator_function import generate_nick
from generator_function import numbers_generator


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.checkout_btn = '.btn_action'
        self.first_name_input = '#first-name'
        self.last_name_input = '#last-name'
        self.postal_code_input = '#postal-code'
        self.btn_ok = '.btn_primary'

    def person_date(self, first_name, last_name, postal_code):
        self.driver.find_element_by_css_selector(self.checkout_btn).click()
        self.driver.find_element_by_css_selector(self.first_name_input).send_keys(generate_nick(6, 2))
        self.driver.find_element_by_css_selector(self.last_name_input).send_keys(generate_nick(8, 4))
        self.driver.find_element_by_css_selector(self.postal_code_input).send_keys(numbers_generator(6))
        self.driver.find_element_by_css_selector(self.btn_ok).click()
