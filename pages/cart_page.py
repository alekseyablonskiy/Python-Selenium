import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import Settings
from locators.products_page_locators import ProductsPageLocators
from locators.cart_page_locators import CartPageLocators


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.locatorsP = ProductsPageLocators
        self.locatorsC = CartPageLocators
        self.wait = WebDriverWait(self.driver, 5)

    @allure.step('Открыть страницу с продуктами')
    def open(self):
        self.driver.get(Settings.PRODUCTS_URL)
        return self

    @allure.step('Добавить продукт в корзину')
    def add_product_to_cart(self):
        with allure.step('Поиск нужного продукта'):
            self.wait.until(EC.visibility_of_element_located(self.locatorsP.PRODUCT_SEARCH))
            product_name = self.driver.find_element(*self.locatorsP.PRODUCT_SEARCH)
            self.driver.execute_script("arguments[0].scrollIntoView();", product_name)
            assert product_name.text == 'Sleeveless Dress'
        with allure.step('Добавление продукта в корзину'):
            self.driver.find_element(*self.locatorsP.ADD_TO_CART_BUTTON).click()
            added_alert = self.wait.until(EC.visibility_of_element_located(self.locatorsP.SUCCESS_ADDED_ALERT))
            assert added_alert.text == 'Your product has been added to cart.'
        with allure.step('Просмотр корзины'):
            self.driver.find_element(*self.locatorsP.VIEW_CART_BUTTON).click()
        return self

    @allure.step('Убедиться что продукт добавлен')
    def verify_added_product_check(self):
        added_product = self.driver.find_element(*self.locatorsC.VERIFY_ADDED_PRODUCT).text
        assert added_product == 'Sleeveless Dress'
        return self

    @allure.step('Продолжить покупку')
    def unlogged_checkout(self):
        self.driver.find_element(*self.locatorsC.CHECKOUT_BUTTON).click()
        return self

    @allure.step('Проверить сообщение о том, что нужно залогиниться')
    def verify_unlogged_checkout_message(self):
        checkout_text = self.driver.find_element(*self.locatorsC.VERIFY_CHECKOUT_UNLOGGED).text
        assert checkout_text == 'Register / Login account to proceed on checkout.'
        self.driver.find_element(*self.locatorsC.CLOSE_CHECKOUT_BUTTON).click()
        return self

    @allure.step('Очистить корзину')
    def empty_cart(self):
        self.driver.find_element(*self.locatorsC.DELETE_PRODUCT).click()
        return self

    @allure.step('Убедиться что корзина пуста')
    def verify_cart_is_empty(self):
        empty_cart = self.wait.until(EC.visibility_of_element_located(self.locatorsC.EMPTY_CART_MESSAGE))
        assert empty_cart.text == 'Cart is empty!'
        return self

    @allure.step('Продолжить покупку залогиненым пользователем')
    def logged_cart_check(self):
        with allure.step('Продолжение покупки'):
            self.driver.find_element(*self.locatorsC.CHECKOUT_BUTTON).click()
        with allure.step('Поиск поля адреса'):
            checkout_text = self.driver.find_element(*self.locatorsC.VERIFY_CHECKOUT_LOGGED).text
            assert checkout_text == 'Address Details'
        with allure.step('Нажатие кнопки оформления заказа'):
            place_order = self.driver.find_element(*self.locatorsC.PLACE_ORDER_BUTTON)
            self.driver.execute_script("arguments[0].scrollIntoView();", place_order)
            place_order.click()
        return self
