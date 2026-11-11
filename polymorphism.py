
# Задача 1.
# Напишите класс Selector. Экземпляр этого класса при инициализации получает список чисел.
# Вызов метода get_odds возвращает нечётные числа из первоначального списка,
# вызов get_evens — чётные. Числа должны идти в том же порядке,
# в котором они были в изначальном списке.

class Selector:
    def __init__(self, values):
        self.values = values

    def get_odds(self):
        return [number for number in self.values if number % 2 != 0]

    def get_evens(self):
        return [number for number in self.values if number % 2 == 0]


# Ожидаемый вывод:
# 11 13 15
# 12 14 16 22 44 66
print("Задача 1. Класс Selector")
values = [11, 12, 13, 14, 15, 16, 22, 44, 66]
selector = Selector(values)
odds = selector.get_odds()
evens = selector.get_evens()
print(' '.join(map(str, odds)))
print(' '.join(map(str, evens)))
print("=================")


# Задача 2.
# Напишите два класса: LeftParagraph и RightParagraph для печати абзаца с выравниванием по левому и правому краю.
# При инициализации экземпляры обоих классов должны принимать целое число — ширину поля вывода.
# В обоих классах нужно реализовать метод add_word для добавления слова в абзац и метод end,
# выводящий полученный абзац на печать и начинающий формирование нового.
# Гарантируется, что длина любого слова не больше ширины поля вывода.

class LeftParagraph:
    def __init__(self, width):
        self.width = width
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def end(self):
        line = ""
        for word in self.words:
            if not line:
                line = word
            elif len(line) + 1 + len(word) <= self.width:
                line += " " + word
            else:
                print(line)
                line = word

        if line:
            print(line)

        self.words = []


class RightParagraph:
    def __init__(self, width):
        self.width = width
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def end(self):
        line = ""
        for word in self.words:
            if not line:
                line = word
            elif len(line) + 1 + len(word) <= self.width:
                line += " " + word
            else:
                print(line.rjust(self.width))
                line = word

        if line:
            print(line.rjust(self.width))

        self.words = []


# Ожидаемый вывод:
# abc defg
# hi
# jklmnopq
# r stuv
#
# abc defg
#       hi
# jklmnopq
#   r stuv
print("Задача 2. Выравнивание абзацев")
lp = LeftParagraph(8)
lp.add_word('abc')
lp.add_word('defg')
lp.add_word('hi')
lp.add_word('jklmnopq')
lp.add_word('r')
lp.add_word('stuv')
lp.end()
print()

rp = RightParagraph(8)
rp.add_word('abc')
rp.add_word('defg')
rp.add_word('hi')
rp.add_word('jklmnopq')
rp.add_word('r')
rp.add_word('stuv')
rp.end()
print("=================")


# Задача 3.
# Форматы записи дат в виде строки в США и Европе отличаются. В США принят формат мм.дд.гггг,
# в Европе — дд.мм.гггг, где дд — день (дополняется нулём слева, если число меньше 10),
# мм — месяц (так же дополняется нулём слева), гггг — год.
# Например, 10 апреля 2000 года будет записано в американском формате как 04.10.2000,
# а в европейском — как 10.04.2000. Все годы в задаче — четырёхзначные.
# Реализуйте классы AmericanDate и EuropeanDate. При инициализации они должны принимать
# год, месяц и число (именно в этом порядке). Так же должны быть реализованы методы
# set_year, set_month, set_day для изменения одной из компонентов даты,
# и get_year, get_month, get_day для чтения компонентов даты.
# Метод format должен возвращать строковое представление (своё для каждого класса).
# Гарантируется, что все даты в тестах корректны и существуют в календаре.

class AmericanDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def set_year(self, year):
        self.year = year

    def set_month(self, month):
        self.month = month

    def set_day(self, day):
        self.day = day

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def format(self):
        return f"{self.month:02d}.{self.day:02d}.{self.year:04d}"


class EuropeanDate(AmericanDate):
    def format(self):
        return f"{self.day:02d}.{self.month:02d}.{self.year:04d}"


# Ожидаемый вывод:
# 04.10.2000
# 10.04.2000
print("Задача 3. Форматы дат")
american = AmericanDate(2000, 4, 10)
european = EuropeanDate(2000, 4, 10)
print(american.format())
print(european.format())
print("=================")


# Задача 4.
# Реализуйте классы MinStat, MaxStat, AverageStat, которые будут находить минимум,
# максимум и среднее арифметическое последовательности целых чисел.
# Экземпляры классов инициализируются без аргументов.
# Метод add_number должен добавлять в статистику число, которое будет учтено при вычислении
# финального результата методом result.
# Для экземпляров MinStat и MaxStat result должен возвращать целое число,
# для AverageStat — число типа float (это число будет сравниваться с правильным ответом
# до седьмой значащей цифры). Если в последовательности отсутствуют числа
# и статистические величины вычислить невозможно, метод result должен возвращать None.

class MinStat:
    def __init__(self):
        self.values = []

    def add_number(self, number):
        self.values.append(number)

    def result(self):
        if not self.values:
            return None
        return min(self.values)


class MaxStat:
    def __init__(self):
        self.values = []

    def add_number(self, number):
        self.values.append(number)

    def result(self):
        if not self.values:
            return None
        return max(self.values)


class AverageStat:
    def __init__(self):
        self.values = []

    def add_number(self, number):
        self.values.append(number)

    def result(self):
        if not self.values:
            return None
        return sum(self.values) / len(self.values)


# Ожидаемый вывод:
# 1 5 3.000
print("Задача 4. Статистика чисел")
values = [1, 2, 4, 5]

mins = MinStat()
maxs = MaxStat()
average = AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)

print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))
print("=================")



# Задача 5.
# Реализуйте класс Table, который хранит целые числа в двумерной таблице.
#
# При инициализации Table(rows, cols) экземпляру передаются число строк и столбцов в таблице.
# Строки и столбцы нумеруются с нуля. Ячейки таблицы инициализируются нулями.
#
# table.get_value(row, col) — прочитать значение из ячейки со строкой row, столбцом col.
# Если ячейка с индексами row и col не лежит внутри таблицы, нужно вернуть None.
# table.set_value(row, col, value) — записать число в ячейку со строкой row, столбцом col.
# Гарантируется, что в тестах будет в запись только в ячейки внутри таблицы.
# table.n_rows() — вернуть число строк в таблице.
# table.n_cols() — вернуть число столбцов в таблице.

class Table:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def get_value(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.data[row][col]
        return None

    def set_value(self, row, col, value):
        self.data[row][col] = value

    def n_rows(self):
        return self.rows

    def n_cols(self):
        return self.cols


# Ожидаемый вывод:
# 0 10 0 0 0
# 0 0 20 0 0
# 0 0 0 30 0
print("Задача 5. Двумерная таблица")
tab = Table(3, 5)
tab.set_value(0, 1, 10)
tab.set_value(1, 2, 20)
tab.set_value(2, 3, 30)
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print("=================")


# Задача 6.
# Реализуйте класс Rectangle для описания прямоугольника, стороны которого параллельны осям координат.
#
# При инициализации экземпляра передаются координаты левой нижней точки прямоугольника x и y,
# а также его ширина и высота w и h. Таким образом, координаты верхнего правого угла — (x + w) и (y + h).
# При вызове метода intersection (например, rect1.intersection(rect2)) должен возвращаться прямоугольник,
# который возникает как пересечение rect1 и rect2. Если прямоугольники не пересекаются,
# должен возвращаться объект None.
# Также необходимо реализовать метод get для каждого из атрибутов класса, возвращающий заданное значение
# данного атрибута. Пример: get_*() - возвращает значение атрибута *.
# Гарантируется, что во входных данных ширина и высота любого прямоугольника положительны.
# Если пересечением прямоугольников является точка или отрезок, то следует считать, что они не пересекаются.

class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_w(self):
        return self.w

    def get_h(self):
        return self.h

    def intersection(self, other):
        left = max(self.x, other.x)
        bottom = max(self.y, other.y)
        right = min(self.x + self.w, other.x + other.w)
        top = min(self.y + self.h, other.y + other.h)

        if left >= right or bottom >= top:
            return None

        return Rectangle(left, bottom, right - left, top - bottom)


# Ожидаемый вывод:
# 5 5 5 5
print("Задача 6. Пересечение прямоугольников")
rect1 = Rectangle(0, 0, 10, 10)
rect2 = Rectangle(5, 5, 10, 10)
rect3 = rect1.intersection(rect2)

if rect3 is None:
    print('No intersection')
else:
    print(rect3.get_x(), rect3.get_y(), rect3.get_w(), rect3.get_h())
print("=================")


# Задача 7.
# Реализуйте класс Table, который хранит целые числа в двумерной таблице.
#
# При инициализации Table(rows, cols) экземпляру передаются число строк и столбцов в таблице.
# Строки и столбцы нумеруются с нуля.
# table.get_value(row, col) — прочитать значение из ячейки в строке row, столбце col.
# Если ячейка с индексами row и col не лежит внутри таблицы, нужно вернуть None.
# table.set_value(row, col, value) — записать число в ячейку строки row, столбца col.
# Гарантируется, что в тестах будет в запись только в ячейки внутри таблицы.
# table.n_rows() — вернуть число строк в таблице
# table.n_cols() — вернуть число столбцов в таблице
# table.delete_row(row) — удалить строку с номером row
# table.delete_col(col) — удалить колонку с номером col
# table.add_row(row) — добавить в таблицу новую строку с индексом row.
# Номера строк >= row, должны увеличится на единицу. Новая строка состоит из нулей.
# table.add_col(col) — добавить в таблицу новую колонку с индексом col.
# Номера колонок >= col, должны увеличится на единицу. Новая колонка состоит из нулей.

class Table:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for i in range(cols)] for i in range(rows)]

    def get_value(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.data[row][col]
        return None

    def set_value(self, row, col, value):
        self.data[row][col] = value

    def n_rows(self):
        return self.rows

    def n_cols(self):
        return self.cols

    def delete_row(self, row):
        self.data.pop(row)
        self.rows -= 1

    def delete_col(self, col):
        for row in self.data:
            row.pop(col)
        self.cols -= 1

    def add_row(self, row):
        self.data.insert(row, [0 for _ in range(self.cols)])
        self.rows += 1

    def add_col(self, col):
        for row in self.data:
            row.insert(col, 0)
        self.cols += 1


# Ожидаемый вывод:
# 0 10 0 0 0
# 0 0 20 0 0
# 0 0 0 30 0
#
# 0 10 0 0 0
# 0 0 0 0 0
# 0 0 20 0 0
# 0 0 0 30 0
print("Задача 7. Изменение двумерной таблицы")
tab = Table(3, 5)
tab.set_value(0, 1, 10)
tab.set_value(1, 2, 20)
tab.set_value(2, 3, 30)
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.add_row(1)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print("=================")


