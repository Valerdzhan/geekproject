"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
 количества слов в каждой строке.

"""

my_list = []


def count_word_line(line):
    words = line.split()
    return len(words)


while True:
    str_line = input('Введите текст. (для выхода оставьте пустую строку): ')
    if len(str_line) == 0:
        break
    my_list.append(str_line)

with open('my_file.txt', 'w', encoding="utf-8") as my_file:
    for line in my_list:
        my_file.writelines(f"{line}\n")

# ------------ 2 ----------------

with open('my_file.txt', 'r', encoding="utf-8") as my_file:
    str_lines = my_file.readlines()
    print(f"Кол-во строк в файле: {len(str_lines)}")
    count = 1
    for line in str_lines:
        print(f"Count words in {count} line: {count_word_line(line)}")
        count += 1
