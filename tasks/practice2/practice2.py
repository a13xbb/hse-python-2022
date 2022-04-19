from typing import Iterable
from random import randint
from random import uniform

UNCULTURED_WORDS = ('kotleta', 'pirog')


def greet_user(name: str) -> str:
    """
    Генерирует приветственную фразу.
    Приветствие не может состоять только из одного имени пользователя.

    :param name: имя пользователя
    :return: приветствие
    """

    # пиши код здесь
    greetings = ['Привет, ', 'Здравствуй, ', 'Рад тебя видеть, ']
    hello_word = greetings[randint(0, 2)]
    greeting = f'{hello_word}{name}!'

    return greeting


def get_amount() -> float:
    """
    Генерируем случайную сумму на счете.

    Сумма:
    - в диапазоне от 100 до 1000000
    - float
    - не больше 2-х знаков после запятой

    :return: случайную сумму на счете
    """

    # пиши код здесь
    amount = float(f'{uniform(100, 1000000):.2f}')

    return amount


def is_phone_correct(phone_number: str) -> bool:
    """
    Функция проверяет, что номер телефона соответствует следующему формату:
    +7xxxxxxxxxx, где x - цифра от 0 до 9

    :param phone_number: предполагаемый номер телефона
    :return: буленовское значение - bool: True - если номер корректны,
                                          False - если номер некорректный
    """

    # пиши код здесь
    digits = [str(i) for i in range(10)]

    if phone_number.startswith('+7') and len(phone_number) == 12:
        for num in phone_number[2:]:
            if num not in digits:
                return False
    else:
        return False

    return True


def is_amount_correct(current_amount: float, transfer_amount: str) -> bool:
    """
    Проверяет возможность осуществления перевода.
    Перевод возможен если выполняется условие:
    - текущий счет (current_amount) больше или равен сумме перевода (transfer_amount)

    :param current_amount: текущий счет
    :param transfer_amount: сумма перевода
    :return: буленовское значение - bool: True - если перевод возможен,
                                          False - если денег недостаточно
    """

    # пиши код здесь
    if current_amount >= float(transfer_amount):
        return True
    else:
        return False


def moderate_text(text: str, uncultured_words: Iterable[str]) -> str:
    """
    Модерирует текст по следующим правилам.

    Требования к тексту:
    - Первая буква заглавная, остальные буквы только в нижнем регистре
    - отсутствую лишние пробелы
    - фильтруются 'опасные' символы: " ' (двойные и одинарные кавычки)
    - слова, перечисленные в переменной uncultured_words заменяются на аналогичное количество знаков #

    :param text: исходный текст
    :param uncultured_words: список запрещенных слов
    :return: текст, соответсвующий правилам
    """

    # пиши код здесь
    words = text.split(' ')

    while '' in words:
        words.remove('')

    resctricted_symbols = ['"', '\'']

    if len(words) != 0:
        for i, word in enumerate(words):
            words[i] = word.lower()
            for resctricted_symbol in resctricted_symbols:
                while resctricted_symbol in words[i]:
                    index = words[i].find(resctricted_symbol)
                    words[i] = words[i][:index] + words[i][index+1:]

        #     if word in uncultured_words:
        #         words[i] = ''.join(['#' for j in range(len(word))])
        words[0] = words[0][0].upper() + words[0][1:]

    result = ' '.join(words)
    for uncultured_word in uncultured_words:
        while uncultured_word in result:
            index = result.find(uncultured_word)
            result = result[:index] + ''.join(['#' for j in range(len(uncultured_word))]) + result[index + len(uncultured_word):]

    return result


def create_request_for_loan(user_info: str) -> str:
    """
    Генерирует заявку на кредит на основе входящей строки.
    Формат входящий строки:

    Иванов,Петр,Сергеевич,01.01.1991,10000

    Что должны вернуть на ее основе:

    Фамилия: Иванов
    Имя: Петр
    Отчество: Сергеевич
    Дата рождения: 01.01.1991
    Запрошенная сумма: 10000

    :param user_info: строка с информацией о клиенте
    :return: текст кредитной заявки
    """

    # пиши код здесь
    user_info = user_info.split(',')
    strings = ['Фамилия: ', 'Имя: ', 'Отчество: ', 'Дата рождения: ', 'Запрошенная сумма: ']
    result = ''
    for i in range(len(strings)):
        result += strings[i] + user_info[i] + '\n'
    result = result[:-1]
    return result
