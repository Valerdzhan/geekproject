"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Complex((self.x + other.x), (self.y + other.y))

    def __mul__(self, other):
        """
        (x1+iy1)(x2+iy2)=x1x2−y1y2+(x1y2+x2y1)i.
        """
        x1 = self.x
        y1 = self.y
        x2 = other.x
        y2 = other.y
        return Complex((x1*x2 - y1 * y2), (x1*y2+x2*y1))

    def __str__(self):
        return f"{self.x}{self.y if self.y < 0 else '+' + str(self.y)}i"


c1 = Complex(2, 3)
c2 = Complex(3, -1)
print(c1 + c2)
print(c1 * c2)