number = int(input('Enter number: '))
max_number = 0

while True:
    # Находим последнее число
    current_number = number % 10
    # Если число равно 9, то мы считаем это максимальным, прерываем цикл
    if current_number == 9:
        max_number = current_number
        break
    # Проверяем число с текущим максимальным
    # если число больше, то делаем его максимальным
    if current_number > max_number:
        max_number = current_number
    # Находим и проверям все ли цифры мы проверили
    # если число равно 0 значит проверили все цифры, прерываем цикл
    number = number // 10
    if number == 0:
        break

print(f'Max number: {max_number}')
