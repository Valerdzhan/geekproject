"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.

"""

from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def how_cloth(self):
        pass


class Coat(Clothes):

    def __init__(self, V):
        self.V = V

    @property
    def V(self):
        return self.__V

    @V.setter
    def V(self, V):
        if V < 0:
            self.__V = 0
        else:
            self.__V = V

    def how_cloth(self):
        return f"Расхода ткани на одно пальто = %.2f" % float(self.V / 6.5 + 0.5)


class Suit(Clothes):

    def __init__(self, H):
        self.H = H

    @property
    def H(self):
        return self.__H

    @H.setter
    def H(self, H):
        if H < 0:
            self.__H = 0
        else:
            self.__H = H

    def how_cloth(self):
        return f"Расхода ткани на один костюм = %.2f" % float(2 * self.H + 0.3)


coat = Coat(1.76)
print(coat.how_cloth())

suit = Suit(1.76)
print(suit.how_cloth())