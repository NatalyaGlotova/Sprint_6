import allure

from locators.header_footer_locators import HeaderFooterLocators
from pages.base_page import BasePage


class HeaderFooterPage(BasePage):
    @allure.step("Клик по логотипу Самоката")
    def click_scooter_logo(self):
        self.click_to_element(HeaderFooterLocators.SAMOKAT_LOGO)
        return self.current_url

    @allure.step("Переход по логотипу Яндекса")
    def go_to_yandex_from_logo(self):
        self.click_to_element(HeaderFooterLocators.YANDEX_LOGO)
        self.switch_to_tab(1)

    @allure.step("Проверка наличия логотипа Дзена")
    def is_dzen_logo_displayed(self):
        return self.wait_for_element_visible(HeaderFooterLocators.DZEN_LOGO).is_displayed()
