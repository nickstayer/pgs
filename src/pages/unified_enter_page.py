from src.pages.base_page import BasePage
from src.pages.search_page import SearchPage
from selenium.webdriver.common.by import By
from src.consts import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# check_box_locator = (By.XPATH, '//*[@class="q-checkbox__bg absolute"]')
check_box_locator = (
    By.XPATH,
    '//td[contains(text(), "ГЛАВНОЕ УПРАВЛЕНИЕ")]/preceding-sibling::td',
)
button_choose_locator = (
    By.XPATH,
    '//*[@class="q-focus-helper"]/following-sibling::span',
)


class UnifiedEnterPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def __str__(self):
        return "ПГС: Страница выбора подразделения"

    @property
    def here(self):
        return self.wait_and_find(check_box_locator)

    @property
    def checkbox(self):
        elements = self.find_all(check_box_locator)
        if len(elements) > 1:
            return elements[1]
        return elements[0]

    def check_checkbox(self):
        self.checkbox.click()

    @property
    def choose_button(self):
        return self.find(button_choose_locator)

    def choose_button_click(self):
        wait = WebDriverWait(self.browser.driver, 10)
        wait.until(ec.element_to_be_clickable(self.choose_button))
        self.choose_button.click()
        return SearchPage(self.browser)
