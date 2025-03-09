import pytest
from selenium import webdriver

from data.card import Card
from data.contact_us import ContactUs
from data.review import ReviewData
from data.user import User
from pages.cart_page import CartPage
from pages.contact_us_page import ContactUsPage
from pages.subscription_page import SubscriptionPage
from pages.login_page import LoginPage
from pages.payment_page import PaymentPage
from pages.products_page import ProductsPage
from pages.registration_page import RegistrationPage


def pytest_collection_modifyitems(config, items):
    order = ["test_registration.py", "test_login.py", "test_contact_us.py", "test_subscription.py",
             "test_product_review.py", "test_buy_product.py", 'test_delete_acc.py']
    items.sort(key=lambda x: order.index(x.nodeid.split("::")[0]))

@pytest.fixture(scope='function', autouse=True)
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()

    yield driver

    driver.quit()

@pytest.fixture
def user():
    return User()

@pytest.fixture
def contact_us():
    return ContactUs()

@pytest.fixture
def review():
    return ReviewData()

@pytest.fixture
def card():
    return Card()

@pytest.fixture
def reg_page(driver):
    return RegistrationPage(driver)

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture
def contact_us_page(driver):
    return ContactUsPage(driver)

@pytest.fixture
def sub_page(driver):
    return SubscriptionPage(driver)

@pytest.fixture
def products_page(driver):
    return ProductsPage(driver)

@pytest.fixture
def cart_page(driver):
    return CartPage(driver)

@pytest.fixture
def payment_page(driver):
    return PaymentPage(driver)