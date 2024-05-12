from selenium.webdriver.common.by import By

class HistoryPageLocators:
    POPUP_WINDOW = (By.XPATH, "/html/body/div[1]/div/section[2]/div[1]/div/p[2]")  # Модальное окно "Заказ в Истории заказов"
    ORDER_HISTORY_BLANK = (By.XPATH, "//a[@class='OrderHistory_link__1iNby']")  # Карточка "Заказа в Истории заказов"
