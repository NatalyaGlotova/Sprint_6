from selenium.webdriver.common.by import By



class OrderPageLocators():
    # ФОРМА Для кого самокат
    # Поле Имя
    NAME_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Имя')]")
    # Поле Фамилия
    SURNAME_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Фамилия')]")
    # Поле Адрес
    ADDRESS_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Адрес')]")
    # Поле Станция метро
    METRO_INPUT = (By.XPATH, "//input[contains(@placeholder,'* Станция метро')]")


    # Локаторы для станций метро
    # Только видимые станции при раскрытии списка
    METRO_STATION_VISIBLE = (By.XPATH, '//*[@class="select-search__row" '
                                       'and @role="menuitem"]')


    # Поле Телефон
    PHONE_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Телефон')]")

    # Кнопка Далее
    NEXT_BUTTON = (By.XPATH, '//button[contains(text(), "Далее")]')


    # ФОРМА Про аренду
    # Когда привезти
    DATE_INPUT = (By.XPATH,
                  './/input[@placeholder="* Когда привезти самокат"]')
    # Выпадающий календарик
    DAY_LOCATOR = (By.XPATH,
                   './/div[contains(@class, "react-datepicker__day--today")]')

    # Локатор для Dropdown срока аренды
    RENTAL_DURATION_DROPDOWN = (By.XPATH,
                                '//div[@class="Dropdown-control"]')
    # Выпадающее меню со сроками
    RENTAL_DURATION_OPTION = (By.XPATH,
                              '//div[@class="Dropdown-menu"]//div[text()="{}"]')

    # Цвет самоката
    COLOR_BLACK_CHECKBOX = (By.ID, "black")
    COLOR_GREY_CHECKBOX = (By.ID, "grey")

    # Комментарий для курьера
    COMMENT_INPUT = (By.XPATH,
                     "//input[contains(@placeholder, 'Комментарий')]")
    # Кнопка "Заказать"
    MAKE_ORDER_BUTTON = (By.XPATH,
                         '//button[contains(@class, "Button_Middle") '
                         'and contains(text(), "Заказать")]')

    # Кнопка заказа вверху страницы
    ORDER_BUTTON_HEADER = (By.XPATH, '//button[contains('
                                     '@class, "Button_Button") and contains('
                                     'text(), "Заказать")]')

    # Локатор для кнопок "Заказать" нижняя часть страницы
    ORDER_BUTTON_ALL_SIZES = (By.XPATH,
                              '//div[contains(@class, "Home_FinishButton")]'
                              '/button[contains(@class, "Button_Button") '
                              'and contains(text(), "Заказать")]')

    # ФОРМА Подтверждение заказа
    # Кнопка "Да"
    YES_BUTTON = (By.XPATH, '//button[contains(@class, "Button_Button") '
                            'and contains(text(), "Да")]')

    # Окно Заказ создан 
    FINALL_WINDOW = (By.XPATH, '//div[contains(@class,"Order_ModalHeader") and contains(text(), "Заказ оформлен")]')


