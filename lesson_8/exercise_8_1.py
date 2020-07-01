"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""
import calendar


class NoDate(Exception):
    def __init__(self, txt):
        self.txt = txt


def dateToNum(date):
    """
    Преобразовывает строковую дату в лист из чисел

    :param date: Дата в формате "дд-мм-гггг"
    :return: Лист с числами [дд, мм, гггг]
    """

    date_split = date.split('-')
    day = date_split[0]
    month = date_split[1]
    year = date_split[2]
    return [int(day), int(month), int(year)]


class Date:

    def __init__(self, date):
        try:
            if type(Date.validate(date)) == bool:
                self.date = date
            else:
                raise NoDate(Date.validate(date))
        except NoDate as err:
            print(err)

    @classmethod
    def get_nums(cls, date):
        return dateToNum(date)

    @staticmethod
    def validate(date):
        try:
            date_num_list = dateToNum(date)
            day = date_num_list[0]
            month = date_num_list[1]
            year = date_num_list[2]
            if year < 1900 or year > 3000:
                return f"Это слишком давно или еще не скоро наступит"
            if month < 1 or month > 12:
                return f"Таких месяцев не бывает"
            day_count = calendar.monthrange(year, month)[1]
            if day > day_count:
                return f"Не верное количество дней в месяце, {day_count} дней в этом месяце"

            return True
        except IndexError:
            return f"Не верное значение! Проверьте вводимое значение"


d = Date("30-05-2000")
day = Date.get_nums("30-05-2000")[0]
month = Date.get_nums("30-05-2000")[1]
year = Date.get_nums("30-05-2000")[2]
print(day)
print(month)
print(year)
