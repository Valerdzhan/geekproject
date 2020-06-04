worlds = input("Введите список слов через пробел: ")
w_split = worlds.split()
for i, world in enumerate(w_split):
    print(i, world[:10])
