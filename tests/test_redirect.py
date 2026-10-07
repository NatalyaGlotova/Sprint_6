import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import URLs
from pages.header_footer_page import HeaderFooterPage


@allure.suite('Тестирование переходов с логотипа')
class TestRedirects:

    @allure.title('Проверка перехода по логотипу Самоката')
    @allure.description('Переход на главную страницу Самоката при клике на слово Самокат в логотипе')
    def test_redirect_scooter_logo(self, driver):
        header_footer_page = HeaderFooterPage(driver)
        current_url = header_footer_page.click_scooter_logo()
        
        assert URLs.main_page in current_url, (
            f"Переход на главную страницу Самоката не выполнен. "
            f"Ожидался {URLs.main_page}, но текущий URL: {current_url}"
        )

    @allure.title('Проверка перехода по логотипу Яндекса')
    @allure.description('Переход на главную страницу Дзена при клике на слово Яндекс в логотипе')
    def test_redirect_yandex_logo(self, driver):
        header_footer_page = HeaderFooterPage(driver)

        # Кликаем по логотипу, переключаем вкладку, ждем пока прогрузится
        header_footer_page.go_to_yandex_from_logo()

        # Проверяем переход на Дзен: корректность URL и отображение логотипа
        current_url = header_footer_page.wait_for_url_contains(URLs.dzen_page)
        is_dzen_logo_displayed = header_footer_page.is_dzen_logo_displayed()

        assert URLs.dzen_page in current_url and is_dzen_logo_displayed, (
            f"Ошибка перехода на Дзен. "
            f"Текущий URL: {current_url} (ожидался подтекст {URLs.dzen_page}). "
            f"Логотип отображается: {is_dzen_logo_displayed}."
        )
        