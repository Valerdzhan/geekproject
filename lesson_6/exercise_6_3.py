"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    name = None
    surname = None
    position = None

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):
    _income = None

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position)
        self._income = dict({"wage": wage, "bonus": bonus})

    def get_full_name(self):
        """
        Методы получения полного имени сотрудника
        """
        print(f"Имя, фамилия: {self.name} {self.surname}")

    def get_total_income(self):
        """
        Методы получения дохода с учетом премии
        """
        print(f"Должность {self.position}, оклад: {sum(self._income.values())}")


person = Position('Valeriy', 'Ivanov', 'engineer', 50000, 10000)
person.get_full_name()
person.get_total_income()

person = Position('Valeriy1', 'Ivanov1', 'engineer1', 40000, 40000)
person.get_full_name()
person.get_total_income()
