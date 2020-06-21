"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.

Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.

"""

from random import randrange


class Car:
    speed = 0
    color = 'white'
    name = 'hyundai'
    is_police = False

    def go(self):
        self.speed = 10
        print("Поехали!!!")

    def stop(self):
        self.speed = 0
        print("Стоп")

    def turn(self):

        direction = ['налево', 'направо']
        print(f'Поворачиваем {direction[randrange(0, 2)]}')

    def show_speed(self):
        if (self.speed > 0):
            self.speed = randrange(30, 80)
            print(f"Текущая скорость {self.speed}")
        else:
            print("Для начала надо тронуться с места")


class TownCar(Car):

    def __init__(self, color, name):
        self.color = color
        self.name = name
        print(f"TownCar  {name} {color} 🚙")

    def show_speed(self):
        if (self.speed > 0):
            self.speed = randrange(30, 80)
            print(f"Текущая скорость {self.speed}")
            if self.speed > 60:
                print('Вы превысили допустимую скорость!')
        else:
            print("Для начала надо тронуться с места")


class SportCar(Car):
    def __init__(self, color, name):
        self.color = color
        self.name = name
        print(f"SportCar {name} {color} 🚗")


class WorkCar(Car):
    def __init__(self, color, name):
        self.color = color
        self.name = name
        print(f"WorkCar {name} {color} 🚌")

    def show_speed(self):
        if (self.speed > 0):
            self.speed = randrange(30, 80)
            print(f"Текущая скорость {self.speed}")
            if self.speed > 40:
                print('Вы превысили допустимую скорость!')
        else:
            print("Для начала надо тронуться с места")


class PoliceCar(Car):
    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.is_police = True
        print(f"PoliceCar {name} {color} 🚓")


town_car = TownCar('Lexus', 'White')
print(f"Скорость {town_car.speed}")
print(f"Полиция? {'ага' if town_car.is_police == True else 'неа'}")
town_car.go()
town_car.show_speed()
town_car.stop()
town_car.show_speed()

sport_car = SportCar('Lexus', 'White')
print(f"Скорость {sport_car.speed}")
print(f"Полиция? {'ага' if sport_car.is_police == True else 'неа'}")
sport_car.go()
sport_car.show_speed()
sport_car.stop()
sport_car.show_speed()

work_car = WorkCar('Lexus', 'White')
print(f"Скорость {work_car.speed}")
print(f"Полиция? {'ага' if work_car.is_police == True else 'неа'}")
work_car.go()
work_car.show_speed()
work_car.turn()
work_car.show_speed()

police_car = PoliceCar('Lexus', 'White')
print(f"Скорость {police_car.speed}")
print(f"Полиция? {'ага' if police_car.is_police == True else 'неа'}")
police_car.go()
police_car.show_speed()
police_car.turn()
police_car.show_speed()
police_car.stop()
