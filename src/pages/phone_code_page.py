from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By

phone_code_inputs_locator = (By.XPATH, '//input[@autocomplete="one-time-code"]')


class PhoneCodePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def __str__(self):
        return 'Госуслуги: Страница ввода кода из смс'

    @property
    def here(self):
        return self.wait_and_find(phone_code_inputs_locator)

    @property
    def phone_code_inputs(self):
        return self.find_all(phone_code_inputs_locator)

    def type_phone_code(self, phone_code):
        inputs = self.phone_code_inputs
        for i in range(len(inputs)):
            inputs[i].click()
            inputs[i].send_keys(phone_code[i])
