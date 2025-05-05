from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from src.consts import *
from src.statement import Statement

back_locator = (By.XPATH, '//i[contains(@class,"pgs-icon pgs-arrow-left")]')
stat_id_locator = (By.XPATH, '//span[contains(text(),"Заявление")]')
first_tab_locator = (By.XPATH, '//div[contains(text(),"Общая информация")]')
target_locator = (
    By.XPATH,
    '//div[contains(text(), "Что хотите вернуть?")]/following-sibling::div/span',
)
status_locator = (
    By.XPATH,
    '//div[contains(text(), "Статус заявления на ЕПГУ")]/following-sibling::div/span',
)
date_in_locator = (
    By.XPATH,
    '//div[contains(text(), "Дата подачи")]/following-sibling::div',
)
date_out_max_locator = (
    By.XPATH,
    '//div[contains(text(), "Максимальный срок предоставления")]/following-sibling::div',
)
fullname_locator = (
    By.XPATH,
    '//div[@class="form-generator-field" and (not(@style) or @style="")]//div[contains(text(),"Полное наименование")]/following-sibling::div',
)
birth_date_locator = (
    By.XPATH,
    '//div[@class="form-generator-field" and (not(@style) or @style="")]//div[contains(text(), "Дата рождения")]/following-sibling::div',
)

pay_id_locator = (
    By.XPATH,
    '//div[@class="form-generator-field" and (not(@style) or @style="")]//div[contains(text(), "Идентификатор платежа")]/following-sibling::div/child::div',
)
pay_uin_locator = (
    By.XPATH,
    '//div[@class="form-generator-field" and (not(@style) or @style="")]//div[contains(text(), "УИН")]/following-sibling::div/child::div',
)
pay_sum_locator = (
    By.XPATH,
    '//div[@class="form-generator-field" and (not(@style) or @style="")]//div[contains(text(), "Сумма возврата")]/following-sibling::div/child::div',
)
reason_locator = (
    By.XPATH,
    '//div[@class="form-generator-field" and (not(@style) or @style="")]//div[contains(text(), "Причина возврата")]/following-sibling::div/child::div',
)
situation_locator = (
    By.XPATH,
    '//div[@class="form-generator-field" and (not(@style) or @style="")]//div[contains(text(), "Обстоятельства")]/following-sibling::div/child::div',
)


class StatPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def __str__(self):
        stat_id_elem = self.wait_and_find(stat_id_locator, 3)
        stat_id = stat_id_elem.text if stat_id_elem else "None"
        return f"Страница {stat_id}"

    @property
    def here(self):
        return self.wait_and_find(stat_id_locator)

    @property
    def back_arrow(self):
        return self.find(back_locator)

    def go_back_to_statements(self):
        self.back_arrow.click()

    def get_statement(self):
        wait = WebDriverWait(self.browser.driver, 10)
        wait.until(ec.visibility_of_element_located(fullname_locator))
        self.first_tab.click()
        stat_id = self.stat_id.text.replace("Заявление ", "") if self.stat_id else ""
        target = self.target.get_attribute("textContent") if self.target else ""
        status = self.status.text if self.status else ""
        date_in = self.date_in.text if self.date_in else ""
        date_out_max = self.date_out_max.text if self.date_out_max else ""
        fullname = self.fullname.get_attribute("textContent") if self.fullname else ""
        birth_date = (
            self.birth_date.get_attribute("textContent") if self.birth_date else ""
        )
        # использую get_attribute('textContent') потому что родитель display: none
        # чтобы не переходить на вкладку Данные
        pay_id_text = self.pay_id.get_attribute("textContent") if self.pay_id else ""
        pay_uin_text = self.pay_uin.get_attribute("textContent") if self.pay_uin else ""
        pay_id = pay_uin_text if pay_id_text == "" else pay_id_text

        pay_sum = self.pay_sum.get_attribute("textContent") if self.pay_sum else ""

        reason_text = self.reason.get_attribute("textContent") if self.reason else ""
        situation_text = (
            self.situation.get_attribute("textContent") if self.situation else ""
        )
        reason = situation_text if reason_text == "" else reason_text

        return Statement(
            stat_id,
            target,
            status,
            date_in,
            date_out_max,
            fullname,
            birth_date,
            pay_id,
            pay_sum,
            reason,
        )

    @property
    def stat_id(self):
        return self.find(stat_id_locator)

    @property
    def target(self):
        return self.find(target_locator)

    @property
    def status(self):
        return self.find(status_locator)

    @property
    def date_in(self):
        return self.find(date_in_locator)

    @property
    def date_out_max(self):
        return self.find(date_out_max_locator)

    @property
    def fullname(self):
        return self.find(fullname_locator)

    @property
    def birth_date(self):
        return self.find(birth_date_locator)

    @property
    def pay_id(self):
        return self.find(pay_id_locator)

    @property
    def pay_uin(self):
        return self.find(pay_uin_locator)

    @property
    def pay_sum(self):
        return self.find(pay_sum_locator)

    @property
    def reason(self):
        return self.find(reason_locator)

    @property
    def situation(self):
        return self.find(situation_locator)

    @property
    def first_tab(self):
        return self.find(first_tab_locator)
