import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.password_page_locators import PasswordPageLocators
from utils.urls import URLs

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу входа")
    def open_login_page(self):
        self.driver.get(URLs.LOGIN_PAGE_URL)

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.driver.get(URLs.MAIN_PAGE_URL)

    @allure.step("Выполнить вход с электронной почтой {email} и паролем {password}")
    def login(self, email, password):
        with allure.step("Ввести электронную почту"):
            self.driver.find_element(*PasswordPageLocators.EMAIL_INPUT).send_keys(email)
        with allure.step("Ввести пароль"):
            self.driver.find_element(*PasswordPageLocators.PASSWORD_INPUT).send_keys(password)
        with allure.step("Дождаться видимости кнопки входа"):
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PasswordPageLocators.LOGIN_BUTTON))
        with allure.step("Нажать кнопку входа"):
            self.driver.find_element(*PasswordPageLocators.LOGIN_BUTTON).click()

