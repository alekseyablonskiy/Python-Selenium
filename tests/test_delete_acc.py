import allure


@allure.title('Успешныое удаление аккаунта')
@allure.description('Тест проверяет усешное удаление аккаунта')
def test_success_delete_account(login_page, user):
    with allure.step('Открыть страницу входа'):
        login_page.open()
    with allure.step('Заполнить форму входа'):
        login_page.fill_login_form(email=user.email, password=user.password)
    with allure.step('Проверить успешный вход'):
        login_page.verify_success_login(name=user.name)
    with allure.step('Удалить аккаунт'):
        login_page.delete_account()
    with allure.step('Проверить успешное удаление аккаунта'):
        login_page.verify_success_delete_account()