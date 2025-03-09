from selenium.webdriver.common.by import By


class PaymentPageLocators:
    VERIFY_PAYMENT_PAGE = (By.CSS_SELECTOR, '.heading')
    NAME_ON_CARD = (By.CSS_SELECTOR, '[data-qa="name-on-card"]')
    CARD_NUMBER = (By.CSS_SELECTOR, '[data-qa="card-number"]')
    CVC = (By.CSS_SELECTOR, '[data-qa="cvc"]')
    EXPIRATION_MONTH = (By.CSS_SELECTOR, '[data-qa="expiry-month"]')
    EXPIRATION_YEAR = (By.CSS_SELECTOR, '[data-qa="expiry-year"]')
    PAY_BUTTON = (By.CSS_SELECTOR, '[data-qa="pay-button"]')
    SUCCESS_ORDER_MESSAGE = (By.CSS_SELECTOR, '[data-qa="order-placed"]')
