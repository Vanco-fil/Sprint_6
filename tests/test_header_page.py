import allure
from data import URL_DZEN
from pages.header_page import HeaderPage
from pages.order_page import OrderPage


class TestHeaderPage:

    @allure.title('Проверка кликабельности и перехода по логотипу "Яндекс"')
    @allure.description('Проверяем кликабельность логотипа Яндекса, что после тапа на него '
                        'в новом окне откроется главная страница Дзена')
    def test_check_yandex_logo_click(self, driver):
        header_page = HeaderPage(driver)
        header_page.click_yandex_logo()
        url = header_page.wait_for_url(URL_DZEN)
        assert URL_DZEN in url

    @allure.title('Проверка кликабельности и перехода на главную по логотипу "Самокат"')
    @allure.description('Проверяем кликабельность логотипа «Самокат», что после тапа не него '
                        'попадаем на главную страницу')
    def test_check_scooter_logo_click(self, driver):
        order_page = OrderPage(driver)
        header_page = HeaderPage(driver)
        order_page.click_header_button_order()
        order_url = driver.current_url
        header_page.click_scooter_logo()
        home_url = driver.current_url
        assert order_url != home_url
