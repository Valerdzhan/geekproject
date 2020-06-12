"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
начиная с 1! и до n!.

Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

"""
while True:
    try:
        n = int(input('Введите число для вычисления факториала: '))

        if n < 0:
            print("Введите чилсо больше 0")
            continue

        if n == 0:
            print("0! = 1")
            break


        def fact(num):
            for el in range(1, num + 1):
                yield el


        result = 1
        str_result = f"{n}! = "
        for i in fact(n):
            result *= i
            str_result += f"{i} = {result}" if i == n else f"{i} * "

        print(str_result)
        break
    except ValueError:
        print('Введеные неправильные данные')
        continue
