from selenium.webdriver.common.by import By


class HeaderPageLocators:
    """Локаторы логотипов в хедере сайта"""
    # Логотип Яндекса в хедере сайта
    HEADER_LOGO_YANDEX = (By.XPATH, "//a[contains(@class,'Header_LogoYandex')]")

    # Логотип Самокат в хедере сайта
    HEADER_LOGO_SCOOTER = (By.XPATH, "//a[contains(@class,'Header_LogoScooter')]")
