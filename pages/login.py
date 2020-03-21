class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.login_input_css = 'input#user-name'
        self.password_input_css = 'input#password'
        self.login_btn_css = '[value="LOGIN"]'
        self.burger_btn_css = '[class="bm-burger-button"]'

    # @allure.step('Login as {1} user')
    def login(self, user, password):
        self.driver.find_element_by_css_selector(self.login_input_css).send_keys(user)
        self.driver.find_element_by_css_selector(self.password_input_css).send_keys(password)
        self.driver.find_element_by_css_selector(self.login_btn_css).click()

    # @allure.step('Show burger menu after valid log in')
    def show_burger_btn(self):
        return self.driver.find_element_by_css_selector(self.burger_btn_css).is_displayed()