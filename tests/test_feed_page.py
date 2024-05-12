import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.history_page_locators import HistoryPageLocators

@allure.feature("Тесты страницы заказов")
class TestFeedPage:

    @allure.story("Отображение всплывающего окна с деталями заказа")
    def test_order_details_popup_appears(self, feed_page, main_page, base_page, user_data):
        base_page.open_login_page()
        base_page.login(user_data["email"], user_data["password"])
        main_page.add_ingredient_to_cart()
        main_page.click_orders_button()
        feed_page.close_order_window()
        main_page.click_orders_feed_button()
        feed_page.click_component_container()
        WebDriverWait(feed_page.driver, 10).until(
            EC.visibility_of_element_located((HistoryPageLocators.POPUP_WINDOW)))
        popup_element = feed_page.driver.find_element(*HistoryPageLocators.POPUP_WINDOW)
        assert "В обработке" in popup_element.text or "Выполнен" in popup_element.text

    @allure.story("Пользователь может разместить заказ и найти его в ленте")
    def test_user_can_place_order_and_search_in_feed(self, feed_page, main_page, base_page, user_data):
        base_page.open_login_page()
        base_page.login(user_data["email"], user_data["password"])
        main_page.add_ingredient_to_cart()
        main_page.click_orders_button()
        feed_page.close_order_window()
        feed_page.open_profile()
        feed_page.open_order_history()
        feed_page.open_order_history_blank()
        order_number = feed_page.copy_order_number_in_order_history()
        feed_page.go_back()
        main_page.click_orders_feed_button()
        searched_order_number = feed_page.search_order_in_feed_page()
        assert order_number == searched_order_number

    @allure.story("Счетчик увеличивается при создании нового заказа")
    def test_counter_increases_when_new_order_created(self, feed_page, main_page, base_page, user_data):
        base_page.open_login_page()
        base_page.login(user_data["email"], user_data["password"])
        main_page.click_orders_feed_button()
        initial_order_number = feed_page.find_and_save_element_counter_increases()
        base_page.open_main_page()
        main_page.add_ingredient_to_cart()
        main_page.click_orders_button()
        feed_page.close_order_window()
        main_page.click_orders_feed_button()
        new_order_number = feed_page.find_and_save_element_counter_increases()
        assert new_order_number == initial_order_number + 1

    @allure.story("Счетчик увеличивается за сегодня при создании нового заказа")
    def test_counter_increases_today_when_new_order_created(self, feed_page, main_page, base_page, user_data):
        base_page.open_login_page()
        base_page.login(user_data["email"], user_data["password"])
        main_page.click_orders_feed_button()
        initial_order_number_today = feed_page.find_and_save_element_counter_increases_today()
        base_page.open_main_page()
        main_page.add_ingredient_to_cart()
        main_page.click_orders_button()
        feed_page.close_order_window()
        main_page.click_orders_feed_button()
        new_order_number_today = feed_page.find_and_save_element_counter_increases_today()
        assert new_order_number_today == initial_order_number_today + 1

    @allure.story("Номер заказа появляется в разделе 'В процессе' после размещения заказа")
    def test_order_number_appears_in_progress_section_after_order_placement(self, feed_page, main_page, base_page, user_data):
        base_page.open_login_page()
        base_page.login(user_data["email"], user_data["password"])
        main_page.add_ingredient_to_cart()
        main_page.click_orders_button()
        main_page_order_number = feed_page.find_and_save_element_order_number_appears()
        feed_page.close_order_window()
        main_page.click_orders_feed_button()
        feed_page_order_number = feed_page.find_and_save_element_order_number_appears_feed()
        assert main_page_order_number == feed_page_order_number
