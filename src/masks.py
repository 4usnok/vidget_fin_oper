def get_mask_card_number(number_card: str) -> str:
    """
    Функция принимает на вход номер карты и выводит
    зашифрованную некоторую часть номера
    """
    # Создадим переменные, которые будут в себе содержать срезы
    # Созданные переменные, позволят замаскировать цифры
    part_1 = number_card[-16:-12]
    part_2 = number_card[-12:-10]
    masked_part = "*" * (len(number_card[-10:-4]))
    part_4 = number_card[-4:]
    # Объединим всё в одну переменную для удобства и упорядочивания
    join_number_card_num = f"{part_1}{part_2}{masked_part}{part_4}"
    # Используем синтаксический сахар, который позволит ставить пробелы
    # после каждого четвертого символа
    return " ".join([join_number_card_num[i: i + 4] for i in range(0, len(join_number_card_num), 4)])


def get_mask_account(number_card_2: str) -> str:
    """
    Функция принимает на вход номер карты и выводит
    последние 6 цифр, две из которых, зашифрованные
    """
    masked_part = len(number_card_2[-6:-4]) * "*"
    part_num = number_card_2[-4:]
    join_number_card = f"{masked_part}{part_num}"
    # С помощью метода join(), мы сможем избавить строку от лишних символов
    return "".join(join_number_card)
