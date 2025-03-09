import allure


@allure.title('Покупка незалогиненым пользователем и отчистка корзины')
@allure.description('Тест проверяет покупку незалогиненым пользователем и отчистку корзины')
def test_unlogged_buy(cart_page):
    with allure.step('Открыть страницу с продуктами'):
        cart_page.open()
    with allure.step('Добавить продукт в карзину'):
        cart_page.add_product_to_cart()
    with allure.step('Убедиться что продукт добавлен'):
        cart_page.verify_added_product_check()
    with allure.step('Продолжить покупку'):
        cart_page.unlogged_checkout()
    with allure.step('Проверить сообщение о том, что нужно залогиниться'):
        cart_page.verify_unlogged_checkout_message()
    with allure.step('Очистить корзину'):
        cart_page.empty_cart()
    with allure.step('Убедиться что корзина пуста'):
        cart_page.verify_cart_is_empty()

@allure.title('Успешная покупка залогиненым пользователем')
@allure.description('Тест проверяет покупку залогиненым пользователем')
def test_logged_buy(login_page, cart_page, payment_page, user, card):
    with allure.step('Открыть страницу входа'):
        login_page.open()
    with allure.step('Заполнить форму входа'):
        login_page.fill_login_form(email=user.email, password=user.password)
    with allure.step('Проверить успешный вход'):
        login_page.verify_success_login(name=user.name)
    with allure.step('Открыть страницу с продуктами'):
        cart_page.open()
    with allure.step('Добавить продукт в корзину'):
        cart_page.add_product_to_cart()
    with allure.step('Убедиться что продукт добавлен'):
        cart_page.verify_added_product_check()
    with allure.step('Продолжить покупку залогиненым пользователем'):
        cart_page.logged_cart_check()
    with allure.step('Проверить переход на страницу оплаты'):
        payment_page.verify_payment()
    with allure.step('Заполнить данные карты'):
        payment_page.fill_payment_form(name=card.name, card_num=card.card_num,
                                       cvc=card.cvc, month=card.month, year=card.year)
    with allure.step('Проверить сообщение об успешной оплате'):
        payment_page.verify_success_payment()
