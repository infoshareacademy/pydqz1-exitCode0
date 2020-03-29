import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from generator_function import generate_nick
from generator_function import numbers_generator
import allure


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.saucedemo.com/')
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.login_page = LoginPage(driver)
    before_failed = request.session.testsfailed
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name='Test failed', attachment_type=AttachmentType.PNG)
    driver.quit()


@pytest.fixture()
def setup1(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.saucedemo.com/inventory.html')
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.inventory_page = InventoryPage(driver)
    request.cls.cart_page = CartPage(driver)
    before_failed = request.session.testsfailed
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name='Test failed', attachment_type=AttachmentType.PNG)
    driver.quit()


@pytest.fixture()
def setup3(request):
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.saucedemo.com/inventory.html')
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.inventory_page = InventoryPage(driver)
    driver.find_element_by_css_selector(
        'div.inventory_item:nth-child(1) > div:nth-child(3) > button:nth-child(2)').click()
    driver.find_element_by_css_selector(
        'div.inventory_item:nth-child(3) > div:nth-child(3) > button:nth-child(2)').click()
    driver.find_element_by_css_selector('.svg-inline--fa > path:nth-child(1)').click()
    yield
    driver.quit()


@pytest.fixture()
def setup4(request):
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.saucedemo.com/inventory.html')
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.inventory_page = InventoryPage(driver)
    driver.find_element_by_css_selector(
        'div.inventory_item:nth-child(1) > div:nth-child(3) > button:nth-child(2)').click()
    driver.find_element_by_css_selector(
        'div.inventory_item:nth-child(3) > div:nth-child(3) > button:nth-child(2)').click()
    driver.find_element_by_css_selector('.svg-inline--fa > path:nth-child(1)').click()
    driver.find_element_by_css_selector('.btn_action').click()
    driver.find_element_by_css_selector('#first-name').send_keys(generate_nick(6, 2))
    driver.find_element_by_css_selector('#last-name').send_keys(generate_nick(8, 4))
    driver.find_element_by_css_selector('#postal-code').send_keys(numbers_generator(6))
    driver.find_element_by_css_selector('.btn_primary').click()
    yield
    driver.quit()


