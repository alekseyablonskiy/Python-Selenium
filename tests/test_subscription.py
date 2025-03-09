import allure


@allure.title('Успешная подписка')
@allure.description('Тест проверяет успешную подписку на новости')
def test_success_subscription(sub_page, user):
    with allure.step('Открыть главную страницу'):
        sub_page.open()
    with allure.step('Заполнить поле Подписаться'):
        sub_page.fill_subscription_field(email=user.email)
    with allure.step('Проверить сообщение об успешной подписке'):
        sub_page.verify_success_subscription()
