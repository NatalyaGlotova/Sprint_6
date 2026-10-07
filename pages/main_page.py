import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Получаем текста ответа для вопроса {index}')
    def get_answer_text(self, index):
        question_locator = self.format_locators(
            MainPageLocators.QUESTION_TEMPLATE, index)
        answer_locator = self.format_locators(
            MainPageLocators.ANSWER_TEMPLATE, index)
        
        self.scroll_page_down()
        self.wait_for_element_clickable(question_locator)
        self.click_with_actions(question_locator)
        self.wait_for_element_visible(answer_locator)

        return self.get_text_from_element(answer_locator)

        

