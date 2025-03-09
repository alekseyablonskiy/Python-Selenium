import allure

from config.settings import Settings
from locators.products_page_locators import ProductsPageLocators


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = ProductsPageLocators
    @allure.step('Открыть страницу продуктов')
    def open(self):
        self.driver.get(Settings.PRODUCTS_URL)
        return self

    @allure.step('Найти и просмотреть продукт')
    def find_and_view_product(self):
        with allure.step('Поиск продукта'):
            product_name = self.driver.find_element(*self.locators.PRODUCT_SEARCH)
            self.driver.execute_script("arguments[0].scrollIntoView();", product_name)
            assert product_name.text == 'Sleeveless Dress'
        with allure.step('Нажатие кнопки Просмотр'):
            self.driver.find_element(*self.locators.VIEW_PRODUCT_BUTTON).click()
        return self

    @allure.step('Заполнить форму обзора')
    def fill_review_form(self, name, email, review):
        with allure.step('Проверка информации об обзоре'):
            review_field = self.driver.find_element(*self.locators.WRITE_YOUR_REVIEW).text
            assert review_field == 'WRITE YOUR REVIEW'
        with allure.step('Ввод имени'):
            self.driver.find_element(*self.locators.NAME_FIELD).send_keys(name)
        with allure.step('Ввод имейла'):
            self.driver.find_element(*self.locators.EMAIL_FIELD).send_keys(email)
        with allure.step('Ввод обзора'):
            self.driver.find_element(*self.locators.REVIEW_FIELD).send_keys(review)
        with allure.step('Нажатие кнопки подтверждения'):
            submit_button = self.driver.find_element(*self.locators.SUBMIT_BUTTON)
            self.driver.execute_script("arguments[0].scrollIntoView();", submit_button)
            submit_button.click()
        return self

    @allure.step('Проверить сообщение об успешной отправке обзора')
    def verify_success_review_alert(self):
        success_alert = self.driver.find_element(*self.locators.SUCCESS_REVIEW_ALERT).text
        assert success_alert == 'Thank you for your review.'
        return self
