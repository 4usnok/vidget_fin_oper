import logging


logger = logging.getLogger('masks.py')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('D:\\Projects_from_skypro\\PythonProject_1\\logs\\masks.log', mode='w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(number_card: str) -> str:
    """
    Функция маскирует некоторую часть номера карты
    """
    try:
        logger.info(f'Выполняем запрос с ключевыми словами:')
        part_1 = number_card[-16:-12]
        part_2 = number_card[-12:-10]
        masked_part = "*" * (len(number_card[-10:-4]))
        part_4 = number_card[-4:]
        # Объединим всё в одну переменную для удобства и упорядочивания
        join_number_card_num = f"{part_1}{part_2}{masked_part}{part_4}"
        # Используем синтаксический сахар, который позволит ставить пробелы
        # после каждого четвертого символа
    except Exception as ex:
        logging.error(f'Произошла ошибка: {ex}')
    return " ".join([join_number_card_num[i: i + 4] for i in range(0, len(join_number_card_num), 4)])


def get_mask_account(number_card_2: str) -> str:
    """
    Функция выводит последние 6 цифр, две из которых замаскированы
    """
    try:
        logger.info(f'Выполняем запрос с ключевыми словами:')
        masked_part = len(number_card_2[-6:-4]) * "*"
        part_num = number_card_2[-4:]
        join_number_card = f"{masked_part}{part_num}"
    except Exception as ex:
        logging.error(f'Произошла ошибка: {ex}')
    # С помощью метода join(), мы сможем избавить строку от лишних символов
    return "".join(join_number_card)
