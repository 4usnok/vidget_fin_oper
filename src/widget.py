from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number_card: str) -> str:
    """
    Функция маскирует номер карты, используя функционал:
    для счета функцию - get_mask_account
    для номера карты функцию - get_mask_card_number
    """
    if "Счет" in number_card:
        # Создадим новую переменную для "Счет"
        # В переменной, мы используем срез с отрицательным значением
        # Тем самым - пойдем с конца и минимизируем ошибки в дальнейшем
        part_words = number_card[:-20]
        result = get_mask_account(number_card)
        return f"{part_words}{result}"

    else:
        part_words = number_card[:-16]
        # Отрицательный срез, помог корректно вывести номер карты и само название
        # Так как срез, с положительным значением, не давал, создать условия для
        # Названия карты и выводил некорректные данные
        result = get_mask_card_number(number_card)
        return f"{part_words}{result}"


def get_date(number_card: str) -> str:
    """
    Функция возвращает строку с датой в формате "ДД.ММ.ГГГГ"
    """
    # Использовали срезы, чтобы поменять местами числа и
    # вывести дату в формате "ДД.ММ.ГГГГ"
    part_words_d = number_card[8:10]
    part_words_m = number_card[5:7]
    part_words_y = number_card[:4]
    result_date = f"{part_words_d}.{part_words_m}.{part_words_y}"
    return result_date
