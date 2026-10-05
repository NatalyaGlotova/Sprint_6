from selenium.webdriver.common.by import By


class HeaderFooterLocators:
    # кнопка принять куки
    COOKIE_BUTTON = (By.XPATH, '//button[@id="rcc-confirm-button" and '
                               'contains(@class, "App_CookieButton")]')
    # логотип Яндекс
    YANDEX_LOGO = (
        By.XPATH,
        "//*[contains(@class, 'Header_LogoYandex')]")
    # логотип Самокат
    SAMOKAT_LOGO = (
        By.XPATH,
        "//*[contains(@class, 'Header_LogoScooter')]")
    # логотип Дзена
    DZEN_LOGO = (By.XPATH, "//*[contains(@class, 'dzen-layout--desktop-base-header__logoLink-2h')]")

