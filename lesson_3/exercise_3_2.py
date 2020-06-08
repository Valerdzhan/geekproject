"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""

def person_func(name, surname, birth, city, mail, phone):
    """

    :param name: Имя
    :param surname: Фамилия
    :param birth: год рождения
    :param city: город проживания
    :param mail: email
    :param phone: телефон
    :return: Выводит данные пользователя в одну строку
    """
    return print(f"Результат: {name} {surname}, {birth}, {city}, {mail}, {phone}")

s_name = input('Введите имя: ')
s_surname = input('Введите фамилию: ')
s_birth = input('Введите год рождения: ')
s_city = input('Введите город проживания: ')
s_email = input('Введите email: ')
s_phone = input('Введите телефон: ')

person_func(name=s_name, surname=s_surname, birth=s_birth, city=s_city, mail=s_email, phone=s_phone)
