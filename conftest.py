import allure
import pytest
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from data import URLs
from datetime import date, timedelta
from selenium.webdriver.support import expected_conditions as EC
from locators.header_footer_locators import HeaderFooterLocators


# Фикстура драйвера для Mozilla Firefox
@pytest.fixture()
def driver():
    firefox_options = webdriver.FirefoxOptions()  # Создали объект для опций
    driver = webdriver.Firefox(options=firefox_options)  # Инициализируем драйвер

    with allure.step("Подготовка драйвера и переход на главную страницу"):
        driver.maximize_window()  # Разворачиваем окно Firefox на максимальный размер
        driver.get(URLs.main_page)  # Переходим на основной url

    with allure.step("Ожидание полной загрузки страницы (document.readyState == 'complete')"):
            WebDriverWait(driver, 20).until(
                lambda d: d.execute_script("return document.readyState") == "complete")

                # Автоматический прием куки сразу после загрузки страницы
    with allure.step("Принимаем куки"):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(HeaderFooterLocators.COOKIE_BUTTON)
        ).click()

    yield driver  

    with allure.step("Закрытие браузера"):
        driver.quit()  


@pytest.fixture
# Генерируем словарь для заполнения формы заказа
def create_order_data():
    name = ["Виктория", "Ксения", "Мария", "Наталья", "Олеся"]
    surname = ["Глотова", "Богачёва", "Кожевникова", "Иванова", "Кузнецова"]
    address = ["Битцевский парк, 18", "Маркса, 8",
                                  "Кирова, 14", "Вернадского, 27", "Курчатова, 87"]
    metro_stations = ["Охотный ряд", "Александровский сад", "Речной вокзал",
                      "Щелковская", "Краснопресненская", "Проспект Мира",
                      "Парк культуры", "Воробьёвы горы","Юго-Западная", 
                      "Театральная", "Павелецкая", "Студенческая",
                      "Ботанический сад", "Калужская", "Улица 1905 года"]
    colors = ["black", "grey"]
    rental_durations = ["сутки", "двое суток", "трое суток", "четверо суток",
                        "пятеро суток", "шестеро суток", "семеро суток"]
    comment = ["Домофон 456", "Не звоните в звонок", "Домофон не работает", "Позвоните за час до доставки", "После 18 часов"]

    return  {
        'name': random.choice(name),
        'surname': random.choice(surname),
        'address': random.choice(address),
        'metro': random.choice(metro_stations),
        'phone': random.randint(10000000000, 99999999999),
        'date': (date.today() + timedelta(
            days=random.randint(1, 7))).strftime('%d.%m.%Y'),
        'duration': random.choice(rental_durations),
        'color': random.choice(colors),
        'comment': random.choice(comment)
        }        
