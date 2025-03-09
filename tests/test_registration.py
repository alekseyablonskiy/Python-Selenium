import allure


@allure.title('Успешная регистрация')
@allure.description('Тест проверяет успешную регистрацию пользователя')
def test_registration_successful(reg_page, user):
    with allure.step('Открыть страницу регистрации'):
        reg_page.open()
    with allure.step('Заполнить поля имя и имейл'):
        reg_page.fill_signup_form(name=user.name, email=user.email)
    with allure.step('Проверить успешный переход на форму регистрации'):
        reg_page.verify_success_signup()
    with allure.step('Заполнить форму регистрации'):
        reg_page.fill_registration_form(
                password=user.password,
                first_name=user.first_name,
                last_name=user.last_name,
                address=user.address,
                country=user.country,
                state=user.state,
                city=user.city,
                zipcode=user.zipcode,
                mobnum=user.mobile_number
            )
    with allure.step('Проверить сообщение об успешной регистрации'):
        reg_page.verify_success_message()

@allure.title('Неуспешная регистрация')
@allure.description('Тест проверяет неуспешную регистрацию пользователя')
def test_registration_unsuccessful(reg_page, user):
    with allure.step('Открыть страницу регистрации'):
        reg_page.open()
    with allure.step('Заполнить поля имя и имейл'):
        reg_page.fill_signup_form(name=user.name, email=user.email)
    with allure.step('Проверить сообщение об ошибке'):
        reg_page.verify_unsuccess_message()