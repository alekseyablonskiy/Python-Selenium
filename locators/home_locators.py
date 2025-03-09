from selenium.webdriver.common.by import By


class HomePageLocators:
    EMAIL_FIELD = (By.CSS_SELECTOR, '#susbscribe_email')
    SUBSCRIBE_BUTTON = (By.CSS_SELECTOR, '#subscribe')
    ALERT_SUCCESS = (By.CSS_SELECTOR, '.alert-success')