import pytest
from selenium import webdriver
from data import URL_SCOOTER, RESOLUTION


@pytest.fixture(scope="function")
def driver():
    """Фикстура для запуска браузера Firefox."""
    firefox_options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=firefox_options)
    driver.set_window_size(*RESOLUTION)
    driver.get(URL_SCOOTER)
    yield driver
    driver.quit()
