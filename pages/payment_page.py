import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.payment_page_locators import PaymentPageLocators


class PaymentPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = PaymentPageLocators
        self.wait = WebDriverWait(self.driver, 5)

    @allure.step('Проверить переход на страницу оплаты')
    def verify_payment(self):
        verify_payment = self.driver.find_element(*self.locators.VERIFY_PAYMENT_PAGE).text
        assert verify_payment == 'Payment'
        return self

    @allure.step('Заполнить данные карты')
    def fill_payment_form(self, name, card_num, cvc, month, year):
        with allure.step('Вводи имени владельца'):
            self.driver.find_element(*self.locators.NAME_ON_CARD).send_keys(name)
        with allure.step('Ввод номера карты'):
            self.driver.find_element(*self.locators.CARD_NUMBER).send_keys(card_num)
        with allure.step('Ввод трехзначного кода'):
            self.driver.find_element(*self.locators.CVC).send_keys(cvc)
        with allure.step('Ввод месяца истечения срока карты'):
            self.driver.find_element(*self.locators.EXPIRATION_MONTH).send_keys(month)
        with allure.step('Ввод года истечения срока карты'):
            self.driver.find_element(*self.locators.EXPIRATION_YEAR).send_keys(year)
        with allure.step('Нажатие кнопки Оплаты'):
            self.driver.find_element(*self.locators.PAY_BUTTON).click()
        return self

    @allure.step('Проверить сообщение об успешной оплате')
    def verify_success_payment(self):
        success_order = self.wait.until(EC.visibility_of_element_located(self.locators.SUCCESS_ORDER_MESSAGE))
        assert success_order.text == 'ORDER PLACED!'
        return self
