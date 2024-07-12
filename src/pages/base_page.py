from selenium.common import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from src.consts import *


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find(self, locator):
        try:
            return self.browser.driver.find_element(*locator)
        except NoSuchElementException:
            self.browser.logger.debug(f'Не нашел элемент: локатор с типом {locator[0]} и значением {locator[1]}')
            return None

    def find_all(self, locator):
        try:
            return self.browser.driver.find_elements(*locator)
        except NoSuchElementException:
            self.browser.logger.debug(f'Не нашел элементы: локатор с типом {locator[0]} и значением {locator[1]}')
            return None

    def wait_and_find(self, locator, wait_time: int = WAIT_1):
        try:
            wait = WebDriverWait(self.browser.driver, wait_time)
            wait.until(ec.visibility_of_element_located(locator))
            return self.find(locator)
        except TimeoutException:
            return None

    def safe_click(self, locator):
        element = None
        try:
            wait = WebDriverWait(self.browser.driver, WAIT_3)
            wait.until(ec.element_to_be_clickable(locator))
            element = self.find(locator)
            element.click()
        except ElementClickInterceptedException:
            self.browser.driver.execute_script("arguments[0].scrollIntoView();", element)
            self.browser.driver.execute_script("arguments[0].click();", element)
