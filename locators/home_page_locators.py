from selenium.webdriver.common.by import By


class HomePageLocators:
    """Локаторы элементов на главной страницы сайта"""
    # Кнопка 'Заказать' в середине страницы
    BUTTON_ORDER_BOTTOM = (By.XPATH, "//div[contains(@class,'Home_FinishButton')]/button[text()='Заказать']")

    # Заголовок на главной странице "Самокат на пару дней"
    TITLE_HOME = (By.CLASS_NAME, "Home_Header__iJKdX")

    # Вопрос в раскрывающемся аккардеоне без индекса
    QUESTION_ACCORDION = (By.ID, "accordion__heading-{}")

    # Ответ в раскрывающемся аккардеона без индекса
    ANSWER_ACCORDION = (By.ID, "accordion__panel-{}")

    # Заголовок вопросы о важном
    TITLE_IMPORT_QUEST = (By.XPATH, "//div[text()='Вопросы о важном']")
    