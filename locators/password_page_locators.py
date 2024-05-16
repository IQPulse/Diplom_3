from selenium.webdriver.common.by import By

class PasswordPageLocators:
    RESET_BUTTON = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")  # Ссылка "Восстановить пароль"
    EMAIL_FIELD = (By.XPATH, "//label[normalize-space()='Email']/following-sibling::input")  # Поле "Email"
    RESET_BUTTON_EMAIL = (By.XPATH, "//button[contains(text(),'Восстановить')]")  # Кнопка "Восстановить"
    NEW_PASSWORD_FIELD = (By.XPATH, "//input[@name='Введите новый пароль']")  # Поле "Введите новый пароль"
    SHOW_HIDE_PASSWORD_BUTTON = (By.XPATH, "//button[contains(text(),'Показать/скрыть пароль')]")  # Кнопка "Показать/скрыть пароль"
    CLICK_SHOW_HIDE_PASSWORD_BUTTON = (By.XPATH, "//div[@class='input__icon input__icon-action']//*[name()='svg']")  # Кнопка "Показать/скрыть пароль" после клика
    PASSWORD_RECOVERY_BUTTON = (By.XPATH, "//h2[contains(text(),'Восстановление пароля')]")  # Текст "Восстановление пароля"
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")  # Поле "Email" Вход
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")  # Поле "Пароль" Вход
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")  # Кнопка "Войти" Вход
