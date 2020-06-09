"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""

ord_start = ord('a')
ord_finish = ord('z')


def int_func(var_word):
    for w in var_word:
        if ord_start <= ord(w) <= ord_finish:
            continue
        else:
            print(f'Вы ввели недопустимый символ {w}')
            return ValueError
            break
    return var_word.title()


def words_func(var_words):
    try:
        words_list = var_words.split()
        result = ''
        for word_item in words_list:
            try:
                result += int_func(word_item) + ' '
            except TypeError:
                return 'Ошибка'
        return result
    except ValueError:
        return


word = input('Введите слово из маленьких латинских букв: ')
words = input('Введите слова из маленьких латинских букв через пробелы: ')

print(int_func(word))
print(words_func(words))
