from datetime import datetime
import logging
from logging.handlers import RotatingFileHandler


class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        log_file = datetime.now().strftime("log_%Y_%m_%d") + '.log'
        # log_file = 'log.log'
        file_handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=2)
        file_handler.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.ERROR)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def debug(self, message: str):
        self.logger.debug(message)

    def info(self, message: str):
        self.logger.info(message)
        print(message)

    def warning(self, message: str):
        self.logger.warning(message)
        print(message)

    def error(self, message: str):
        self.logger.error(message)
        print(message)

    def critical(self, message: str):
        self.logger.critical(message)
        print(message)

# Пример использования класса Logger
# if __name__ == "__main__":
#     logger = Logger('MyLogger', 'my_log.log')
#     logger.debug('Это сообщение для отладки')
#     logger.info('Это информационное сообщение')
#     logger.warning('Это предупреждение')
#     logger.error('Это сообщение об ошибке')
#     logger.critical('Это критическое сообщение')
