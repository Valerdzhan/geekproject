"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from random import randint
from functools import reduce


def sum_func(prev_el, el):
    if isinstance(int(prev_el), int) and isinstance(int(el), int):
        return int(prev_el) + int(el)


numbers = ""
for i in range(0, 100):
    numbers += f"{randint(0, 100)} "

with open("result_ex_5.txt", 'w', encoding="utf-8") as res_file:
    res_file.write(numbers)

with open("result_ex_5.txt", 'r', encoding="utf-8") as res_file:
    num = res_file.read()
    print(reduce(sum_func, num.split()))
