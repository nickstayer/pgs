from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import requests
from PIL import Image
from io import BytesIO

page_marker_locator = (By.XPATH, '//*[contains(text(), "Введите код с картинки")]')
img_locator = (By.XPATH, '//img')
input_locator = (By.XPATH, '//input')
button_locator = (By.XPATH, '//button[contains(text(), "Продолжить")]')


class ImgCodePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def __str__(self):
        return 'Госуслуги: Страница введения кода с картинки'

    @property
    def here(self):
        return self.wait_and_find(page_marker_locator)

    @property
    def img(self):
        return self.find(img_locator)

    @property
    def input(self):
        return self.find(input_locator)

    @property
    def get_img_url(self):
        return self.img.get_attribute('src')

    def download_and_open_image(self):
        url = self.get_img_url()
        response = requests.get(url)
        if response.status_code == 200:
            img_data = response.content
            img = Image.open(BytesIO(img_data))
            img.show()
        else:
            self.browser.logger("Failed to retrieve the image. Status code:", response.status_code)

    @property
    def button(self):
        return self.wait_and_find(button_locator)

    def button_click(self):
        wait = WebDriverWait(self.browser.driver, 3)
        wait.until_not(ec.text_to_be_present_in_element_attribute(button_locator, 'class', '_disabled'))
        self.button.click()

    def type_img_code(self, img_code):
        self.input.click()
        self.input.send_keys(img_code)
