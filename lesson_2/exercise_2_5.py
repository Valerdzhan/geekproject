enter_list = input("Введите список чисел через пробел: ")
str_list = enter_list.split()
my_list = []
for sl in str_list:
    my_list.append(int(sl))

num = int(input('Введите число: '))
length = len(my_list)
print(f"Исходный список: {my_list}")

for j in range(len(my_list)):
    for i in range(len(my_list) - j):
        a = my_list[i]
        if i + 1 < length:
            b = my_list[i + 1]
            if a < b:
                my_list[i] = b
                my_list[i + 1] = a

print(f"Отсортированный список: {my_list}")

if num in my_list:
    index = my_list.index(num)
    my_list.insert(index + 1, num)
else:
    index = length
    for i in range(len(my_list)):
        if num > my_list[i]:
            index = i
            break
    my_list.insert(index, num)

print(f"Результат: {my_list}")
