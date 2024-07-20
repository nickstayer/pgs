from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium.webdriver.firefox.options import Options as OptionsFirefox


class Browser:
    driver: webdriver = None

    def __init__(self, logger, secret):
        self.logger = logger
        self.login = secret[0]
        self.password = secret[1]

    def start_chrome(self):
        chrome_options = OptionsChrome()
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument('--log-level=3')
        chrome_options.add_argument('--disable-logging')
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        # chrome_options.add_argument('--headless')
        service_chrome = ChromeService(executable_path='chromedriver.exe')
        self.driver = webdriver.Chrome(service=service_chrome, options=chrome_options)

    def start_firefox(self):
        ff_options = OptionsFirefox()
        ff_options.add_argument("--disable-dev-shm-usage")
        ff_options.add_argument("--disable-blink-features=AutomationControlled")
        ff_options.add_argument("--disable-gpu")
        ff_options.add_argument("--disable-infobars")
        ff_options.add_argument("--disable-extensions")
        ff_options.add_argument('--log-level=3')
        ff_options.add_argument('--disable-logging')
        ff_options.add_argument('--disable-notifications')
        ff_options.add_argument('--disable-dev-shm-usage')
        ff_options.add_argument('--disable-blink-features=AutomationControlled')
        ff_options.add_argument('--headless')
        service_ff = FirefoxService(executable_path='geckodriver.exe')
        self.driver = webdriver.Firefox(service=service_ff, options=ff_options)
