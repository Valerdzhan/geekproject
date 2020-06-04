list = input('Введите список через запятую ",": ')
list = list.split(",")
result_list = []
for i in range(len(list[::2])):
    if len(list[1::2]) > i:
        result_list.append(list[1::2][i])
    result_list.append(list[::2][i])
print(list)
print(result_list)
