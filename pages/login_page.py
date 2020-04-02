class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.login_input = 'input#user-name'
        self.password_input = 'input#password'
        self.login_btn = '[value="LOGIN"]'
        self.burger_btn = '[class="bm-burger-button"] > button'
        self.logout_btn = '#logout_sidebar_link'
        self.error_alert = '#login_button_container h3'

    def login(self, user, password):
        self.driver.find_element_by_css_selector(self.login_input).send_keys(user)
        self.driver.find_element_by_css_selector(self.password_input).send_keys(password)
        self.driver.find_element_by_css_selector(self.login_btn).click()
