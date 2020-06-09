"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    """
    Функция возвращает сумму наибольших двух аргументов.

    :param a:
    :param b:
    :param c:
    :return: сумму наибольших двух аргументов
    """
    my_list = [a, b, c]
    i = 0
    result = 0
    while i < 2:
        var_1 = max(my_list)
        my_list.pop(my_list.index(var_1))
        result += var_1
        i += 1

    return result


s_a = int(input('Введите число: '))
s_b = int(input('Введите число: '))
s_c = int(input('Введите число: '))

print(f"Результат: {my_func(s_a, s_b, s_c)}")
