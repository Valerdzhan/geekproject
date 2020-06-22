"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.


31 22
37 43
51 86

3   5    32
2   4    6
-1  64  -8

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.

"""


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        str_matrix = ""
        for i in self.matrix:
            for j in i:
                str_matrix += f"{str(j)} "
            str_matrix += "\n"

        return str_matrix

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return f"Вы пытаетесь сложить разноразрядные матрицы"
        result = []
        for i in range(0, len(self.matrix)):
            temp = []
            for j in range(0, len(self.matrix[i])):
                temp.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(temp)

        return Matrix(result)

matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[1, 2], [3, 4], [5, 6]])
print(matrix_1)
print(matrix_1 + matrix_2)
