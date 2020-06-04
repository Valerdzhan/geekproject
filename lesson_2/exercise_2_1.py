list = [1, 2.3, "3", True, False, [1, 2], ("1", "2"), {1, 2}, {"name": "Valera", "Surname": "Ivanov"}, None]

for i in list:
    if type(i) is str:
        print(f"Переменная {i} - сторка ({type(i)})")
    elif type(i) is int:
        print(f"Переменная {i} - целочисленный тип ({type(i)})")
    elif type(i) is float:
        print(f"Переменная {i} - вещественное число ({type(i)})")
    elif type(i) is bool:
        print(f"Переменная {i} - булевый тип ({type(i)})")
    elif type(i) is list:
        print(f"Переменная {i} - список ({type(i)})")
    elif type(i) is tuple:
        print(f"Переменная {i} - кортеж ({type(i)})")
    elif type(i) is set:
        print(f"Переменная {i} - множество ({type(i)})")
    elif type(i) is dict:
        print(f"Переменная {i} - словарь ({type(i)})")
    elif type(i) is None:
        print(f"Переменная {i} - none тип({type(i)})")
    else:
        print(f"Тип переменной у которой нет проверки: {i} - тип ({type(i)})")