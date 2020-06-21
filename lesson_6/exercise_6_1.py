"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.  Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
завершать скрипт.
"""
from time import sleep

CRED2 = '\33[91m'
CGREEN2 = '\33[92m'
CYELLOW2 = '\33[93m'
CGREY = '\33[90m'

red = [CRED2, CGREY, CGREY]
yellow = [CGREY, CYELLOW2, CGREY]
green = [CGREY, CGREY, CGREEN2]

times = [5, 2, 7, 2]
colors = [red, yellow, green, yellow]


def select_color(color):
    for c in color:
        print(f"{c} ◉")
    print()


class TrafficLight:
    __color = ''

    def running(self):
        while True:
            for i in range(0, len(colors)):
                select_color(colors[i])
                sleep(times[i])


light = TrafficLight()
light.running()
