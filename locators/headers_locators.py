from selenium.webdriver.common.by import By

class HeadersLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")  # Кнопка "Конструктор"
    ORDERS_FEED_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")  # Кнопка "Лента заказов"
