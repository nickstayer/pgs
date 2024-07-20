import traceback
from src.authentication import get_search_page
from src.statement import *
from src.browser import Browser
from src.logger import Logger
import gc
from src.pages.img_code_page import ImgCodePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import requests
from PIL import Image
from io import BytesIO


def download_and_open_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        img.show()
    else:
        print("Failed to retrieve the image. Status code:", response.status_code)


logger = Logger('test')
login = ''
password = ''
secret = (login, password)
browser = Browser(logger, secret)
try:
    browser.start_firefox()
    browser.driver.get(TEST_PAGE)
    img_element = browser.driver.find_element(By.XPATH, '//img[@alt="Google"]')
    img_url = img_element.get_attribute('src')
    download_and_open_image(img_url)
except Exception as ex:
    print(ex)
finally:
    input(f'Работа программы завершена.\r\n'
          f'Для выхода нажмите любую клавишу')
    if browser.driver:
        browser.driver.quit()
        browser.logger.debug('Браузер закрыт')
