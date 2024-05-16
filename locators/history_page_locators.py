from selenium.webdriver.common.by import By

class HistoryPageLocators:
    POPUP_WINDOW = (By.XPATH, "(//p[@class='undefined text text_type_main-default mb-15'])[1]")  # Модальное окно "Заказ в Истории заказов"
    ORDER_HISTORY_BLANK = (By.XPATH, "//a[@class='OrderHistory_link__1iNby']")  # Карточка "Заказа в Истории заказов"
