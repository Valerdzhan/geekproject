mounth = None
while True:
    m = int(input("Введите номер месяца от 1 до 12: "))
    if 0 < m < 12:
        mounth = m
        break
    else:
        continue

print(f"Вы выбрали {mounth} месяц")
year_list = ["зима", "зима", "весна", "весна", "весна", "лето", "лето", "лето", "осень", "осень", "осень", "зима"]
year_dict = {"зима": [12, 1, 2], "весна": [3, 4, 5], "лето": [6, 7, 8], "осень": [9, 10, 11]}

print(f"Время года из листа - {year_list[mounth - 1]}")
for k, v in year_dict.items():
    if v.count(mounth) > 0:
        print(f"Время года из словаря- {k}")
