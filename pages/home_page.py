import allure
from pages.base_page import BasePage


class HomePage(BasePage):

    @allure.step('Тапаем на вопрос в аккордеоне')
    def tap_question(self, locator, index):
        selector, locator = locator
        locator = locator.format(index)
        self.wait_element((selector, locator))
        self.click_element((selector, locator))
        return self.wait_element((selector, locator)).get_attribute("id")

    @allure.step('Ищем текст ответа в открывшемся элементе аккордеона')
    def find_answer(self, locator, index):
        selector, locator = locator
        locator = locator.format(index)
        element = self.wait_element((selector, locator))
        return element.text
