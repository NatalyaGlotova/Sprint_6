import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    # Базовые методы, которые будут применяться на каждой странице

    def __init__(self, driver):
        self.driver = driver

    @property
    def current_url(self):
        # Возвращает текущий URL страницы.
        return self.driver.current_url
    

    @allure.step("Ждём, пока элемент станет видимым: {locator}")
    def wait_for_element_visible(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент с локатором {locator} не стал видимым в течение {timeout} секунд."
        )

    @allure.step("Ждём, пока элемент станет кликабельным: {locator}")
    def wait_for_element_clickable(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент с локатором {locator} не стал кликабельным в течение {timeout} секунд."
        )

    @allure.step("Кликаем по элементу через ActionChains: {locator}")
    def click_with_actions(self, locator):
        element = self.driver.find_element(*locator)
        ActionChains(self.driver).move_to_element(element).click().perform()

    @allure.step("Ждём и ищем список элементов: {locator}")
    def find_elements_with_wait(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator),
            message=f"Элементы с локатором {locator} не стали видимыми в течение {timeout} секунд."
        )

    @allure.step("Скролл до элемента с локатором {locator}")
    def scroll_to_element(self, locator):
        element = self.wait_for_element_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Скроллим в самый низ")
    def scroll_page_down(self):
        self.driver.execute_script("window.scrollTo("
                                   "0, document.body.scrollHeight);")

       

    @allure.step("Клик по элементу с локатором: {locator}")
    def click_to_element(self, locator):
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(locator))
        element.click()


    @allure.step("Получение текста из элемента с локатором: {locator}")
    def get_text_from_element(self, locator, timeout=15):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return element.text

    @allure.step("Заполняем поле {locator} значением: {value}")
    def fill(self, locator, value):
        # Используем существующий метод wait_for_element_visible для консистентности тайм-аутов
        element = self.wait_for_element_visible(locator)
        element.send_keys(value)


    @allure.step("Переключение на вкладку с индексом {tab_index}")
    def switch_to_tab(self, tab_index):
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[tab_index])

    @allure.step("Ожидаем появление подстроки в URL и возвращаем финальный URL страницы")
    def wait_for_url_contains(self, url_part, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(url_part))
        return self.driver.current_url        

    @allure.step("Ищем элемент по тегу {tag_name} и кликаем")
    def click_by_tag_name(self, tag_name):
        element = self.driver.find_element(By.TAG_NAME, tag_name)
        element.click()

    # Метод, который форматирует локаторы
    @staticmethod
    def format_locators(locator_template, num):
        method, locator = locator_template
        locator = locator.format(num)
        return method, locator

    
