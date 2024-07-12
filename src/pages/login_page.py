from src.pages.base_page import BasePage
from src.pages.login_gs_page import LoginGsPage
from selenium.webdriver.common.by import By

input_login_locator = (By.XPATH, '//*[@name="login"]')
input_password_locator = (By.XPATH, '//*[@name="password"]')
button_enter_locator = (By.XPATH, '//form[contains(@action,"gosuslugi")]//button')


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def __str__(self):
        return 'Сервис ИСОД: Страница авторизации'

    @property
    def here(self):
        return self.wait_and_find(input_login_locator)

    @property
    def input_login(self):
        return self.find(input_login_locator)

    @property
    def input_password(self):
        return self.find(input_password_locator)

    def type_login(self, login):
        self.input_login.click()
        self.input_login.send_keys(login)

    def type_password(self, password):
        self.input_password.click()
        self.input_password.send_keys(password)

    @property
    def button_enter(self):
        return self.find(button_enter_locator)

    def button_enter_click(self):
        self.button_enter.click()
        return LoginGsPage(self.browser)
