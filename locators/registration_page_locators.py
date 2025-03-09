from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    SIGNUP_NAME_FIELD = (By.CSS_SELECTOR, '[data-qa="signup-name"]')
    SIGNUP_EMAIL_FIELD = (By.CSS_SELECTOR, '[data-qa="signup-email"]')
    SIGNUP_BUTTON = (By.CSS_SELECTOR, '[data-qa="signup-button"]')
    ACC_INFO_MESSAGE = (By.CSS_SELECTOR, '.title:first-child')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#password')
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, '#first_name')
    LAST_NAME_FIELD = (By.CSS_SELECTOR, '#last_name')
    ADDRESS_FIELD = (By.CSS_SELECTOR, '#address1')
    COUNTRY_DROPDOWN = (By.CSS_SELECTOR, '#country')
    STATE_FIELD = (By.CSS_SELECTOR, '#state')
    CITY_FIELD = (By.CSS_SELECTOR, '#city')
    ZIPCODE_FIELD = (By.CSS_SELECTOR, '#zipcode')
    MOBILE_NUMBER_FIELD = (By.CSS_SELECTOR, '#mobile_number')
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, '[data-qa="create-account"]')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '[data-qa="account-created"]')
    UNSUCCESS_MESSAGE = (By.CSS_SELECTOR, '[style="color: red;"]')