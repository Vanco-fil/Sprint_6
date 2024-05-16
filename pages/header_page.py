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
