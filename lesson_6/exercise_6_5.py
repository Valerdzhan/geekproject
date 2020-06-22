"""
Реализовать класс Stationery (канцелярская принадлежность).
 Определить в нем атрибут title (название) и метод draw (отрисовка).
 Метод выводит сообщение “Запуск отрисовки.”
 Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
 В каждом из классов реализовать переопределение метода draw.
 Для каждого из классов метод должен выводить уникальное сообщение.
 Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

"""


class Stationery:
    title = 'Канцелярская принадлежность'

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def __init__(self):
        self.title = 'Ручка'

    def draw(self):
        print('Рисуем ручкой')


class Pencil(Stationery):
    def __init__(self):
        self.title = 'Карандаш'

    def draw(self):
        print('Рисуем карандашем')


class Handle(Stationery):
    def __init__(self):
        self.title = 'Маркер'

    def draw(self):
        print('Рисуем маркером')


pen_object = Pen()
pen_object.draw()

pencil_object = Pencil()
pen_object.draw()

handler_object = Handle()
handler_object.draw()
