import logging
from pytest import mark

'''
Создаём базовый конфиг нашего логгера с указанием:
    1) Путь где он будет находится ( в данном варианте - в корне )
    2) Формат вывода сообщения ( Время  УровеньУведомления ТелоУведомления )
    3) Формат вывода времени в сообщениях логгера
    4) Указываем что нам интересны все выводы, начиная с debug. Без указания, выводит только : warning , error , critical
Создаём обьект нашего логера.
Выводим сообщения в фукнции
'''

logging.basicConfig(filename="test.log",
                    format="%(asctime)s: %(levelname)s: %(message)s",
                    datefmt="%d/%m/%Y %I:%M:%S",
                    level=logging.DEBUG)

# создаём объект логгера для работы 

logger = logging.getLogger()
logger.setLevel(logging.DEBUG) 

def test_log():
    logger.debug("This is debug message")
    logger.info("This is info message")
    logger.warning("This is warning message")
    logger.error("This is error message")
    logger.critical("This is critical message")



