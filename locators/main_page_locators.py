from selenium.webdriver.common.by import By


class MainPageLocators:
    #  Вопросы
    QUESTION_TEMPLATE = (By.XPATH, "//div[@id='accordion__heading-{0}']")
    # Ответы
    ANSWER_TEMPLATE = (By.XPATH, "//div[@id='accordion__panel-{0}']")

    # Кнопка заказа вверху страницы
    ORDER_BUTTON_HEADER = (By.XPATH, '//button[contains('
                                     '@class, "Button_Button") and contains('
                                     'text(), "Заказать")]')
    # Кнопка заказа в середине страницы
    ORDER_BUTTON_MIDDLE = (By.XPATH, '//button[contains(@class,'
                                     ' "Button_Button") and contains('
                                     '@class, "Button_Middle") and contains('
                                     'text(), "Заказать")]')
    
