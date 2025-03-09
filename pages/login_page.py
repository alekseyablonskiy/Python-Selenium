from config.settings import Settings
from locators.login_page_locators import LoginPageLocators
import allure

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = LoginPageLocators

    @allure.step('Открыть страницу входа')
    def open(self):
        self.driver.get(Settings.LOGIN_URL)
        return self

    @allure.step('Заполнить форму входа')
    def fill_login_form(self, email, password):
        with allure.step('Ввод имейла'):
            self.driver.find_element(*self.locators.EMAIL_FIELD).send_keys(email)
        with allure.step('Ввод пароля'):
            self.driver.find_element(*self.locators.PASSWORD_FIELD).send_keys(password)
        with allure.step('Нажатие кнопки подтверждения'):
            self.driver.find_element(*self.locators.LOGIN_BUTTON).click()
        return self

    @allure.step('Проверить успешный вход')
    def verify_success_login(self, name):
        logged_in_user  = self.driver.find_element(*self.locators.LOGGED_IN_USER).text
        assert name in logged_in_user
        return self

    @allure.step('Выйти из системы')
    def logout_from_account(self):
        self.driver.find_element(*self.locators.LOGOUT_BUTTON).click()
        return self

    @allure.step('Проверить заголовок формы входа')
    def verify_login_form_title(self):
        login_form_title = self.driver.find_element(*self.locators.LOGIN_FORM_TITLE).text
        assert login_form_title == 'Login to your account'
        return self

    @allure.step('Проверить сообщение об ошибке')
    def verify_incorrect_data(self):
        try:
            incorrect_login = self.driver.find_element(*self.locators.UNSUCCESS_MESSAGE).text
            assert  incorrect_login == 'Your email or password is incorrect!'
        except Exception as e:
            raise AssertionError(f'Ошибка в verify_incorrect_data: {e}')
        return self

    @allure.step('Удалить аккаунт')
    def delete_account(self):
        self.driver.find_element(*self.locators.DELETE_ACC_BUTTON).click()
        return self

    @allure.step('Проверить успешное удаление аккаунта')
    def verify_success_delete_account(self):
        success_deleted = self.driver.find_element(*self.locators.VERIFY_ACC_DELETED).text
        assert success_deleted == 'ACCOUNT DELETED!'
        return self