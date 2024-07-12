import time

from src.pages.base_page import BasePage
from src.pages.stat_page import StatPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.consts import *

stay_button_locator = (By.XPATH, '//span[contains(text(),"Остаться")]')
input_search_locator = (By.XPATH, '//input[contains(@placeholder, "Номер")]')
statement_link_locator = (By.XPATH, '//*[contains(@class, "q-chip--clickable")]')
no_data_locator = (By.XPATH, '//*[contains(text(),"Нет данных")]')


class SearchPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def __str__(self):
        return 'ПГС: Страница "Поиск заявлений"'

    @property
    def here(self):
        return self.wait_and_find(input_search_locator)

    def get_statement_link(self, stat_id):
        locator = (By.XPATH, f'//*[contains(text(), "{stat_id}")]/parent::div')
        return self.wait_and_find(locator, WAIT_3)

    @property
    def input_search(self):
        return self.wait_and_find(input_search_locator, WAIT_3)

    def open_statement(self, statement_id):
        counter = 0

        while counter < WAIT_5:
            self.input_search.click()
            self.input_search.send_keys(Keys.CONTROL + "a")
            self.input_search.send_keys(Keys.DELETE)
            self.input_search.send_keys(statement_id)
            if self.input_search.get_attribute('value') == statement_id:
                break
            else:
                counter += 1
                time.sleep(1)

        if self.input_search.get_attribute('value') == statement_id:
            self.input_search.send_keys(Keys.RETURN)
            if self.wait_and_find(no_data_locator, WAIT_3):
                self.browser.logger.error(f'Не удалось получить данные. '
                                          f'Искал: {statement_id}.Ввод: {self.input_search.get_attribute('value')}')
                return None
            statement_link = self.get_statement_link(statement_id)
            if statement_link:
                statement_link.click()
                return StatPage(self.browser)
        else:
            self.browser.logger.error(f'Не удалось получить данные. '
                                      f'Искал: {statement_id}.Ввод: {self.input_search.get_attribute('value')}')
            return None

    def close_alert(self):
        stay_button = self.wait_and_find(stay_button_locator, WAIT_60)
        if stay_button:
            stay_button.click()
