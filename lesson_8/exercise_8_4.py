"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.

Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.

"""
stocks = []
product_types = {'printer': 'Принтер', 'scanner': 'Сканер', 'xerox': 'Ксерокс'}


class Stock:
    """
    products = { printer: [
                            { id: 1, firm: 'samsung', note: 'Описание', is_color: True, is_laser: True}
                            { id: 2, firm: 'lg', note: 'Описание 2', is_color: false, is_laser: False}
                         ],
                scanner: [
                            { id: 3, firm: 'samsung', note: 'Описание', type_scan: 'ручной'}
                            { id: 4, firm: 'lg', note: 'Описание 2', type_scan: 'листовой'}
                          ],
                xerox: [
                            { id: 5, firm: 'samsung', note: 'Описание', is_color: True, scan_speed: 10}
                            { id: 6, firm: 'lg', note: 'Описание 2', is_color: False, scan_speed: 15}
                          ]
    """

    def __init__(self, name):
        self.products = dict()
        self.name = name

    def set_item(self, product_type, product):
        unit = self.products.get(product_type)
        if unit:
            self.__update_products(unit, product_type, product)
        else:
            self.__add_products(product_type, product)

    def __add_products(self, product_type, product):
        self.__products_save(product_type, [product])
        print('Продукт добавлен!')

    def __update_products(self, unit, product_type, product):
        unit.append(product)
        self.__products_save(product_type, unit)
        print('Продукт добавлен!')

    def __products_save(self, product_type, unit):
        self.products.update({product_type: unit})

    def get_item(self, product_type):
        unit = self.products.get(product_type)
        if unit and len(unit) > 0:
            item = unit.pop()
            print(f'Продукт: {item} выдан')
            self.__products_save(product_type, unit)
            return item
        else:
            print('Продукт закончился!')

    def __str__(self):
        result = f"{self.name} \n"
        if len(self.products) == 0:
            result += 'Склад пуст!'
        else:
            for key, value in self.products.items():
                result += f"{product_types[key]}, кол-во: {len(value)} \n"
                for item in value:
                    result += f"    {item} \n"
        return result


class OfficeEquipment:
    ID = 0

    def __init__(self, firm, note):
        OfficeEquipment.ID += 1
        self.firm = firm
        self.note = note


class Printer(OfficeEquipment):

    def __init__(self, firm, note, is_color, is_laser):
        super().__init__(firm, note)
        self.id = self.ID
        self.is_color = is_color
        self.is_laser = is_laser

    @staticmethod
    def add():
        firm = input('Введите название фирмы производителя: ')
        note = input('Введите описание: ')
        is_color = input('1 - Цветной/0 - ЧБ: ')
        is_laser = input('1 - Лазерный/0 - Струйный: ')
        return Printer(firm, note, True if is_color == '1' else False, True if is_laser == '1' else False)


    def __str__(self):
        return f"id: {self.id}, firm: {self.firm}, note: {self.note}, is_color: {self.is_color}, is_laser: {self.is_laser}"


class Scaner(OfficeEquipment):

    def __init__(self, firm, note, type_scan):
        super().__init__(firm, note)
        self.id = self.ID
        self.type_scan = type_scan

    @staticmethod
    def add():
        firm = input('Введите название фирмы производителя: ')
        note = input('Введите описание: ')
        type_scan = input('Введите тип сканера: ')
        return Scaner(firm, note, type_scan)

    def __str__(self):
        return f"id: {self.id}, firm: {self.firm}, note: {self.note}, type_scan: {self.type_scan}"


class Xerox(OfficeEquipment):

    def __init__(self, firm, note, is_color, scan_speed):
        super().__init__(firm, note)
        self.id = self.ID
        self.is_color = is_color
        self.scan_speed = scan_speed

    @staticmethod
    def add():
        firm = input('Введите название фирмы производителя: ')
        note = input('Введите описание: ')
        is_color = input('1 - Цветной/0 - ЧБ: ')
        scan_speed = input('Скорость сканирования лист/мин ')
        return Printer(firm, note, True if is_color == '1' else False, scan_speed)

    def __str__(self):
        return f"id: {self.id}, firm: {self.firm}, note: {self.note}, is_color: {self.is_color}, scan_speed: {self.scan_speed}"


storage = Stock('Склад № 1')
storage_2 = Stock('Склад № 2')
stocks.append(storage)
stocks.append(storage_2)

printer_1 = Printer('lg', 'notes', True, True)
scan_1 = Scaner('Samsung', 'описание', 'ручной')
xerox_1 = Xerox('Xerox', 'описание', True, 100)

printer_2 = Printer('Samsung', 'notes', True, False)
storage.set_item('printer', printer_1)
storage.set_item('printer', printer_2)
storage.set_item('scanner', scan_1)
storage.set_item('xerox', xerox_1)
t = storage.get_item('printer')

print('Добро пожаловать!')
print('Для работы выберите нужный пункт:')


def get_product(current_stock):
    while True:
        for i, item in enumerate(product_types.items()):
            print(f"{i} - {item[1]} ({len(current_stock.products.get(item[0]))}) шт")
        print('q - Вернуться назад')
        p_inp = input('Выберите товар: ')
        if p_inp == 'q':
            return
        else:
            current_stock.get_item(list(product_types.keys())[int(p_inp)])

def add_product(current_stock):
    while True:
        for i, item in enumerate(product_types.items()):
            print(f"{i} - {item[1]} ({len(current_stock.products.get(item[0]))}) шт")
        print('q - Вернуться назад')
        p_inp = input('Выберите товар: ')
        if p_inp == 'q':
            return
        if p_inp == '0':
            new_printer = Printer.add()
            current_stock.set_item(list(product_types.keys())[int(p_inp)], new_printer)
        if p_inp == '1':
            new_scan = Scaner.add()
            current_stock.set_item(list(product_types.keys())[int(p_inp)], new_scan)
        if p_inp == '2':
            new_xerox = Xerox.add()
            current_stock.set_item(list(product_types.keys())[int(p_inp)], new_xerox)

def transfer_to(current_stock):
    while True:
        for i, item in enumerate(product_types.items()):
            print(f"{i} - {item[1]} ({len(current_stock.products.get(item[0]))}) шт")
        print('q - Вернуться назад')
        p_inp = input('Выберите товар: ')
        if p_inp == 'q':
            return
        else:
            key = list(product_types.keys())[int(p_inp)]
            select_product = current_stock.get_item(key)
            for i, s in enumerate(stocks):
                print(f"{i} - {s.name}")
            print('q - Выход')
            s_inp = input('Выбрите склад: ')
            if s_inp == 'q':
                break
            else:
                count = int(input('Введите кол-во товаров которые хотите передать:'))
                current_count = len(current_stock.products.get(key))
                if current_count < count:
                    print(f"На складе осталось {current_count} товаров")
                elif count < 0:
                    print("Введите положительное число")
                elif count == 0:
                    print("Уточните число, возможно вы ошиблись")
                else:
                    s = 0
                    while s < count:
                        select_stock = stocks[int(s_inp)]
                        select_stock.set_item(key, select_product)
                        s += 1


def action_stock(current_stock):
    while True:
        print('0 - Посмотреть наличие товаров')
        print('1 - Добавить товар')
        print('2 - Получить товар')
        print('3 - Передать товар в другой склад')
        print('q - Вернуться в главное меню')
        cs_inp = input('Выбрите действие: ')
        if cs_inp == 'q':
            break
        if cs_inp == '0':
            print(current_stock)
        if cs_inp == '1':
            add_product(current_stock)
        if cs_inp == '2':
            get_product(current_stock)
        if cs_inp == '3':
            transfer_to(current_stock)

while True:
    for i, s in enumerate(stocks):
        print(f"{i} - {s.name}")
    print('q - Выход')
    s_inp = input('Выбрите склад: ')
    if s_inp == 'q':
        break
    else:
        current_stock = stocks[int(s_inp)]
        print(f'Вы находитесь на складе {current_stock.name}')
        action_stock(current_stock)

print(storage)
