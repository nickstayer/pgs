from src.pages.base_page import BasePage
from src.pages.phone_code_page import PhoneCodePage
from selenium.webdriver.common.by import By
from src.consts import *

input_login_locator = (By.XPATH, '//*[@id="login"]')
input_password_locator = (By.XPATH, '//*[@id="password"]')
button_enter_locator = (By.XPATH, '//button[contains(text(), "Войти")]')
message_incorrect_login_locator = (By.XPATH, '//div[contains(text(), "Введите логин")]')
message_incorrect_login_pass_locator = (By.XPATH, '//div[contains(text(), "Неверные логин или пароль")]')


class LoginGsPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def __str__(self):
        return 'Госуслуги: Страница авторизации'

    @property
    def here(self):
        return self.wait_and_find(input_password_locator)

    @property
    def input_login(self):
        return self.find(input_login_locator)

    def type_login(self, login):
        self.input_login.click()
        self.input_login.send_keys(login)

    @property
    def input_password(self):
        return self.find(input_password_locator)

    def type_password(self, password):
        self.input_password.click()
        self.input_password.send_keys(password)

    @property
    def button_enter(self):
        return self.find(button_enter_locator)

    def button_enter_click(self):
        self.button_enter.click()
        if self.incorrect_enter:
            raise 'Неверный логин или пароль'
        return PhoneCodePage(self.browser)

    @property
    def incorrect_enter(self):
        message_incorrect_login_pass = self.wait_and_find(message_incorrect_login_pass_locator, WAIT_3)
        message_incorrect_login = self.wait_and_find(message_incorrect_login_locator, WAIT_3)
        c1 = message_incorrect_login_pass is not None
        c2 = message_incorrect_login is not None
        return c1 or c2
