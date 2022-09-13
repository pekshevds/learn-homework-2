"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""


def get_referat() -> str:
    """
    get file content
    """
    try:
        with open('referat.txt', mode='r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return ""


def clear_text(text: str) -> str:
    """
    clear text from some characters
    """
    for ch in ".,!:«»\n":
        if ch in text:
            text.replace('.', '')
    return text


def output(length_of_referat: int, words_count: int):
    print(f"Длинна строки: {length_of_referat} символов. \
        Количество слов: {words_count}")


def save_referat2(referat2: str):
    with open('referat2.txt', mode='w', encoding='utf-8') as file:
        file.write(referat2)


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    referat = get_referat()
    length_of_referat = len(referat)
    referat_without_some_symbols = clear_text(referat)
    words_count = len(referat_without_some_symbols.split(' '))
    referat2 = referat.replace('.', '!')
    output(length_of_referat, words_count)
    save_referat2(referat2)


if __name__ == "__main__":
    main()
