import traceback
from src.authentication import get_search_page
from src.statement import *
from src.browser import Browser
from src.logger import Logger

file_in = "statements_list.csv"
file_out = "result.csv"
logger = Logger('main')
login = input('Логин: ').strip()
password = input('Пароль: ').strip()
secret = (login, password)
browser = Browser(logger, secret)


def main():
    logger.info(f'Подготавливаю файл {file_out}')
    write_headers(file_out)
    logger.info(f'Подготавливаю файл {file_in}')
    statement_id_list = read_stat_id(file_in)
    logger.info(f'Запускаю браузер')
    browser.start()
    logger.info(f'Подключаюсь к {START_PAGE}')
    browser.driver.get(START_PAGE)
    search_page = get_search_page(browser)
    logger.info('Ожидаю окно с предложением перейти на новый интерфейс')
    search_page.close_alert()
    logger.info('Начинаю работу со списком заявлений')

    for statement_id in statement_id_list:
        if is_null_or_empty(statement_id):
            continue
        logger.info(f'Работаю с ид: {statement_id}')
        stat_page = search_page.open_statement(statement_id)
        if stat_page:
            logger.info(stat_page)
            statement = stat_page.get_statement()
            logger.info(f'Информация получена')
            statement.write_body(file_out)
            logger.info(f'Информация записана в файл')
            stat_page.go_back_to_statements()
        search_page = get_search_page(browser)

    logger.info(f'Получены данные заявлений в количестве: {len(statement_id_list)}')
    input(f'Работа программы завершена.\r\n'
          f'Результат в файле {file_out}.\r\n'
          f'Для выхода нажмите любую клавишу')
    if browser.driver:
        browser.driver.quit()
        browser.logger.debug('Браузер закрыт')


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        if browser.driver:
            browser.driver.quit()
            browser.logger.debug('Браузер закрыт')
        logger.critical(f'main: Возникло исключение: {ex}')
        tb = traceback.format_exc()
        logger.critical(tb)
