"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.

"""
from googletrans import Translator
translator = Translator()
result_text = []
try:
    with open("text_4.txt", "r", encoding="utf-8") as my_file:
        lines = my_file.readlines()
        for el in lines:
            new_el = translator.translate(el, dest='ru')
            result_text.append(f"{new_el.text}")
    with open("result_ex_4.txt", "w", encoding="utf-8") as result_file:
        for res in result_text:
            result_file.writelines(f"{res}\n")
except IOError:
    print("Error!!!")
