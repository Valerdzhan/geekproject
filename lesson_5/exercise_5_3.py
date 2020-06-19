"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32

"""
import numbers
from functools import reduce


def sum_func(prev_el, el):
    return prev_el + el


try:
    with open("text_3.txt", "r", encoding="utf=8") as my_file:
        salary = 0
        users_less_20 = []
        users = my_file.readlines()
        len_lines = len(users)
        profit = []
        for u in users:
            user = u.split()
            for s in user:
                try:
                    if isinstance(float(s), float):
                        if float(s) < 20000.0:
                            users_less_20.append(user)
                        profit.append(float(s))
                except ValueError:
                    continue
        print(users_less_20)
        print(f"Средняя величина дохода сотрудников: {reduce(sum_func, profit)/len_lines}")
except IOError:
    print('Открытие файла невозможно! Проверьте наличие файла!')
