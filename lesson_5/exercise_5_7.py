"""
Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.

"""
import json


def profit(revenue, costs):
    return revenue - costs


def firm_dict(_firm):
    num_arr = []
    firm_items = _firm.split()
    firm_name = firm_items[0]
    for el in firm_items:
        if int(el.isdigit()):
            num_arr.append(int(el))
    return dict({firm_name: profit(num_arr[0], num_arr[1])})


def write_in_file(data):
    with open('result_ex_7.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file)


try:
    average_profit = 0
    result_dict = list()
    with open("text_7.txt", "r", encoding="utf-8") as file:
        firms = file.readlines()
        firm_profit_dict = dict()
        for firm in firms:
            firm_profit_dict.update(firm_dict(firm))

        for prof in firm_profit_dict.values():
            if prof > 0:
                average_profit += prof

        average_profit_dict = dict(average_profit=average_profit)
        result_dict.append(firm_profit_dict)
        result_dict.append(average_profit_dict)
        write_in_file(result_dict)
except IOError:
    print("Error!!!")
