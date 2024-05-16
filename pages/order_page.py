import allure
from helpers import create_random_data
from locators.base_page_locators import BasePageLocators
from locators.home_page_locators import HomePageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Кликаем на кнопку "Заказать" в хедере страницы')
    def click_header_button_order(self):
        self.click_element(BasePageLocators.BUTTON_ORDER_HEADER)

    @allure.step('Кликаем на кнопку "Заказать" в середине страницы')
    def click_bottom_button_order(self):
        self.scroll_to_element(HomePageLocators.BUTTON_ORDER_BOTTOM)
        self.click_element(HomePageLocators.BUTTON_ORDER_BOTTOM)

    @allure.step('Вводим имя')
    def input_name(self, name):
        self.enter_text(OrderPageLocators.INPUT_NAME, name)

    @allure.step('Вводим фамилию')
    def input_surname(self, surname):
        self.enter_text(OrderPageLocators.INPUT_SURNAME, surname)

    @allure.step('Вводим адрес')
    def input_address(self, address):
        self.enter_text(OrderPageLocators.INPUT_ADDRESS, address)

    @allure.step('Выбираем метро из списка')
    def choose_metro(self, metro):
        self.click_element(OrderPageLocators.INPUT_METRO_STATION)
        self.enter_text(OrderPageLocators.INPUT_METRO_STATION, metro)
        self.click_element(OrderPageLocators.METRO_STATION)

    @allure.step('Вводим номер телефона')
    def input_phone_number(self, number):
        self.enter_text(OrderPageLocators.INPUT_PHONE_NUMBER, number)

    @allure.step('Вводим случайную дату начала аренды')
    def input_date_start_rent(self):
        date = create_random_data()
        self.enter_text(OrderPageLocators.INPUT_DATE, date)
        self.click_element(OrderPageLocators.TITLE_ABOUT_RENT)

    @allure.step('Выбираем срок аренды')
    def choose_rent_period(self):
        self.click_element(OrderPageLocators.INPUT_RENTAL_PERIOD)
        self.click_element(OrderPageLocators.TWO_DAYS_RENT)

    @allure.step('Вводим все пользовательские данные для заказа аренды')
    def enter_rental_details(self, name, surname, address, metro, number):
        self.input_name(name)
        self.input_surname(surname)
        self.input_address(address)
        self.choose_metro(metro)
        self.input_phone_number(number)
        self.click_element(OrderPageLocators.BUTTON_NEXT)
        self.wait_element(OrderPageLocators.TITLE_ABOUT_RENT)
        self.input_date_start_rent()
        self.choose_rent_period()
        self.click_element(OrderPageLocators.BUTTON_ORDER)
        self.click_element(OrderPageLocators.BUTTON_YES_CHECKOUT)

    @allure.step('Ожидаем модалку подтверждения успешного заказа')
    def successful_order_modal(self):
        element = self.wait_element(OrderPageLocators.TITLE_SUCCESSFUL_ORDER)
        return element.text
