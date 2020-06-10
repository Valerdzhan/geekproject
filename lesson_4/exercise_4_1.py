"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами
"""

from sys import argv

script_name, hours, hourly_payment, premium = argv


def profit(_hours, _hourly_payment, _premium):
    return int(_hours) * float(_hourly_payment) + float(_premium)


print("Имя скрипта: ", script_name)
print(f"Заработная плата равна - {profit(hours, hourly_payment, premium)}")
