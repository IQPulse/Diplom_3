import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from locators.main_page_locators import MainPageLocators
from locators.headers_locators import HeadersLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Нажать кнопку 'Конструктор'")
    def click_constructor_button(self):
        self.driver.find_element(*HeadersLocators.CONSTRUCTOR_BUTTON).click()

    @allure.step("Нажать кнопку 'Лента Заказов'")
    def click_orders_feed_button(self):
        self.driver.find_element(*HeadersLocators.ORDERS_FEED_BUTTON).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.ORDER_IDENTIFIER))

    @allure.step("Нажать на карточку ингредиента")
    def click_ingredient_card(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.INGREDIENT_1))
        self.driver.find_element(*MainPageLocators.INGREDIENT_1).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.INGREDIENT_DETAILS))

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.driver.find_element(*MainPageLocators.CLOSE_MODAL_BUTTON).click()

    @allure.step("Добавить ингредиент в корзину")
    def add_ingredient_to_cart(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.INGREDIENT_1))
        ingredient_card_1 = self.driver.find_element(*MainPageLocators.INGREDIENT_1)
        cart = self.driver.find_element(*MainPageLocators.ADD_INGREDIENT_BUTTON)
        ActionChains(self.driver).drag_and_drop(ingredient_card_1, cart).perform()
        self.driver.find_element(*MainPageLocators.SAUCE_BUTTON).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.INGREDIENT_2))
        ingredient_card_2 = self.driver.find_element(*MainPageLocators.INGREDIENT_2)
        cart = self.driver.find_element(*MainPageLocators.ADD_INGREDIENT_BUTTON)
        ActionChains(self.driver).drag_and_drop(ingredient_card_2, cart).perform()
        self.driver.find_element(*MainPageLocators.SAUCE_BUTTON).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.INGREDIENT_3))
        ingredient_card_3 = self.driver.find_element(*MainPageLocators.INGREDIENT_3)
        cart = self.driver.find_element(*MainPageLocators.ADD_INGREDIENT_BUTTON)
        ActionChains(self.driver).drag_and_drop(ingredient_card_3, cart).perform()
        wait = WebDriverWait(self.driver, 5)
        wait.until_not(EC.text_to_be_present_in_element(MainPageLocators.ORDER_WAIT, '9999'))

    @allure.step("Нажать кнопку 'Оформить заказ'")
    def click_orders_button(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        self.driver.find_element(*MainPageLocators.ORDER_BUTTON).click()

    @allure.step("Получить идентификатор заказа")
    def get_order_identifier(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.ORDER_IDENTIFIER)).text
