from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.continue_btn = 'div#cart_contents_container a.btn_secondary'
        self.cart_navbar_status = (By.CSS_SELECTOR, 'div#shopping_cart_container span')
        self.your_cart = (By.CSS_SELECTOR, '#contents_wrapper > div.subheader')

    @classmethod
    def pick_cart_element(cls, element):
        xpath = f"/html/body/div/div[2]/div[3]/div/div[1]/div[{element}]/div[2]/a/div"
        return By.XPATH, xpath

    def continue_shopping(self):
        button = self.driver.find_element_by_css_selector('self.continue_btn')
        button.click()

    def get_cart_quantity(self):
        quantity = self.driver.find_element(*self.cart_navbar_status)
        return quantity.text

    def get_cart_header(self):
        cart_header = self.driver.find_element(*self.your_cart)
        return cart_header.text

    def get_cart_element_name(self, element):
        element = self.driver.find_element(*self.pick_cart_element(element))
        return element.text
