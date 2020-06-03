n = int(input('Enter n: '))
i = 1
# Делаем
str_n = str(n)
summ = 0

while i <= n:
    summ += int(str_n)
    str_n = str_n + str(n)
    i += 1


print('Result: {}'.format(summ))
