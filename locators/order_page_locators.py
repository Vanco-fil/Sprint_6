from selenium.webdriver.common.by import By


class OrderPageLocators:
    """Локаторы элементов на странице оформления заказа"""
    # Заголовок "Для кого самокат"
    TITLE_ORDER = (By.XPATH, "//div[text()='Для кого самокат']")

    # Поле ввода имени
    INPUT_NAME = (By.XPATH, "//input[@placeholder='* Имя']")

    # Поле ввода фамилии
    INPUT_SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")

    # Поле ввода адреса для заказа
    INPUT_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")

    # Поле выпадающего списка со станциями метро
    INPUT_METRO_STATION = (By.CLASS_NAME, "select-search__input")

    # Поле ввода номера телефона
    INPUT_PHONE_NUMBER = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    # Станция метро 'Черкизовская' в списке станций
    METRO_STATION = (By.XPATH, "//div[text()='Черкизовская']")

    # Кнопка Далее странице заказа
    BUTTON_NEXT = (By.CLASS_NAME, "Button_Button__ra12g.Button_Middle__1CSJM")

    # Заголовок 'Про аренду' на странице заказа
    TITLE_ABOUT_RENT = (By.XPATH, "//div[text()='Про аренду']")

    # Поле ввода даты когда привезти самокат
    INPUT_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")

    # Поле выпадающего списка срока аренды
    INPUT_RENTAL_PERIOD = (By.XPATH, "//div[text()='* Срок аренды']")

    # Вариант 'двое суток' в списке срока аренды
    TWO_DAYS_RENT = (By.XPATH, "//div[@class = 'Dropdown-option' and text()='двое суток']")

    # Чекбокс выбор цвета самоката 'чёрный жемчуг'
    CHECKBOX_BLACK = (By.ID, "black")

    # Поле ввода комментария для курьера
    INPUT_COMMENT_COURIER = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    # Кнопка 'Заказать' для оформления заказа
    BUTTON_ORDER = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")

    # Модальное окно подтверждения заказа
    MODAL_CHECKOUT = (By.XPATH, "Order_Modal__YZ-d3")

    # Кнопка 'Да' в модальном окне подтверждения заказа
    BUTTON_YES_CHECKOUT = (By.XPATH, "//button[text()='Да']")

    # Заголовок 'Заказ оформлен' в модалке успешно оформленного заказа
    TITLE_SUCCESSFUL_ORDER = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")

    # Кнопка 'Посмотреть статус' в модалке успешно оформленного заказа
    BUTTON_SEE_STATUS = (By.CLASS_NAME, "//button[text()='Посмотреть статус']")
