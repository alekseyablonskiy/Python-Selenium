from selenium.webdriver.common.by import By


class ContactUsPageLocators:
    CONTACT_US_TITLE = (By.CSS_SELECTOR, '.title:nth-child(2)')
    NAME_FIELD = (By.CSS_SELECTOR, '[data-qa="name"]')
    EMAIL_FIELD = (By.CSS_SELECTOR, '[data-qa="email"]')
    SUBJECT_FIELD = (By.CSS_SELECTOR, '[data-qa="subject"]')
    MESSAGE_FIELD = (By.CSS_SELECTOR, '#message')
    UPLOAD_FILE_BUTTON = (By.CSS_SELECTOR, '[name="upload_file"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '[data-qa="submit-button"]')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.status')