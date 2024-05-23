import allure
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):

    @allure.step('Кликаем на кнопку "Заказать" в середине страницы')
    def click_bottom_button_order(self):
        self.scroll_to_element(HomePageLocators.BUTTON_ORDER_BOTTOM)
        self.click_element(HomePageLocators.BUTTON_ORDER_BOTTOM)

    @allure.step('Скроллим до раздела "Вопросы о важном" с аккардеоном внизу страницу')
    def scroll_to_questions(self):
        self.scroll_to_element(HomePageLocators.TITLE_IMPORT_QUEST)

    @allure.step('Тапаем на вопрос в аккордеоне')
    def tap_question(self, index):
        selector, locator = HomePageLocators.QUESTION_ACCORDION
        locator = locator.format(index)
        self.wait_element((selector, locator))
        self.click_element((selector, locator))
        return self.wait_element((selector, locator)).get_attribute("id")

    @allure.step('Ищем текст ответа в открывшемся элементе аккордеона')
    def find_answer(self, index):
        selector, locator = HomePageLocators.ANSWER_ACCORDION
        locator = locator.format(index)
        element = self.wait_element((selector, locator))
        return element.text
