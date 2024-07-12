import traceback
from src.logger import Logger
from src.main import main

logger = Logger('run')

if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        logger.critical(f'run: Возникло исключение: {ex}')
        tb = traceback.format_exc()
        logger.critical(tb)
        input('Для выхода нажмите любую клавишу')
