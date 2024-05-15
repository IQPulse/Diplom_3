import allure
from locators.profile_page_locators import ProfilePageLocators
from locators.feed_page_locators import FeedPageLocators
from locators.history_page_locators import HistoryPageLocators
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class FeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Закрыть окно заказа")
    def close_order_window(self):
        self.driver.refresh()

    @allure.step("Открыть профиль")
    def open_profile(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((ProfilePageLocators.PROFILE_LINK)))
        self.driver.find_element(*ProfilePageLocators.PROFILE_LINK).click()

    @allure.step("Открыть историю заказов")
    def open_order_history(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((ProfilePageLocators.ORDER_HISTORY_BUTTON)))
        self.driver.find_element(*ProfilePageLocators.ORDER_HISTORY_BUTTON).click()

    @allure.step("Открыть пустую историю заказов")
    def open_order_history_blank(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((HistoryPageLocators.ORDER_HISTORY_BLANK)))
        self.driver.find_element(*HistoryPageLocators.ORDER_HISTORY_BLANK).click()

    @allure.step("Скопировать номер заказа в истории заказов")
    def copy_order_number_in_order_history(self):
        element = self.driver.find_element(*FeedPageLocators.COPY_ORDER_NUMBER)
        value = element.text
        return value

    @allure.step("Поиск заказа на странице ленты заказов")
    def search_order_in_feed_page(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((FeedPageLocators.SEARCH_ORDER_IN_FEED_PAGE)))
        element = self.driver.find_element(*FeedPageLocators.SEARCH_ORDER_IN_FEED_PAGE)
        value = element.text
        return value

    @allure.step("Найти и сохранить значение счетчика увеличений")
    def find_and_save_element_counter_increases(self):
        element = self.driver.find_element(*FeedPageLocators.FIND_AND_SAVE_ELEMENT_COUNTER_INCREASES)
        value = element.text
        return int(value)

    @allure.step("Найти и сохранить значение счетчика увеличений за сегодня")
    def find_and_save_element_counter_increases_today(self):
        element = self.driver.find_element(*FeedPageLocators.FIND_AND_SAVE_ELEMENT_COUNTER_INCREASES_TODAY)
        value = element.text
        return int(value)

    @allure.step("Найти и сохранить номер заказа встречающегося в истории заказов")
    def find_and_save_element_order_number_appears(self):
        WebDriverWait(self.driver, 10).until_not(
            EC.text_to_be_present_in_element((MainPageLocators.FIND_AND_SAVE_ELEMENT_ORDER_NUMBER_APPEARS), "9999"))
        element = self.driver.find_element(*MainPageLocators.FIND_AND_SAVE_ELEMENT_ORDER_NUMBER_APPEARS)
        value = element.text
        return "#0" + value

    @allure.step("Найти и сохранить номер заказа в ленте заказов")
    def find_and_save_element_order_number_appears_feed(self):
        element = self.driver.find_element(*FeedPageLocators.SEARCH_ORDER_IN_FEED_PAGE)
        value = element.text
        return value

    @allure.step("Вернуться назад")
    def go_back(self):
        self.driver.back()

    @allure.step("Нажать на контейнер компонентов")
    def click_component_container(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((FeedPageLocators.CLICK_COMPONENT_CONTAINER)))
        self.driver.find_element(*FeedPageLocators.CLICK_COMPONENT_CONTAINER).click()
