from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_FIELD = (By.CSS_SELECTOR, '[data-qa="login-email"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '[data-qa="login-password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-qa="login-button"]')
    LOGGED_IN_USER = (By.CSS_SELECTOR, "li:nth-child(10) > a")
    UNSUCCESS_MESSAGE = (By.CSS_SELECTOR, '[style="color: red;"]')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '[href="/logout"]')
    LOGIN_FORM_TITLE = (By.CSS_SELECTOR, "h2")
    DELETE_ACC_BUTTON = (By.CSS_SELECTOR, '[href="/delete_account"]')
    VERIFY_ACC_DELETED = (By.CSS_SELECTOR, '[data-qa="account-deleted"]')