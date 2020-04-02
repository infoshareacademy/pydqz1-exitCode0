import pytest
import allure
import time


@pytest.mark.usefixtures('setup')
class TestLogin:

# Test that checks the login function using the valid data
    @pytest.mark.parametrize('user, password', [('standard_user', 'secret_sauce'),
                                                ('problem_user', 'secret_sauce'),
                                                ('performance_glitch_user', 'secret_sauce')])
    @allure.step('Test login with valid data')
    def test_login_valid_data(self, user, password):
        self.login_page.login(user, password)
        time.sleep(2)
        self.driver.find_element_by_css_selector(self.login_page.burger_btn).click()
        time.sleep(2)
        # Assertion that checks displaying the logout button after successful login
        assert self.driver.find_element_by_css_selector(self.login_page.logout_btn).is_displayed() is True

# Test that checks the login function using the invalid data
    @allure.step('Test login with invalid data')
    def test_login_invalid_data(self):
        self.login_page.login("user", "password")
        # Assertion that checks for an error message caused by the use of incorrect data
        assert self.driver.find_element_by_css_selector(self.login_page.error_alert).text == "Epic sadface: Username and password do not match any user in this service"

# Test that checks the login function with both input boxes empty
    @allure.step('Test login with input boxes empty')
    def test_login_empty(self):
        self.login_page.login("", "")
        # Assertion that checks for an error message caused by the login attempt with both input boxes empty
        assert self.driver.find_element_by_css_selector(self.login_page.error_alert).text == "Epic sadface: Username is required"

# Test that checks the login function with password input box empty
    @allure.step('Test login with password input empty')
    def test_login_empty_password(self):
        self.login_page.login("standard_user", "")
        # Assertion that checks for an error message caused by the login attempt with password input box empty
        assert self.driver.find_element_by_css_selector(self.login_page.error_alert).text == "Epic sadface: Password is required"

# Test that checks the login function using the locked out user data
    @allure.step('Test login with locked out user data')
    def test_login_locked_out_user(self):
        self.login_page.login("locked_out_user", "secret_sauce")
        # Assertion that checks for an error message caused by the use of locked out user data
        assert self.driver.find_element_by_css_selector(self.login_page.error_alert).text == "Epic sadface: Sorry, this user has been locked out."
