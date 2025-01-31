import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждем {locator}')
    def wait_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ожидаем что {locator} станет кликабельным')
    def wait_element_clickable(self, locator):
        element = WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))
        return element

    @allure.step('Кликаем на {locator}')
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Скроллим к {locator}')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Печатаем {text} в {locator}')
    def enter_text(self, locator, text):
        self.wait_element_clickable(locator)
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Кликаем на кнопку "Заказать" в хедере страницы')
    def click_header_button_order(self):
        self.click_element(BasePageLocators.BUTTON_ORDER_HEADER)

    @allure.step('Переключаем активное окно браузера на последнее открытое окно')
    def switch_to_last_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Ожидаем URL текущей страницы')
    def wait_url_contains(self, url):
        WebDriverWait(self.driver, 6).until(expected_conditions.url_contains(url))
        return self.driver.current_url

    @allure.step('Ждем окно о куках и закрываем его')
    def click_cookie_button(self):
        self.wait_element(BasePageLocators.BUTTON_COOKIE)
        self.click_element(BasePageLocators.BUTTON_COOKIE)
