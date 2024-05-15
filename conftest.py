import pytest
import random
import string
import requests
from selenium import webdriver
from pages.profile_page import ProfilePage
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.base_page import BasePage

@pytest.fixture(scope="function", params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")  # Открываем браузер в полный размер
        driver = webdriver.Chrome(options=options)
    elif request.param == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--start-maximized")  # Открываем браузер в полный размер
        driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def generate_user():
    email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + "@mail.ru"
    password = ''.join(random.choices(string.ascii_lowercase, k=10))
    name = ''.join(random.choices(string.ascii_lowercase, k=10))
    return {"email": email, "password": password, "name": name}

@pytest.fixture(scope="function")
def register_user(generate_user):
    user_data = generate_user
    response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/register", json=user_data)
    assert response.status_code == 200
    return user_data

@pytest.fixture(scope="function")
def authorize_and_cleanup_user(register_user):
    user_data = register_user
    login_data = {"email": user_data["email"], "password": user_data["password"]}
    login_response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/login", json=login_data)
    assert login_response.status_code == 200
    access_token = login_response.json()["accessToken"]

    yield user_data

    delete_headers = {"Authorization": access_token}
    delete_response = requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user", headers=delete_headers)
    if delete_response.status_code != 202:
        print(f"Failed to delete user. Status code: {delete_response.status_code}, Response: {delete_response.text}")
    assert delete_response.status_code == 202

@pytest.fixture(scope="function")
def user_data(authorize_and_cleanup_user):
    return authorize_and_cleanup_user

@pytest.fixture(scope="function")
def main_page(driver):
    return MainPage(driver)

@pytest.fixture(scope="function")
def feed_page(driver):
    return FeedPage(driver)

@pytest.fixture(scope="function")
def base_page(driver):
    return BasePage(driver)

@pytest.fixture(scope="function")
def profile_page(driver):
    return ProfilePage(driver)

