"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами
"""

from sys import argv

try:
    script_name, hours, hourly_payment, premium = argv


    def profit(_hours, _hourly_payment, _premium):
        try:
            return print(f"Заработная плата равна - {int(_hours) * float(_hourly_payment) + float(_premium)}")
        except ValueError:
            print('Введены неверные параметры')


    print("Имя скрипта: ", script_name)
    profit(hours, hourly_payment, premium)
except ValueError:
    print('Проверьте правильность введенных параметров')
