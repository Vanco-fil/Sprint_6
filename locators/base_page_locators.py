from selenium.webdriver.common.by import By


class BasePageLocators:
    """Локаторы общих элементов сайта"""
    # Кнопка 'Заказать' в хедере сайта
    BUTTON_ORDER_HEADER = (By.XPATH, "//div[contains(@class,'Header_Nav')]/button[text()='Заказать']")

    # Кнопка 'Статус заказа' в хедере сайта
    BUTTON_ORDER_STATUS = (By.XPATH, "//div[contains(@class,'Header_Nav')]/button[text()=Статус заказа']")

    # Поле ввода номера заказа в хедере сайта
    INPUT_ORDER_NUMBER = (By.XPATH, "//input[@placeholder='Введите номер заказа']")

    # Кнопка 'Go' для поиска номера заказа
    BUTTON_REGISTER_LINK = (By.XPATH, "//div[contains(@class,'Header_SearchInput')]/button[text()='Go!']")

    # Кнопка 'да все привыкли' в модальном запиненом окне для кук внизу
    BUTTON_COOKIE = (By.ID, "rcc-confirm-button")
