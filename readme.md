для решения проблемы "Опаньки" Out of memory, предлагается добавить опции:

	options.add_argument("--disable-dev-shm-usage")
	options.add_argument("--disable-blink-features=AutomationControlled")
	options.add_argument("--disable-gpu")
	options.add_argument("--disable-infobars")
	options.add_argument("--disable-extensions")

а также очщать куки перед в конце каждой итерации:

	browser.delete_all_cookies()