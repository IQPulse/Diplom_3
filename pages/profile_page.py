import allure
from locators.profile_page_locators import ProfilePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProfilePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Перейти в профиль")
    def go_to_profile(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((ProfilePageLocators.PROFILE_LINK))
        )
        profile_link = self.driver.find_element(*ProfilePageLocators.PROFILE_LINK)
        profile_link.click()

    @allure.step("Выйти из профиля")
    def logout(self):
        # Ожидание появления кнопки выхода
        logout_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((ProfilePageLocators.LOGOUT_BUTTON))
        )
        logout_button.click()

    @allure.step("Перейти в историю заказов")
    def go_to_order_history(self):
        order_history_link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((ProfilePageLocators.ORDER_HISTORY_BUTTON))
        )
        order_history_link.click()
