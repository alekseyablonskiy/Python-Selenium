import allure


@allure.title('Успешная отправка обзора')
@allure.description('Тест проверяет успешную отправку обзора')
def test_success_review(products_page, review):
    with allure.step('Открыть страницу продуктов'):
        products_page.open()
    with allure.step('Найти и просмотреть продукт'):
        products_page.find_and_view_product()
    with allure.step('Заполнить форму обзора'):
        products_page.fill_review_form(name=review.name, email=review.email, review=review.review)
    with allure.step('Проверить сообщение об успешной отправке обзора'):
        products_page.verify_success_review_alert()
