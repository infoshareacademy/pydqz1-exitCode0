import pytest
import allure


@pytest.mark.usefixtures('setup3')
class TestCheckoutFeature:

    # @allure.step('Test checkout feature continue')
    def test_checkout_feature_continue(self):
        self.checkout_page.person_data()
        assert self.cart_page.get_cart_header() == "Checkout: Overview"

    # @allure.step('Test checkout feature cancel')
    def test_checkout_feature_cancel(self):
        self.checkout_page.cancel_person_data()
        assert self.cart_page.get_cart_header() == "Your Cart"


@pytest.mark.usefixtures('setup4')
class TestOverwievFeature:


    # @allure.step('Test checkout overwiev finish')
    def test_checkout_overwiev_finish(self):
        self.checkout_overview_page.finish()
        assert self.cart_page.get_cart_header() == "Finish"


    # @allure.step('Test checkout overwiev cancel')
    def test_checkout_overview_cancel(self):
        self.checkout_overview_page.cancel()
        assert self.cart_page.get_cart_header() == "Products"
