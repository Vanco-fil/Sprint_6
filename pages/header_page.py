import allure
from locators.header_page_locators import HeaderPageLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):

    @allure.step('Клик по логотипу Яндекса в хедере')
    def click_yandex_logo(self):
        self.click_element(HeaderPageLocators.HEADER_LOGO_YANDEX)

    @allure.step('Клик по логотипу Самоката в хедере')
    def click_scooter_logo(self):
        self.click_element(HeaderPageLocators.HEADER_LOGO_SCOOTER)

    @allure.step('Ожидаем что открытая страница в новом окне будет содержать {url}')
    def wait_for_url(self, url):
        self.switch_to_last_window()
        url = self.wait_url_contains(url)
        return url
