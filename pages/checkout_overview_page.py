from selenium.webdriver.common.by import By


class CheckoutOverviewPage:

    def __init__(self, driver):
        self.driver = driver
        self.cancel_btn = '.cart_cancel_link'
        self.finish_btn = ".btn_action"
        self.finish_cart = (By.CSS_SELECTOR, '#contents_wrapper > div.subheader')
        self.product_cart = (By.CSS_SELECTOR, '.product_label')

    def cancel(self):
        self.driver.find_element_by_css_selector(self.cancel_btn).click()

    def finish(self):
        self.driver.find_element_by_css_selector(self.finish_btn).click()

    def finish_header_finder(self):
        cart_header = self.driver.find_element(*self.finish_cart)
        return cart_header.text

    def product_header_finder(self):
        cart_header = self.driver.find_element(*self.product_cart)
        return cart_header.text
