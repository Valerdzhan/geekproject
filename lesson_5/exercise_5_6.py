"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                     Физика:   30(л)   —   10(лаб)
                     Физкультура:   —   30(пр)   —

Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
import operator
import re


def gen_dict(data):
    data_split = data.split()
    key_name = data_split[0]
    list_number = []
    for el in data_split:
        try:
            if re.search(r'\d+', el):
                num = int(re.search(r'\d+', el).group())
                list_number.append(num)
        except ValueError:
            pass
    return dict({key_name: sum(list_number)})


try:
    with open("text_6.txt", "r", encoding="utf-8") as my_file:
        lines = my_file.readlines()
        d = dict()
        for line in lines:
            d.update(gen_dict(line))

        print(d)
except IOError:
    print("Error!!!")
