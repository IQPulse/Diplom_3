from selenium.webdriver.common.by import By

class ProfilePageLocators:
    PROFILE_LINK = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")  # Ссылка "Личный кабинет"
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")  # Ссылка "Выход"
    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[contains(text(),'История заказов')]")  # Ссылка "История заказов"
