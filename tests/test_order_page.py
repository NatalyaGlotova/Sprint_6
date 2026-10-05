import pytest
import allure

from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators

@allure.suite('Тестирование страницы заказа')
class TestOrderPage:
    @allure.title('Тест создания заказа')
    @allure.description('Позитивный сценарий создания заказа с уникальными данными через разные точки входа')
    @pytest.mark.parametrize(
        'button_location, method_name',
        [
            ('Верхняя кнопка', 'create_order_from_header'),
            ('Нижняя кнопка', 'create_order_from_bottom')
        ]
    )
    def test_create_order(self, driver, button_location, method_name, create_order_data):
        # Динамически устанавливаем заголовок для Allure с учетом параметров
        allure.dynamic.title(f'Тест создания заказа: {button_location}')
         
        order_page = OrderPage(driver)
        # Генерируем уникальный набор данных для текущего теста
        order_info = create_order_data
        
        # Динамический вызов нужного метода страницы
        order_method = getattr(order_page, method_name)
        order_method(order_info)
        
        assert order_page.wait_for_element_visible(OrderPageLocators.STATUS_WINDOW), \
            f"Окно с информацией о заказе не появилось при оформлении через: {button_location}"
