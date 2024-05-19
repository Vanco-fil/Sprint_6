import allure
import pytest
import data
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
from pages.home_page import HomePage


class TestHomePage:

    @allure.title('Проверка соответствия текста ответа в открывающемся аккордеон вопросов')
    @allure.description('Проверяем что при раскрытии каждого аккордеона открывается соответсвующий ему текст')
    @pytest.mark.parametrize("index, text_of_answer",
                             [(0, data.text[0]),
                              (1, data.text[1]),
                              (2, data.text[2]),
                              (3, data.text[3]),
                              (4, data.text[4]),
                              (5, data.text[5]),
                              (6, data.text[6]),
                              (7, data.text[7])])
    def test_check_answers(self, driver, index, text_of_answer):
        home_page = HomePage(driver)
        home_page.click_cookie_button()
        home_page.scroll_to_questions()
        question = home_page.tap_question(HomePageLocators.QUESTION_ACCORDION, index)
        result = home_page.find_answer(HomePageLocators.ANSWER_ACCORDION, index)
        assert text_of_answer[question] == result
