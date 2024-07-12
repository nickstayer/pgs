from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By

page_marker_locator = (By.XPATH, '//*[contains(text(), "Введите код с картинки")]')


class ImgCodePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def __str__(self):
        return 'Госуслуги: Страница введения кода с картинки'

    @property
    def here(self):
        return self.wait_and_find(page_marker_locator)
