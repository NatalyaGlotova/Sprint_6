from selenium.webdriver.common.by import By


class MainPageLocators:
    #  Вопросы
    QUESTION_TEMPLATE = (By.XPATH, "//div[@id='accordion__heading-{0}']")
    # Ответы
    ANSWER_TEMPLATE = (By.XPATH, "//div[@id='accordion__panel-{0}']")

