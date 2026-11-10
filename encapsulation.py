
# Задача 1.
# Напишите класс LittleBell, который при вызове метода sound печатает слово ding.

class LittleBell:
    def sound(self):
        print("ding")


# Ожидаемый вывод:
# ding
print("Задача 1. Класс LittleBell")
bell = LittleBell()
bell.sound()
print("=================")


# Задача 2.
# Напишите класс кнопки Button, экземпляры которого будут измерять количество нажатий на кнопку-объект.
# Метод click увеличивает количество нажатий, метод click_count возвращает число нажатий.
# Метод reset обнуляет количество нажатий.

class Button:
    def __init__(self):
        self.count = 0

    def click(self):
        self.count += 1

    def click_count(self):
        return self.count

    def reset(self):
        self.count = 0


# Ожидаемый вывод:
# 2
# 3
print("Задача 2. Класс Button")
button = Button()
button.click()
button.click()
print(button.click_count())
button.click()
print(button.click_count())
print("=================")


# Задача 3.
# Напишите класс Balance для описания весов с двумя чашами. На левую и правую чашу объекта
# будут добавляться грузы с различным весом, ваша задача определить положение чаш.
# Метод add_right принимает целое число — вес, положенный на правую чашу весов,
# add_left — на левую чашу. Метод result должен возвращать символ =, если вес на чашах
# одинаковый, R — если перевесила правая, L — если перевесила левая.

class Balance:
    def __init__(self):
        self.left = 0
        self.right = 0

    def add_right(self, weight):
        self.right += weight

    def add_left(self, weight):
        self.left += weight

    def result(self):
        if self.left == self.right:
            return "="
        elif self.right > self.left:
            return "R"
        else:
            return "L"


# Ожидаемый вывод:
# =
# R
print("Задача 3. Класс Balance")
balance = Balance()
balance.add_right(10)
balance.add_left(5)
balance.add_left(5)
print(balance.result())
balance.add_right(1)
print(balance.result())
print("=================")


# Задача 4.
# Напишите класс OddEvenSeparator, в который можно добавлять числа, получая потом отдельно
# чётные и нечётные. Числа добавляются в объект с помощью метода add_number.
# Методы even и odd должны возвращать списки чётных и нечётных чисел соответственно.
# Числа в списке должны идти в том же порядке, что и при добавлении в объект.

class OddEvenSeparator:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def even(self):
        return [number for number in self.numbers if number % 2 == 0]

    def odd(self):
        return [number for number in self.numbers if number % 2 != 0]


# Ожидаемый вывод:
# 6 8
# 1 5 3
print("Задача 4. Класс OddEvenSeparator")
separator = OddEvenSeparator()
separator.add_number(1)
separator.add_number(5)
separator.add_number(6)
separator.add_number(8)
separator.add_number(3)
print(' '.join(map(str, separator.even())))
print(' '.join(map(str, separator.odd())))
print("=================")


# Задача 5.
# Напишите класс BigBell, который при вызове метода sound печатает попеременно слова
# ding и dong, начиная c ding.

class BigBell:
    def __init__(self):
        self.next_sound = "ding"

    def sound(self):
        print(self.next_sound)

        if self.next_sound == "ding":
            self.next_sound = "dong"
        else:
            self.next_sound = "ding"


# Ожидаемый вывод:
# ding
# dong
# ding
print("Задача 5. Класс BigBell")
bell = BigBell()
bell.sound()
bell.sound()
bell.sound()
print("=================")


# Задача 6.
# Напишите класс MinMaxWordFinder. Класс должен уметь анализировать текст и находить в нём
# слова наименьшей и наибольшей длины. Текст состоит из предложений, которые добавляются
# в обработку методом add_sentence. Метод shortest_words возвращает список самых коротких
# на данный момент слов, метод longest_words — самых длинных. Слова, возвращаемые методами
# shortest_words и longest_words, должны быть отсортированы по алфавиту.
# Если одно из самых коротких слов встретилось в исходных предложениях несколько раз,
# оно должно столько же раз повториться в списке самых коротких слов.
# Самые длинные слова наоборот должны входить в список без повторов.

class MinMaxWordFinder:
    def __init__(self):
        self.words = []

    def add_sentence(self, sentence):
        self.words.extend(sentence.split())

    def shortest_words(self):
        min_length = min(len(word) for word in self.words)
        return sorted(
            word for word in self.words if len(word) == min_length
        )

    def longest_words(self):
        max_length = max(len(word) for word in self.words)
        return sorted(
            set(word for word in self.words if len(word) == max_length)
        )


# Ожидаемый вывод:
# abc def
# hello qwert world
print("Задача 6. Класс MinMaxWordFinder")
finder = MinMaxWordFinder()
finder.add_sentence('hello abc world')
finder.add_sentence('def asdf qwert')
print(' '.join(finder.shortest_words()))
print(' '.join(finder.longest_words()))
print("=================")


# Задача 7.
# Создайте класс BoundingRectangle, который обрабатывает точки на плоскости и строит по ним
# прямоугольник минимального размера, в который входят все эти точки.
# Если точка лежит на границе прямоугольника, считается, что она в него входит.
# Нужно определить следующие методы (rect – экземпляр BoundingRectangle):
# rect.add_point(x, y) — добавить новую точку.
# rect.width() — ширина прямоугольника.
# rect.height() — высота прямоугольника.
# rect.bottom_y() — Y-координата нижней границы прямоугольника.
# rect.top_y() — Y-координата верхней границы прямоугольника.
# rect.left_x() — X-координата левой границы прямоугольника.
# rect.right_x() — X-координата правой границы прямоугольника.
# Гарантируется, что хотя бы одна точка будет добавлена в экземпляр до вызова методов,
# возвращающих описание прямоугольника.

class BoundingRectangle:
    def __init__(self):
        self.points = []

    def add_point(self, x, y):
        self.points.append((x, y))

    def width(self):
        return self.right_x() - self.left_x()

    def height(self):
        return self.top_y() - self.bottom_y()

    def bottom_y(self):
        return min(y for x, y in self.points)

    def top_y(self):
        return max(y for x, y in self.points)

    def left_x(self):
        return min(x for x, y in self.points)

    def right_x(self):
        return max(x for x, y in self.points)


# Ожидаемый вывод:
# -1 3
# -2 4
# 4 6
print("Задача 7. Класс BoundingRectangle")
rect = BoundingRectangle()
rect.add_point(-1, -2)
rect.add_point(3, 4)
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())
print("=================")
