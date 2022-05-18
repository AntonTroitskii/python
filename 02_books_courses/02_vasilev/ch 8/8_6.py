# Функция с аргументом - классом и
# результатом - объектом класса

def F(A):
    class Alpha(A):
        def hi(self):
            print('Класс Aplpha!')

    return Alpha


# Функция с аргументом - классом и
# результатом - объектом класса
def Q(A):
    class Bravo(A):
        def hi(self):
            print('Класс Bravo!')

    return Bravo


# Класс с декоратором
@F  # Декоратор класса
class First:
    def hello(self):
        print('Класс First!')


# Класс с декоратором
@F  # Декоратор класса
class Second:
    def hello(self):
        print('Класс Second!')

    def hi(self):
        print('Класс Second. Hi!')


@Q
@F
class Third:
    def hello(self):
        print('Класс Third!')


def show_obj(obj):
    # Класс экземпляра
    print('Класс экземпляра:', obj.__class__)
    # Вызов методов экземпляра
    obj.hi()
    obj.hello()


def show_class(A):
    # Имя класса
    print('Имя класса:', A.__name__)
    # Базовы класс
    print('Базовы класс:', A.__bases__)
    # Цепочка наследования
    print('Цепочка наследования:', A.__mro__)


one = First()
two = Second()
three = Third()

# print('Экземпляры классов.')
# for obj in [one, two, three]:
#     show_obj(obj)
#
# print('\nКлассы.')
# for A in [First, Second, Third]:
#     show_class(A)


print(Second.__bases__)
print(Second.__mro__)
super(Second, two).hi()
# two.hi()
