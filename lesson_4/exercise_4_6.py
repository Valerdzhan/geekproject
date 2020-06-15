"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""
from itertools import count, cycle


def func_a():
    while True:
        try:
            start = int(input("Введите начальное целое число: "))
            finish = int(input(f"Введите конечное число, больше {start}: "))

            if start > finish:
                print("Конечное число не должно быть меньше начального")
                continue

            for i in count(start):
                if i > finish:
                    break
                else:
                    print(i)
            break
        except ValueError:
            print('Введеные неправильные данные')
            continue


def func_b():
    while True:
        try:
            my_list = ["a", "b", "c", "d"]
            end = int(input('Сколько раз вывести список?: '))

            i = 0
            for el in cycle(my_list):
                if i >= end * len(my_list):
                    break
                print(el)
                i += 1

        except ValueError as error:
            print(f"{error}")
            continue

        # Завершение функции
        break


func_a()
func_b()
