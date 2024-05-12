from selenium.webdriver.common.by import By

class FeedPageLocators:
    COPY_ORDER_NUMBER = (By.XPATH, "/html/body/div/div/section[2]/div[1]/div/p[1]")  # Номер "Заказа"
    SEARCH_ORDER_IN_FEED_PAGE = (By.XPATH, "/html/body/div[1]/div/main/div/div/ul/li[1]/a/div[1]/p[1]")  # Поиск "Заказа"
    FIND_AND_SAVE_ELEMENT_COUNTER_INCREASES = (By.XPATH, "/html/body/div[1]/div/main/div/div/div/div[2]/p[2]")  # Счетчик "Выполнено за все время"
    FIND_AND_SAVE_ELEMENT_COUNTER_INCREASES_TODAY = (By.XPATH, "/html/body/div[1]/div/main/div/div/div/div[3]/p[2]")  # Счетчик "Выполнено за сегодня"
    FIND_AND_SAVE_ELEMENT_ORDER_NUMBER_APPEARS_FEED = (By.XPATH, "/html/body/div[1]/div/main/div/div/ul/li[1]/a/div[1]/p[1]")  # Номер "Заказа в Ленте заказов"
    CLICK_COMPONENT_CONTAINER = (By.XPATH, "//main[@class='App_componentContainer__2JC2W']//li[1]//a[1]")  # Модальное окно "Заказ в Ленте заказов"
