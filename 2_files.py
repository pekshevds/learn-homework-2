"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('referat.txt', mode='r', encoding='utf-8') as file:
        referat = file.read()
        length_of_string = len(referat)
        text_without_some_symbols = referat.replace('.', '').replace(',', '').\
            replace('!', '').replace(':', '').replace('«', '').replace('»', '').replace('\n', ' ')

        words_count = len(text_without_some_symbols.split(' '))
        referat2 = referat.replace('.', '!')
    
    print('Слова из текста:', text_without_some_symbols)
    print(f"Длинна строки: {length_of_string} символов. Количество слов: {words_count}")
    
    with open('referat2.txt', mode='w', encoding='utf-8') as file:
        file.write(referat2)

if __name__ == "__main__":
    main()
