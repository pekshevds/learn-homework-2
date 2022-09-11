import csv
"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    list_of_dicts = [
        {'name':'Mike', 'age': 21, 'job': 'Engineer'},
        {'name':'John', 'age': 33, 'job': 'Policeman'},
        {'name':'Alex', 'age': 53, 'job': 'Doctor'},
        {'name':'Mary', 'age': 19, 'job': 'Housewife'},
        {'name':'Alan', 'age': 45, 'job': 'Sailor'},
    ]

    with open('list_of_dicts.csv', mode='w', encoding='utf-8', newline='') as file:
        fieldnames = ['name', 'age', 'job']
        dict_writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
        dict_writer.writeheader()

        dict_writer.writerows(list_of_dicts)

        

if __name__ == "__main__":
    main()
