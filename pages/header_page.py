import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.header_page_locators import HeaderPageLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):

    @allure.step('Клик по логотипу Яндекса в хедере')
    def click_yandex_logo(self):
        self.click_element(HeaderPageLocators.HEADER_LOGO_YANDEX)

    @allure.step('Клик по логотипу Самоката в хедере')
    def click_scooter_logo(self):
        self.click_element(HeaderPageLocators.HEADER_LOGO_SCOOTER)

    @allure.step('Ожидаем что открытая страница будет содержать {url}')
    def wait_for_url(self, url):
        driver = self.driver
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(self.driver, 6).until(expected_conditions.url_contains(url))
        return self.driver.current_url
