from datetime import datetime, timedelta, date, time
"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    one_day = timedelta(days=1)
    today = date.today()
    yesterday = today - one_day
    thirty_days_ago = today - (one_day * 30)

    print(f"Вчера: {yesterday}, сегодня: {today}, 30 дней назад: {thirty_days_ago}")
    

def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    return datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
