"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_mass(self, mass=25, depth=1):
        """
            Метод определения для покрытия дороги асфальтом

            :param mass: масса для покрытия одного кв метра толщиной 1 см
            :param depth: толщина одного кв метра
            :return: результат деления a / b
            """
        return self._width * self._length * mass * depth


all_road = Road(20, 5000)
print(f"{all_road.get_mass(25, 5) / 1000} т")
