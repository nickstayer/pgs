import src.pages as pages
from src.consts import *


def get_search_page(browser):
    counter = 0
    while counter < WAIT_60:
        if pages.SearchPage(browser).here:
            search_page = pages.SearchPage(browser)
            browser.logger.info(f'{search_page}')
            return search_page

        elif pages.UnifiedEnterPage(browser).here:
            unified_enter_page = pages.UnifiedEnterPage(browser)
            browser.logger.info(f'{unified_enter_page}')
            unified_enter_page.check_checkbox()
            search_page = unified_enter_page.choose_button_click()
            return search_page

        elif pages.StatPage(browser).here:
            stat_page = pages.StatPage(browser)
            browser.logger.info(f'{stat_page}')
            stat_page.go_back_to_statements()
            return pages.SearchPage(browser)

        elif pages.LoginPage(browser).here:
            login_page = pages.LoginPage(browser)
            browser.logger.info(f'{login_page}')
            login_page.button_enter_click()

        elif pages.LoginGsPage(browser).here:
            login_gs_page = pages.LoginGsPage(browser)
            browser.logger.info(f'{login_gs_page}')
            if login_gs_page.input_login:
                login_gs_page.type_login(browser.login)
            login_gs_page.type_password(browser.password)
            login_gs_page.button_enter_click()

        elif pages.PhoneCodePage(browser).here:
            phone_code_page = pages.PhoneCodePage(browser)
            browser.logger.info(f'{phone_code_page}')
            phone_code = input('Введите код из смс: ')
            phone_code_page.type_phone_code(phone_code)

        # elif pages.ImgCodePage(browser).here:
        #     img_code_page = pages.ImgCodePage(browser)
        #     img_code_page.download_and_open_image()
        #     img_code = input(f'{img_code_page}. Введите код и нажмите Enter')
        #     img_code_page.type_img_code(img_code)
        #     img_code_page.button_click()

    raise 'Страница не определена'
