from selenium.webdriver.common.by import By


class InventoryPage:

    def __init__(self, driver):

        self.driver = driver
        self.cart_status = (By.CSS_SELECTOR, '#shopping_cart_container > a > svg')
        self.continue_shopping_btn = (By.CSS_SELECTOR, 'div#cart_contents_container a.btn_secondary')
        self.products = (By.XPATH, '/html/body/div/div[2]/div[2]/div/div[1]/div[3]/div')

    @classmethod
    def element_xpath(cls, element):
        xpath = f"/html/body/div/div[2]/div[2]/div/div[2]/div/div[{element}]/div[3]/button"
        return By.XPATH, xpath

    def click_on_cart_icon(self):
        cart = self.driver.find_element(*self.cart_status)
        return cart.click()

    def click_on_element(self, element):
        button = self.driver.find_element(*self.element_xpath(element))
        return button.click()

    def click_on_continue_shopping(self):
        continue_shopping = self.driver.find_element(*self.continue_shopping_btn)
        return continue_shopping.click()

    def get_products_header(self):
        products_text = self.driver.find_element(*self.products)
        return products_text.text

    def button_text(self, element):
        button = self.driver.find_element(*self.element_xpath(element))
        return button.text




















