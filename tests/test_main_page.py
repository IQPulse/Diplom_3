import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators

@allure.feature("Тесты главной страницы")
class TestMainPage:

    @allure.title("Нажатие на кнопку 'Конструктор'")
    def test_click_constructor_button(self, main_page):
        main_page.open_login_page()
        main_page.click_constructor_button()
        assert "Соберите бургер" in main_page.driver.page_source

    @allure.title("Нажатие на кнопку 'Лента Заказов'")
    def test_click_orders_feed_button(self, main_page):
        main_page.open_main_page()
        main_page.click_orders_feed_button()
        assert "Лента заказов" in main_page.driver.page_source

    @allure.title("Появление модального окна с ингредиентом")
    def test_ingredient_modal_appears(self, main_page):
        main_page.open_main_page()
        main_page.click_ingredient_card()
        assert "Детали ингредиента" in main_page.driver.page_source

    @allure.title("Закрытие модального окна")
    def test_close_modal(self, main_page):
        main_page.open_main_page()
        main_page.click_ingredient_card()
        main_page.close_modal()
        assert not main_page.driver.find_elements(*MainPageLocators.CLOSE_MODAL_BUTTON)

    @allure.title("Увеличение счетчика добавленного ингредиента")
    def test_add_ingredient_counter_increase(self, main_page):
        main_page.open_main_page()
        main_page.add_ingredient_to_cart()
        assert main_page.driver.find_element(*MainPageLocators.COUNTER_INCREASE).text.strip() == "2"

    @allure.title("Пользователь может разместить заказ")
    def test_user_can_place_order(self, main_page, user_data):
        main_page.open_login_page()
        main_page.login(user_data["email"], user_data["password"])
        main_page.add_ingredient_to_cart()
        main_page.click_orders_button()
        order_identifier = WebDriverWait(main_page.driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.WAIT_FOR_READINESS)).text
        assert order_identifier == "Дождитесь готовности на орбитальной станции"
