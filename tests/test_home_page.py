import allure
import pytest
from data import text
from pages.home_page import HomePage


class TestHomePage:

    @allure.title('Проверка соответствия текста ответа в открывающемся аккордеон вопросов')
    @allure.description('Проверяем что при раскрытии каждого аккордеона открывается соответсвующий ему текст')
    @pytest.mark.parametrize("index, text_of_answer",
                             [(0, text[0]),
                              (1, text[1]),
                              (2, text[2]),
                              (3, text[3]),
                              (4, text[4]),
                              (5, text[5]),
                              (6, text[6]),
                              (7, text[7])])
    def test_check_answers(self, driver, index, text_of_answer):
        home_page = HomePage(driver)
        home_page.click_cookie_button()
        home_page.scroll_to_questions()
        question = home_page.tap_question(index)
        result = home_page.find_answer(index)
        assert text_of_answer[question] == result
