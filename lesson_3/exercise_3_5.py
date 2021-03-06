"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
к полученной ранее сумме и после этого завершить программу.
"""
is_continue = True
sum = 0
while True:
    input_num = input('Введите числа через пробел: ')
    _list = input_num.split()
    for n in _list:
        try:
            if n == 'q':
                break
            sum += int(n)
        except ValueError:
            print('Вы ввели недопустимый символ')
            is_continue = False
            break
    print(f"Summa: {sum}")
    if not is_continue:
        break
