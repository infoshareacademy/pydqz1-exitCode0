
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.inventory import InventoryPage
from pages.login import LoginPage



# @pytest.fixture()
# def setup(request):
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#     driver.get('https://www.saucedemo.com/')
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     request.cls.driver = driver
#     request.cls.login_page = LoginPage(driver)
#     before_failed = request.session.testsfailed
#     yield
#     # if request.session.testsfailed != before_failed:
#     #     allure.attach(driver.get_screenshot_as_png(), name='Test failed', attachment_type=AttachmentType.PNG)
#     driver.quit()


@pytest.fixture()
def setup1(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.saucedemo.com/inventory.html')
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.inventory_page = InventoryPage(driver)
    yield
    driver.quit()





