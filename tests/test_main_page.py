import allure
import pytest

from data import AnswerText, QuestionText
from pages.main_page import MainPage



@allure.suite('Проверяем FAQ')
class TestMainPage:

    @allure.title("Проверка ответов на вопросы")
    @allure.description("Принимаем куки, скроллим страницу, "
                        "кликаем поочерёдно на каждый вопрос и "
                        "сравниваем полученный ответ с ответом из словаря")

    @pytest.mark.parametrize("index", range(len(QuestionText.QUESTIONS)))
    def test_questions_and_answers(self, driver, index):
        main_page = MainPage(driver)

        question_text = QuestionText.QUESTIONS[index]
        
        with allure.step(f'Кликаем на вопрос "{question_text}"'
                         f' и проверяем ответ'):
            expected_answer_text = AnswerText.ANSWERS[index]

            actual_answer_text = main_page.get_answer_text(index)

            assert actual_answer_text == expected_answer_text, (
                f'Ошибка для вопроса: "{question_text}".\n'
                f'Ожидали: {expected_answer_text}\n'
                f'Получили: {actual_answer_text}'
            )
