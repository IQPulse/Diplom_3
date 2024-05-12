from selenium.webdriver.common.by import By

class MainPageLocators:
    INGREDIENT_1 = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")  # Первый ингредиент
    INGREDIENT_2 = (By.XPATH, "//img[@alt='Соус Spicy-X']")  # Второй ингредиент
    INGREDIENT_3 = (By.XPATH, "//img[@alt='Мясо бессмертных моллюсков Protostomia']")  # Третий ингредиент
    SAUCE_BUTTON = (By.XPATH, "//body/div[@id='root']/div[@class='App_App__aOmNj']/main[@class='App_componentContainer__2JC2W']/section[@class='BurgerIngredients_ingredients__1N8v2']/div[1]")  # Кнопка "Соусы"
    FILLING_BUTTON = (By.XPATH, "//span[contains(text(),'Начинки')]")  # Кнопка "Начинки"
    ADD_INGREDIENT_BUTTON = (By.XPATH, "//div[@class='constructor-element constructor-element_pos_top']//span[@class='constructor-element__row']//span[1]")  # Поле сборки бургера
    CLOSE_MODAL_BUTTON = (By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//button[@type='button']//*[name()='svg']")  # Закрытие модального окна
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")  # Кнопка "Оформить заказ"
    ORDER_WAIT = (By.XPATH, "//h2[normalize-space()='9999']")  # Начальный счетчик заказов на модальном окне "9999"
    ORDER_IDENTIFIER = (By.XPATH, "//h1[contains(text(),'Лента заказов')]")  # Кнопка "Лента заказов"
    INGREDIENT_DETAILS = (By.XPATH, "//h2[contains(text(),'Детали ингредиента')]")  # Карточка ингредиента текст "Детали ингредиента"
    COUNTER_INCREASE = (By.XPATH, "//p[normalize-space()='2']")  # Счетчик ингредиента
    WAIT_FOR_READINESS = (By.XPATH, "// p[contains(text(), 'Дождитесь готовности на орбитальной станции')]")  # Текст "Дождитесь готовности на орбитальной станции" на модальном окне
    FIND_AND_SAVE_ELEMENT_ORDER_NUMBER_APPEARS = (By.XPATH, "/html/body/div[1]/div/section/div[1]/div/h2")  # Номер "Заказа на Главной странице"
