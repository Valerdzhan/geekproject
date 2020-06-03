time = int(input('Enter the time in seconds: '))
hh = 0
mm = 0
ss = 0
# делители часы/минуты
hours_divider = 3600
minutes_divider = 60

# Находим часы, остаток от деления считаем за минуты
hh = time // hours_divider
if hh > 0:
    time -= hh * hours_divider
# Находим минуты, остаток от деления считаем за секунды
mm = time // minutes_divider
if mm > 0:
    time -= mm * minutes_divider
ss = time

print(f'Result: {hh:02}:{mm:02}:{ss:02}')
