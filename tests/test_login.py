import allure
import pytest
from data.user import User

@allure.title('Успешный вход и выход из системы')
@allure.description('Тест проверяет усешный вход в систему и выход из нее')
def test_success_login_and_logout(login_page, user):
    with allure.step('Открыть страницу входа'):
        login_page.open()
    with allure.step('Заполнить форму входа'):
        login_page.fill_login_form(email=user.email, password=user.password)
    with allure.step('Проверить успешный вход'):
        login_page.verify_success_login(name=user.name)
    with allure.step('Выйти из системы'):
        login_page.logout_from_account()
    with allure.step('Проверить заголовок формы входа'):
        login_page.verify_login_form_title()

@allure.title('Проверка входа с некорректными данными')
@allure.description('Тест проверяет вход с некорректными email и/или паролем')
@pytest.mark.parametrize('email, password',
    [('incorrect@mail.com', User.password),
    (User.email, 'incorrect_password'),
    ('incorrect@mail.ru', 'incorrect_password')])
def test_incorrect_login(login_page, email, password):
    with allure.step('Открыть страницу входа'):
        login_page.open()
    with allure.step('Заполнить форму входа с некорректными данными'):
        login_page.fill_login_form(email=email, password=password)
    with allure.step('Проверить сообщение об ошибке'):
        login_page.verify_incorrect_data()