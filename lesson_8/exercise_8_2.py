"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и
не завершиться с ошибкой.
"""

class ZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt

inp_dec = input("Введите делимое: ")
inp_data = input("Введите делитель: ")

try:
    inp_data = int(inp_data)
    inp_dec = int(inp_dec)
    if inp_data == 0:
        raise ZeroError("На ноль делить нельзя")
except ValueError:
    print("Вы ввели не число")
except ZeroError as err:
    print(err)
else:
    print(f"результат {inp_dec}/{inp_data} = {int(inp_dec)/int(inp_data)}")
