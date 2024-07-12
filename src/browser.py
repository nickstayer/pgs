from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options


class Browser:
    driver: webdriver = None

    def __init__(self, logger, secret):
        self.logger = logger
        self.login = secret[0]
        self.password = secret[1]

    def start(self):
        chrome_options = Options()
        chrome_options.add_argument('--log-level=3')
        chrome_options.add_argument('--disable-logging')
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        # chrome_options.add_argument('--headless')
        service = ChromeService(executable_path='chromedriver.exe')
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
