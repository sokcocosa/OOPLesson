

# Задача 1.
# В игре Minecraft все игровые объекты делятся на три типа: блоки, сущности и предметы.
# Блоки – это «кирпичики», из которых состоит весь игровой мир.
# Сущности – это все динамические и движущиеся игровые объекты.
# Предметы – это все остальные объекты.
# Реализуйте иерархию классов для игры Minecraft:
# BaseObject – базовый класс для всех объектов.
# Интерфейс этого класса состоит из двух методов:
# __init__(x, y, z) – конструктор класса, который принимает на вход 3 числа
# (координаты объекта в игровом мире).
# get_coordinates() – метод, возвращающий список координат x, y, z (именно в таком порядке).
# Block – класс, наследующийся от BaseObject.
# У этого класса есть дополнительный метод shatter(), который ничего не принимает на вход
# и ничего не возвращает. При вызове этого метода все три координаты объекта Block должны стать равны None.
# Entity – класс, наследующийся от BaseObject.
# У этого класса есть дополнительный метод move(x, y, z), который принимает на вход 3 числа
# (новые координаты объекта) и ничего не возвращает.
# При вызове этого метода координаты объекта должны стать равны x, y, z соответственно.
# Thing – класс, наследующийся от BaseObject.
# У этого класса нет дополнительных методов.

class BaseObject:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_coordinates(self):
        return [self.x, self.y, self.z]


class Block(BaseObject):
    def shatter(self):
        self.x = None
        self.y = None
        self.z = None


class Entity(BaseObject):
    def move(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Thing(BaseObject):
    pass


# Ожидаемый вывод:
# [1, 2, 3]
# [None, None, None]
# [10, 11, 12]
# [7, 8, 9]
# True True True
print("Задача 1. Наследование в Minecraft")
block = Block(1, 2, 3)
entity = Entity(4, 5, 6)
thing = Thing(7, 8, 9)
print(block.get_coordinates())
block.shatter()
print(block.get_coordinates())
entity.move(10, 11, 12)
print(entity.get_coordinates())
print(thing.get_coordinates())
print(issubclass(Block, BaseObject), issubclass(Entity, BaseObject), issubclass(Thing, BaseObject))
print("=================")


# Задача 2.
# Рассмотрим следующую упрощенную классификацию живых существ:
# Живые существа делятся на бесклеточных (к ним относятся вирусы) и клеточных.
# Клеточные в свою очередь делятся на прокариотов (их клетки не содержат ядер;
# к прокариотам относятся бактерии) и эукариотов (их клетки имеют ядра).
# Эукариоты – одноклеточные, грибы, растения и животные.
# Постройте иерархию классов для данной классификации.
# Для именования классов используйте латинские названия:
# Бесклеточные: Acellularia
# Клеточные: Cellularia
# Прокариоты: Prokaryota
# Эукариоты: Eukaryota
# Одноклеточные: Unicellularia
# Грибы: Fungi
# Растения: Plantae
# Животные: Animalia

class Acellularia:
    pass


class Cellularia:
    pass


class Prokaryota(Cellularia):
    pass


class Eukaryota(Cellularia):
    pass


class Unicellularia(Eukaryota):
    pass


class Fungi(Eukaryota):
    pass


class Plantae(Eukaryota):
    pass


class Animalia(Eukaryota):
    pass


# Ожидаемый вывод:
# True True
# True True True True
# True False False False
print("Задача 2. Классификация живых существ")
print(issubclass(Prokaryota, Cellularia), issubclass(Eukaryota, Cellularia))
print(issubclass(Unicellularia, Eukaryota), issubclass(Fungi, Eukaryota),
      issubclass(Plantae, Eukaryota), issubclass(Animalia, Eukaryota))
print(issubclass(Animalia, Cellularia), issubclass(Acellularia, Cellularia),
      issubclass(Fungi, Prokaryota), issubclass(Eukaryota, Prokaryota))
print("=================")


# Задача 3.
# Разобьём пользователей интернет-обучения на три группы: администраторы,
# преподаватели и ученики. Все пользователи могут решать задачи.
# Также администраторы могут редактировать задачи, а преподаватели могут
# проверять решения учеников. Также среди администраторов есть особенные
# «супер-администраторы», которые могут сделать администратором любого
# пользователя портала.
# Реализуйте следующую иерархию классов:
# User – базовый класс с методом solve(n), где n – целое число (идентификатор задачи).
# Student – класс, наследующийся от User.
# Teacher – класс, наследующийся от User и имеющий дополнительный метод
# check_solution(user, n), где user – объект типа User, а n – целое число
# (идентификатор задачи).
# Admin – класс, наследующийся от User и имеющий дополнительный метод
# edit(n), где n – целое число (идентификатор задачи).
# SuperAdmin – класс, наследующийся от Admin и имеющий дополнительный метод
# grant(user), где user – объект типа User.

class User:
    def solve(self, n):
        pass


class Student(User):
    pass


class Teacher(User):
    def check_solution(self, user, n):
        pass


class Admin(User):
    def edit(self, n):
        pass


class SuperAdmin(Admin):
    def grant(self, user):
        pass


# Ожидаемый вывод:
# True True True True
# True False False
# True False
# True False
# True True True
print("Задача 3. Пользователи интернет-обучения")
print(issubclass(Student, User), issubclass(Teacher, User),
      issubclass(Admin, User), issubclass(SuperAdmin, Admin))
print(hasattr(Student, 'solve'), hasattr(Student, 'check_solution'), hasattr(Student, 'edit'))
print(hasattr(Teacher, 'check_solution'), hasattr(Teacher, 'edit'))
print(hasattr(Admin, 'edit'), hasattr(Admin, 'grant'))
print(hasattr(SuperAdmin, 'solve'), hasattr(SuperAdmin, 'edit'), hasattr(SuperAdmin, 'grant'))
print("=================")


# Задача 4.
# В социальной сети есть два вида пользователей: люди и сообщества.
# Все пользователи должны указывать свое имя.
# Люди могут также указывать свою дату рождения, а сообщества – своё краткое описание.
# Все пользователи (и люди, и сообщества) могут отправлять сообщения друг другу,
# а также выкладывать посты на своей стене.
# Люди могут подписываться на других людей и на сообщества.
# Реализуйте иерархию классов в соответствии с этим описанием.
# User – базовый класс. Его конструктор должен принимать один аргумент – имя.
# Также этот класс должен предоставлять методы:
# send_message(user, message) – отправить сообщение message пользователю user
# post(message) – отправить сообщение message себе на стену
# info() – вернуть строку с дополнительной информацией о пользователе.
# Для класса User это пустая строка, метод info() будет переопределяться в производных классах.
# describe() – напечатать имя пользователя, а на следующей строке — дополнительную информацию о нем
# (т.е. результат работы метода info()), если она не пустая.
# Person – производный от класса User. Его конструктор должен принимать на вход два аргумента –
# имя и дату рождения.
# Метод info() класса Person должен возвращать строку вида «Дата рождения: ...»
# Также у Person должен быть реализован дополнительный метод subscribe(user),
# где user – объект класса User.
# Community – производный от класса User. Его конструктор должен принимать на вход два аргумента –
# имя и краткое описание.
# Метод info() класса Community должен возвращать строку вида «Описание: ...»

class User:
    def __init__(self, name):
        self.name = name

    def send_message(self, user, message):
        pass

    def post(self, message):
        pass

    def info(self):
        return ""

    def describe(self):
        print(self.name)
        if self.info():
            print(self.info())


class Person(User):
    def __init__(self, name, birth_date):
        super().__init__(name)
        self.birth_date = birth_date

    def info(self):
        return f"Дата рождения: {self.birth_date}"

    def subscribe(self, user):
        pass


class Community(User):
    def __init__(self, name, description):
        super().__init__(name)
        self.description = description

    def info(self):
        return f"Описание: {self.description}"


# Ожидаемый вывод:
# Аноним
# Иван Иванов
# Дата рождения: 01.01.2000
# Любители Python
# Описание: Пишем на Python
# True True
# True False
# True True
print("Задача 4. Пользователи социальной сети")
user = User('Аноним')
person = Person('Иван Иванов', '01.01.2000')
community = Community('Любители Python', 'Пишем на Python')
user.describe()
person.describe()
community.describe()
print(isinstance(person, User), isinstance(community, User))
print(hasattr(person, 'subscribe'), hasattr(community, 'subscribe'))
print(hasattr(community, 'send_message'), hasattr(community, 'post'))
print("=================")


# Задача 5.
# Все животные обладают некоторыми общими свойствами; в частности,
# они дышат кислородом и чем-то питаются.
# К животным относятся рыбы, которые умеют плавать, и птицы, которые откладывают яйца.
# Большинство птиц (но не все!) также умеют летать.
# Реализуйте следующую иерархию классов:
# Animal – базовый класс с методами breathe() и eat()
# Fish – наследник класса Animal с дополнительным методом swim()
# Bird – наследник класса Animal с дополнительным методом lay_eggs()
# FlyingBird – наследник класса Bird с дополнительным методом fly()
# Сами методы breathe, eat, swim, lay_eggs и fly реализовывать не нужно.
# То есть, например, для метода breathe достаточно написать def breathe(self): pass.

class Animal:
    def breathe(self):
        pass

    def eat(self):
        pass


class Fish(Animal):
    def swim(self):
        pass


class Bird(Animal):
    def lay_eggs(self):
        pass


class FlyingBird(Bird):
    def fly(self):
        pass


# Ожидаемый вывод:
# True True True
# True True False
# True True False
# True True False
print("Задача 5. Иерархия животных")
print(issubclass(Fish, Animal), issubclass(Bird, Animal), issubclass(FlyingBird, Bird))
print(hasattr(Fish, 'breathe'), hasattr(Fish, 'swim'), hasattr(Fish, 'lay_eggs'))
print(hasattr(Bird, 'eat'), hasattr(Bird, 'lay_eggs'), hasattr(Bird, 'fly'))
print(hasattr(FlyingBird, 'lay_eggs'), hasattr(FlyingBird, 'fly'), hasattr(FlyingBird, 'swim'))
print("=================")


# Задача 6.
# Реализуйте иерархию транспортных средств.
# За основу можно взять такую:
# Водный транспорт.
# Воздушный транспорт. Можно поделить на авиацию (самолёты)
# и воздухоплавание (дирижабли и воздушные шары).
# Наземный транспорт. Делится на железнодорожный, автомобильный,
# велосипедный и движимый животными.
# Космический транспорт.
# Постарайтесь реализовать иерархию максимально подробно,
# дополните предложенный вариант своими классами.
# Имена классов выберите самостоятельно.

class Transport:
    pass


class WaterTransport(Transport):
    pass


class AirTransport(Transport):
    pass


class Aviation(AirTransport):
    pass


class AirshipTransport(AirTransport):
    pass


class GroundTransport(Transport):
    pass


class RailwayTransport(GroundTransport):
    pass


class AutomobileTransport(GroundTransport):
    pass


class BicycleTransport(GroundTransport):
    pass


class AnimalDrawnTransport(GroundTransport):
    pass


class SpaceTransport(Transport):
    pass


print("Задача 6. Иерархия транспортных средств")
print("Тестовых задач нет, сам код написан с 341 строки")
print("=================")


# Задача 7.
# С помощью наследования постройте иерархию геометрических фигур,
# состоящую из следующих классов:
# Shape (Фигура)
# Polygon (Многоугольник)
# Triangle (Треугольник)
# IsoscelesTriangle (Равнобедренный треугольник)
# EquilateralTriangle (Равносторонний треугольник)
# Quadrilateral (Четырехугольник)
# Parallelogram (Параллелограмм)
# Rectangle (Прямоугольник)
# Square (Квадрат)
# Иерархия должна быть построена в соответствии со следующим условием:
# класс B должен наследоваться от класса A, если B является частным случаем A.
# Сами классы реализовывать не нужно.

class Shape:
    pass


class Polygon(Shape):
    pass


class Triangle(Polygon):
    pass


class IsoscelesTriangle(Triangle):
    pass


class EquilateralTriangle(IsoscelesTriangle):
    pass


class Quadrilateral(Polygon):
    pass


class Parallelogram(Quadrilateral):
    pass


class Rectangle(Parallelogram):
    pass


class Square(Rectangle):
    pass


# Ожидаемый вывод:
# True True True True
# True True True True
# True True
# False False False
print("Задача 7. Иерархия геометрических фигур")
print(issubclass(Polygon, Shape), issubclass(Triangle, Polygon),
      issubclass(IsoscelesTriangle, Triangle), issubclass(EquilateralTriangle, IsoscelesTriangle))
print(issubclass(Quadrilateral, Polygon), issubclass(Parallelogram, Quadrilateral),
      issubclass(Rectangle, Parallelogram), issubclass(Square, Rectangle))
print(issubclass(Square, Shape), issubclass(EquilateralTriangle, Polygon))
print(issubclass(Square, Triangle), issubclass(Triangle, Quadrilateral), issubclass(Shape, Polygon))
print("=================")


# Задача 8.
# Реализуйте несколько классов, вычисляющих суммы следующих последовательностей
# натуральных чисел от 1 до N:
# 1+2+3+…+N
# 1+2^2+3^2+…+N^2
# 1+2^3+3^3+…+N^3
# Сделайте это с помощью наследования.
# Базовым классом будет Summator, который реализует методы transform(n) и sum(N).
# Метод transform(n) выполняет преобразование элемента последовательности.
# Для класса Summator это будет тождественное преобразование, т.е. transform(n) == n.
# Метод transform(n) будет переопределяться в производных классах.
# Метод sum(N) должен вычислять сумму значений transform(n) для всех значений n от 1 до N.
# Производные классы должны переопределять метод transform(n):
# SquareSummator: transform(n) == n ** 2
# CubeSummator: transform(n) == n ** 3
# Метод sum(N) переопределять не нужно.

class Summator:
    def transform(self, n):
        return n

    def sum(self, N):
        return sum(self.transform(n) for n in range(1, N + 1))


class SquareSummator(Summator):
    def transform(self, n):
        return n ** 2


class CubeSummator(Summator):
    def transform(self, n):
        return n ** 3


# Ожидаемый вывод:
# 55 385 3025
# 3 9 27
# True True
# False False
print("Задача 8. Вычисление сумм последовательностей")
print(Summator().sum(10), SquareSummator().sum(10), CubeSummator().sum(10))
print(Summator().transform(3), SquareSummator().transform(3), CubeSummator().transform(3))
print(issubclass(SquareSummator, Summator), issubclass(CubeSummator, Summator))
print('sum' in SquareSummator.__dict__, 'sum' in CubeSummator.__dict__)
print("=================")


# Задача 9.
# На сайте поиска вакансий есть два типа объектов: вакансии и резюме.
# Каждый такой объект имеет название профессии (в вакансии – предлагаемая профессия,
# в резюме – желаемая профессия).
# Также в вакансиях указывается название компании и предлагаемая зарплата,
# а в резюме – стаж работы.
# Реализуйте иерархию классов для такого сайта.
# Profile – базовый класс. Его конструктор должен принимать один аргумент – название профессии.
# Также этот класс должен предоставлять методы:
# info(), который должен возвращать строку с дополнительной информацией.
# Для класса Profile эта строка должна быть пустой, в производных классах этот метод будет переопределяться.
# describe(), который печатает название, а на следующей строке — дополнительную информацию
# (т.е. результат работы метода info()), если она не пустая.
# Vacancy – наследник класса Profile. Его конструктор должен принимать два аргумента –
# название профессии и предлагаемую зарплату.
# При написании конструктора используйте конструктор базового класса.
# Метод info() класса Vacancy должен возвращать строку вида «Предлагаемая зарплата: ...»
# Resume – наследник класса Profile. Его конструктор должен принимать два аргумента –
# название профессии и стаж работы.
# При написании конструктора используйте конструктор базового класса.
# Метод info() класса Resume должен возвращать строку вида «Стаж работы: ...»

class Profile:
    def __init__(self, profession):
        self.profession = profession

    def info(self):
        return ""

    def describe(self):
        print(self.profession)
        if self.info():
            print(self.info())


class Vacancy(Profile):
    def __init__(self, profession, salary):
        super().__init__(profession)
        self.salary = salary

    def info(self):
        return f"Предлагаемая зарплата: {self.salary}"


class Resume(Profile):
    def __init__(self, profession, experience):
        super().__init__(profession)
        self.experience = experience

    def info(self):
        return f"Стаж работы: {self.experience}"


# Ожидаемый вывод:
# Дворник
# Программист
# Предлагаемая зарплата: 100000
# Программист
# Стаж работы: 5
# True True
print("Задача 9. Профили сайта поиска вакансий")
profile = Profile('Дворник')
vacancy = Vacancy('Программист', 100000)
resume = Resume('Программист', 5)
profile.describe()
vacancy.describe()
resume.describe()
print(isinstance(vacancy, Profile), isinstance(resume, Profile))
print("=================")


# Задача 10.
# Создайте класс Triangle, представляющий треугольник.
# Конструктор этого класса должен принимать на вход 3 числа (длины сторон треугольника).
# Также у этого класса должен быть метод perimeter(), возвращающий периметр.
# Отнаследуйте от класса Triangle класс EquilateralTriangle, представляющий равносторонний треугольник.
# Переопределите конструктор этого класса с использованием конструктора базового класса.
# Конструктор класса EquilateralTriangle должен принимать на вход 1 число (длину стороны).

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c


class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)


# Ожидаемый вывод:
# 12 15
# True
print("Задача 10. Треугольники")
triangle = Triangle(3, 4, 5)
equilateral = EquilateralTriangle(5)
print(triangle.perimeter(), equilateral.perimeter())
print(isinstance(equilateral, Triangle))
print("=================")


# Задача 11.
# Реализуйте класс PowerSummator, вычисляющий сумму последовательности натуральных чисел от 1 до N:
# 1+2^b+3^b+…+N^b, где b – произвольное вещественное число.
# Как и в задаче 8, класс PowerSummator должен наследоваться от класса Summator.
# Напомним, что класс Summator должен иметь методы transform(n) и sum(N).
# Метод transform(n) выполняет преобразование элемента последовательности.
# Для класса Summator это будет тождественное преобразование, т.е. transform(n) == n.
# Метод transform(n) должен быть переопределен в классе PowerSummator.
# Метод sum(N) должен вычислять сумму значений transform(n) для всех значений n от 1 до N.
# Помимо метода transform, для класса PowerSummator также нужно переопределить конструктор.
# Конструктор класса PowerSummator должен принимать один параметр – степень b,
# в которую нужно возводить элементы последовательности.
# Также отнаследуйте от класса PowerSummator классы SquareSummator и CubeSummator,
# которые (как и в классной задаче 8) должны вычислять суммы квадратов и кубов соответственно.
# Конструкторы классов SquareSummator и CubeSummator не должны принимать аргументов.
# В классах SquareSummator и CubeSummator должен быть переопределён только конструктор;
# переопределять другие методы нельзя.

class PowerSummator(Summator):
    def __init__(self, b):
        self.b = b

    def transform(self, n):
        return n ** self.b


class SquareSummator(PowerSummator):
    def __init__(self):
        super().__init__(2)


class CubeSummator(PowerSummator):
    def __init__(self):
        super().__init__(3)


# Ожидаемый вывод:
# 55 385 3025
# 385 3025
# 6.1463
print("Задача 11. Сумматор степеней")
print(PowerSummator(1).sum(10), PowerSummator(2).sum(10), PowerSummator(3).sum(10))
print(SquareSummator().sum(10), CubeSummator().sum(10))
print(round(PowerSummator(0.5).sum(4), 4))
print("=================")
