from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.continue_btn = 'div#cart_contents_container a.btn_secondary'

    def continue_shopping(self):
        button = self.driver.find_element_by_css_selector('self.continue_btn')
        return button.click()
