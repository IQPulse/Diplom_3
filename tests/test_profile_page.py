import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.urls import URLs

@allure.feature("Тесты страницы профиля")
class TestProfilePage:
    @allure.title("Переход по ссылке профиля")
    def test_click_profile_link(self, driver, profile_page, user_data):
        profile_page.open_login_page()
        profile_page.login(user_data["email"], user_data["password"])
        profile_page.go_to_profile()
        WebDriverWait(driver, 10).until(EC.url_to_be(URLs.PROFILE_URL))
        assert driver.current_url == URLs.PROFILE_URL

    @allure.title("Переход по ссылке истории заказов")
    def test_click_order_history_link(self, driver, profile_page, user_data):
        profile_page.open_login_page()
        profile_page.login(user_data["email"], user_data["password"])
        profile_page.go_to_profile()
        profile_page.go_to_order_history()
        WebDriverWait(driver, 10).until(EC.url_to_be(URLs.ORDER_HISTORY_URL))
        assert driver.current_url == URLs.ORDER_HISTORY_URL

    @allure.title("Выход из профиля")
    def test_logout(self, driver, profile_page, user_data):
        profile_page.open_login_page()
        profile_page.login(user_data["email"], user_data["password"])
        profile_page.go_to_profile()
        profile_page.logout()
        WebDriverWait(driver, 10).until(EC.url_to_be(URLs.LOGIN_PAGE_URL))
        assert driver.current_url == URLs.LOGIN_PAGE_URL
