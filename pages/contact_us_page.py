from config.settings import Settings
from locators.contact_us_page_locators import ContactUsPageLocators
import allure


class ContactUsPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = ContactUsPageLocators

    @allure.step('Открыть страницу contact us')
    def open(self):
        self.driver.get(Settings.CONTACT_US)
        return self

    @allure.step('Проверить заголовок формы contact us')
    def verify_title(self):
        title = self.driver.find_element(*self.locators.CONTACT_US_TITLE).text
        assert title == 'GET IN TOUCH'
        return self

    @allure.step('Заполнить форму contact us')
    def fill_contact_us_form(self, name, email, subject, message, file_path):
        with allure.step('Ввод имени'):
            self.driver.find_element(*self.locators.NAME_FIELD).send_keys(name)
        with allure.step('Ввод имейла'):
            self.driver.find_element(*self.locators.EMAIL_FIELD).send_keys(email)
        with allure.step('Ввод темы'):
            self.driver.find_element(*self.locators.SUBJECT_FIELD).send_keys(subject)
        with allure.step('Ввод сообщения'):
            self.driver.find_element(*self.locators.MESSAGE_FIELD).send_keys(message)
        with allure.step('Выбор файла для загрузки'):
            self.driver.find_element(*self.locators.UPLOAD_FILE_BUTTON).send_keys(file_path)
        with (allure.step('Нажатие кнопки подтверждения')):
            submit_button = self.driver.find_element(*self.locators.SUBMIT_BUTTON)
            self.driver.execute_script("arguments[0].scrollIntoView();", submit_button)
            submit_button.click()
        return self

    @allure.step('Подтвердить алерт')
    def accept_alert(self):
        self.driver.switch_to.alert.accept()
        return self

    @allure.step('Проверить успешное сообщение отправки формы')
    def verify_success_message(self):
        success_message = self.driver.find_element(*self.locators.SUCCESS_MESSAGE).text
        assert success_message == 'Success! Your details have been submitted successfully.'
        return self
