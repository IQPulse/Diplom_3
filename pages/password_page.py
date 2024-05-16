import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.password_page_locators import PasswordPageLocators

class PasswordPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Переход на страницу по URL")
    def navigate_to_page(self, url):
        self.driver.get(url)

    @allure.step("Нажать кнопку 'Восстановить пароль'")
    def click_reset_button(self):
        reset_button = self.driver.find_element(*PasswordPageLocators.RESET_BUTTON)
        reset_button.click()

    @allure.step("Ввести email и нажать кнопку 'Восстановить'")
    def enter_email_and_click_reset(self, email):
        email_field = self.driver.find_element(*PasswordPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        reset_button = self.driver.find_element(*PasswordPageLocators.RESET_BUTTON_EMAIL)
        reset_button.click()

    @allure.step("Ввести новый пароль")
    def enter_new_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((PasswordPageLocators.NEW_PASSWORD_FIELD))
        )
        password_field = self.driver.find_element(*PasswordPageLocators.NEW_PASSWORD_FIELD)
        password_field.send_keys(password)

    @allure.step("Нажать кнопку 'Показать/скрыть пароль'")
    def click_show_hide_password_button(self):
        show_hide_button = self.driver.find_element(*PasswordPageLocators.CLICK_SHOW_HIDE_PASSWORD_BUTTON)
        show_hide_button.click()

    @allure.step("Найти элемент")
    def find_element(self, by, value):
        return self.driver.find_element(by, value)
