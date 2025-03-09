from selenium.webdriver.common.by import By


class CartPageLocators:
    VERIFY_ADDED_PRODUCT = (By.CSS_SELECTOR, '[href="/product_details/3"]')
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, '.check_out')
    VERIFY_CHECKOUT_UNLOGGED = (By.CSS_SELECTOR, '.modal-body :first-child.text-center')
    CLOSE_CHECKOUT_BUTTON = (By.CSS_SELECTOR, '.btn-success')
    DELETE_PRODUCT = (By.CSS_SELECTOR, '.cart_quantity_delete')
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, '.text-center b')
    VERIFY_CHECKOUT_LOGGED = (By.CSS_SELECTOR, '.heading')
    PLACE_ORDER_BUTTON = (By.CSS_SELECTOR, '[href="/payment"]')

