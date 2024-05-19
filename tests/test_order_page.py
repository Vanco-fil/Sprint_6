import allure
import pytest
from data import personal_date
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Проверка оформления аренды самоката через кнопку "Заказать" в хедере')
    @allure.description('Проверяем возможность успешного оформления аренды с 2 наборами данных через кнопку в хедере страницы')
    @pytest.mark.parametrize('name, surname, address, metro, number', [*personal_date])
    def test_successful_order_header_button(self, driver, name, surname, address, metro, number):
        order_page = OrderPage(driver)
        base_page = BasePage(driver)
        base_page.click_header_button_order()
        order_page.enter_rental_details(name, surname, address, metro, number)
        text_order = order_page.successful_order_modal()
        assert "Заказ оформлен" in text_order

    @allure.title('Проверка оформления аренды самоката через кнопку "Заказать" внизу страницы')
    @allure.description('Проверяем возможность успешного оформления аренды с 2 наборами данных через кнопку внизу страницы')
    @pytest.mark.parametrize('name, surname, address, metro, number', [*personal_date])
    def test_successful_order_bottom_button(self, driver, name, surname, address, metro, number):
        order_page = OrderPage(driver)
        home_page = HomePage(driver)
        home_page.click_bottom_button_order()
        order_page.enter_rental_details(name, surname, address, metro, number)
        text_order = order_page.successful_order_modal()
        assert "Заказ оформлен" in text_order
