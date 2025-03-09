import os


class Settings:
    BASE_URL = 'https://www.automationexercise.com'
    SIGNUP_URL = f'{BASE_URL}/signup'
    LOGIN_URL = f'{BASE_URL}/login'
    CONTACT_US = f'{BASE_URL}/contact_us'
    PRODUCTS_URL = f'{BASE_URL}/products'
    CART_URL = f'{BASE_URL}/view_cart'

    FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/files/test_file.txt"))
