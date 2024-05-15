from selenium.webdriver.common.by import By

class FeedPageLocators:
    COPY_ORDER_NUMBER = (By.XPATH, " (//p[@class='text text_type_digits-default mb-10 mt-5'])[1]")  # Номер "Заказа"
    SEARCH_ORDER_IN_FEED_PAGE = (By.XPATH, "(//p[contains(@class,'digits-default')])[1]")  # Поиск "Заказа"
    FIND_AND_SAVE_ELEMENT_COUNTER_INCREASES = (By.XPATH, "(//p[contains(@class,'digits-large')])[1]")  # Счетчик "Выполнено за все время"
    FIND_AND_SAVE_ELEMENT_COUNTER_INCREASES_TODAY = (By.XPATH, "(//p[contains(@class,'digits-large')])[2]")  # Счетчик "Выполнено за сегодня"
    CLICK_COMPONENT_CONTAINER = (By.XPATH, "//main[@class='App_componentContainer__2JC2W']//li[1]//a[1]")  # Модальное окно "Заказ в Ленте заказов"
