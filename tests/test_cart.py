import pytest
import allure


@pytest.mark.usefixtures('setup1')
class TestInventory:

# Test that checks display of the quantity of products in cart
    @allure.step('Test cart quantity')
    def test_cart_quantity(self):
        for n in range(1, 7):
            self.inventory_page.click_on_element(n)
        assert self.cart_page.get_cart_quantity() == '6'

# Test that checks display of the REMOVE button after adding product to the cart
    @allure.step('Test remove btn')
    def test_remove_btn(self):
        self.inventory_page.click_on_element(1)
        assert self.inventory_page.button_text(1) == "REMOVE"

# Test that checks removal of products from the cart
    @allure.step('Test remove from cart')
    def test_remove_from_cart(self):
        for n in range(1, 3):
            self.inventory_page.click_on_element(n)
        self.inventory_page.click_on_element(1)
        assert self.cart_page.get_cart_quantity() == '1'

# Test that checks redirection to inventory page from cart page
    @allure.step('Test continue shopping')
    def test_continue_shopping(self):
        self.inventory_page.click_on_element(1)
        assert self.cart_page.get_cart_quantity() == '1'

        self.inventory_page.click_on_cart_icon()
        assert self.cart_page.get_cart_header() == 'Your Cart'

        self.inventory_page.click_on_continue_shopping()
        assert self.inventory_page.get_products_header() == 'Products'

# Test that checks display of products in cart
    @allure.step('Test products name')
    def test_products_name_cart(self):
        for n in range(1, 7):
            self.inventory_page.click_on_element(n)
        self.inventory_page.click_on_cart_icon()
        assert self.cart_page.get_cart_element_name(3) == 'Sauce Labs Backpack'
