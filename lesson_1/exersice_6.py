start = int(input('Enter start value: '))
finish = int(input('Enter finish value: '))

day = 1
result = start
while True:
    if result > finish:
        break
    result += result * 0.1
    day += 1


print(day)
