from selenium.webdriver.support.select import Select
from config.settings import Settings
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.registration_page_locators import RegistrationPageLocators
import allure


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = RegistrationPageLocators
        self.wait = WebDriverWait(self.driver, 5)

    @allure.step('Открыть страницу регистрации')
    def open(self):
        self.driver.get(Settings.SIGNUP_URL)
        return self

    @allure.step('Заполнить поля имя и имейл')
    def fill_signup_form(self, name, email):
        with allure.step('Ввод имени пользователя'):
            self.driver.find_element(*self.locators.SIGNUP_NAME_FIELD).send_keys(name)
        with allure.step('Ввод имейла'):
            self.driver.find_element(*self.locators.SIGNUP_EMAIL_FIELD).send_keys(email)
        with allure.step('Нажатие нопки регистрации'):
            self.driver.find_element(*self.locators.SIGNUP_BUTTON).click()

    @allure.step('Проверить успешный переход на форму регистрации')
    def verify_success_signup(self):
        with allure.step('Проверка информации об аккаунте'):
            message = self.driver.find_element(*self.locators.ACC_INFO_MESSAGE).text
            assert message == 'ENTER ACCOUNT INFORMATION'
        return self

    @allure.step('Заполнить форму регистрации')
    def fill_registration_form(self, password, first_name, last_name, address, country, state, city, zipcode, mobnum):
        with allure.step('Ввод пароля'):
            self.driver.find_element(*self.locators.PASSWORD_FIELD).send_keys(password)
        with allure.step('Ввод имени'):
            self.driver.find_element(*self.locators.FIRST_NAME_FIELD).send_keys(first_name)
        with allure.step('Ввод фамилии'):
            self.driver.find_element(*self.locators.LAST_NAME_FIELD).send_keys(last_name)
        with allure.step('Ввод адреса'):
            self.driver.find_element(*self.locators.ADDRESS_FIELD).send_keys(address)
        with allure.step('Выбор страны'):
            country_dropdown = Select(self.driver.find_element(*self.locators.COUNTRY_DROPDOWN))
            country_dropdown.select_by_value(country)
        with allure.step('Ввод штата'):
            self.driver.find_element(*self.locators.STATE_FIELD).send_keys(state)
        with allure.step('Ввод города'):
            self.driver.find_element(*self.locators.CITY_FIELD).send_keys(city)
        with allure.step('Ввод индекса'):
            self.driver.find_element(*self.locators.ZIPCODE_FIELD).send_keys(zipcode)
        with allure.step('Ввод телефона'):
            self.driver.find_element(*self.locators.MOBILE_NUMBER_FIELD).send_keys(mobnum)
        with allure.step('Нажатие кнопки Создать Аккаунт'):
            create_account_button = self.driver.find_element(*self.locators.CREATE_ACCOUNT_BUTTON)
            self.driver.execute_script("arguments[0].scrollIntoView();", create_account_button)
            create_account_button.click()
        return self

    @allure.step('Проверить сообщение об усппешной регистрации')
    def verify_success_message(self):
        success_message = self.driver.find_element(*self.locators.SUCCESS_MESSAGE).text
        assert success_message == 'ACCOUNT CREATED!'
        return self

    @allure.step('Проверить сообщение об ошибке')
    def verify_unsuccess_message(self):
        self.wait.until(EC.visibility_of_element_located(self.locators.UNSUCCESS_MESSAGE))
        unsuccess_message = self.driver.find_element(*self.locators.UNSUCCESS_MESSAGE).text
        assert  unsuccess_message == 'Email Address already exist!'





