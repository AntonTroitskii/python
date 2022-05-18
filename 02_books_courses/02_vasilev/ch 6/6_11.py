class MyClass:
    pass


A = MyClass()
B = MyClass()
C = MyClass()


def hello():
    print("Метод экземпляра - 'hello'")


def hi():
    print("Метод экземпляра - 'hi'")

print(type(hello), type(hi))

A.say = hello
C.say = hi

A.say()
try:
    B.say()
except AttributeError:
    print("Такого метода нет")

C.say()

print()
try:
    MyClass.say()
except AttributeError:
    print("Такой фукнции нет")

del A.say

try:
    A.say()
except AttributeError:
    print("Такого метода нет")

C.say()
