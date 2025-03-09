import allure
from config.settings import Settings


@allure.title('Успешный вход и выход из системы')
@allure.description('Тест проверяет усешный вход в систему и выход из нее')
def test_contact_us_form(contact_us_page, contact_us):
    with allure.step('Открыть страницу contact us'):
        contact_us_page.open()
    with allure.step('Проверить заголовок формы contact us'):
        contact_us_page.verify_title()
    with allure.step('Заполнить форму contact us'):
        contact_us_page.fill_contact_us_form(name=contact_us.name, email=contact_us.email,
                                        subject=contact_us.subject, message=contact_us.message,
                                        file_path=Settings.FILE_PATH)
    with allure.step('Подтвердить алерт'):
        contact_us_page.accept_alert()
    with allure.step('Проверить успешное сообщение отправки формы'):
        contact_us_page.verify_success_message()