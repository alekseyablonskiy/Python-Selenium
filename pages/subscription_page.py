from config.settings import Settings
from locators.home_locators import HomePageLocators
import allure


class SubscriptionPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = HomePageLocators

    @allure.step('Открыть главную страницу')
    def open(self):
        self.driver.get(Settings.BASE_URL)
        return self

    @allure.step('Заполнить поле Подписаться')
    def fill_subscription_field(self, email):
        with allure.step('Ввод имейла в поле Подписаться'):
            subscription_field = self.driver.find_element(*self.locators.EMAIL_FIELD)
            self.driver.execute_script("arguments[0].scrollIntoView();", subscription_field)
            subscription_field.send_keys(email)
        with allure.step('Нажатие кнопки Подписаться'):
            self.driver.find_element(*self.locators.SUBSCRIBE_BUTTON).click()
        return self

    @allure.step('Проверить сообщение об успешной подписке')
    def verify_success_subscription(self):
        success_message = self.driver.find_element(*self.locators.ALERT_SUCCESS).text
        assert success_message == 'You have been successfully subscribed!'
        return self

