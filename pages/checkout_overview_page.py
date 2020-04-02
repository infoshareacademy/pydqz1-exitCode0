class CheckoutOverviewPage:

    def __init__(self, driver):
        self.driver = driver
        self.cancel_btn = '.cart_cancel_link'
        self.finish_btn = ".btn_action"

    def cancel(self):
        self.driver.find_element_by_css_selector(self.cancel_btn).click()

    def finish(self):
        self.driver.find_element_by_css_selector(self.finish_btn).click()
