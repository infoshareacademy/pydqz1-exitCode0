import pytest
import allure


@pytest.mark.usefixtures('setup3')
class TestCheckoutFeature:

# Test that checks fill in fields and redirection to overview page from your information page
    @allure.step('Test checkout feature continue')
    def test_checkout_feature_continue(self):
        self.checkout_page.person_data()
        assert self.cart_page.get_cart_header() == "Checkout: Overview"

# Test that checks resignation from ordering and redirection to your cart page from your information page
    @allure.step('Test checkout feature cancel')
    def test_checkout_feature_cancel(self):
        self.checkout_page.cancel_person_data()
        assert self.checkout_page.cancel_cart_finder() == "Your Cart"


@pytest.mark.usefixtures('setup4')
class TestOverwievFeature:

# Test that checks correct completion of the order and redirection to finish page from overview page
    @allure.step('Test checkout overwiev finish')
    def test_checkout_overwiev_finish(self):
        self.checkout_overview_page.finish()
        assert self.checkout_overview_page.finish_header_finder() == "Finish"

# Test that checks cancellation of an order placed and redirection to products page from overview page
    @allure.step('Test checkout overwiev cancel')
    def test_checkout_overview_cancel(self):
        self.checkout_overview_page.cancel()
        assert self.checkout_overview_page.product_header_finder() == "Products"
