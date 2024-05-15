import allure
from utils.urls import URLs
from locators.password_page_locators import PasswordPageLocators
from pages.password_page import PasswordPage

@allure.feature("Тесты страницы восстановления пароля")
class TestPasswordPage:
    @allure.title("Проверка заголовка страницы восстановления пароля")
    def test_reset_password_page_title(self, driver):
        password_page = PasswordPage(driver)
        password_page.navigate_to_page(URLs.LOGIN_PAGE_URL)
        password_page.click_reset_button()
        element = password_page.find_element(*PasswordPageLocators.PASSWORD_RECOVERY_BUTTON)
        assert "Восстановление пароля" in element.text

    @allure.title("Ввод почты и сброс пароля")
    def test_enter_email_and_click_reset(self, driver):
        password_page = PasswordPage(driver)
        password_page.navigate_to_page(URLs.FORGOT_PASSWORD_URL)
        password_page.enter_email_and_click_reset("test@example.com")
        result_locator = (PasswordPageLocators.EMAIL_INPUT)
        result = driver.find_element(*result_locator)
        assert result.is_displayed()

    @allure.title("Показать/скрыть пароль")
    def test_show_hide_password_button(self, driver):
        password_page = PasswordPage(driver)
        password_page.navigate_to_page(URLs.RESET_PASSWORD_URL)
        password_page.enter_email_and_click_reset("test@example.com")
        password_page.enter_new_password("123456")
        password_page.click_show_hide_password_button()
        password_field = password_page.find_element(*PasswordPageLocators.NEW_PASSWORD_FIELD)
        password_value = password_field.get_attribute("value")
        assert password_value == "123456"
