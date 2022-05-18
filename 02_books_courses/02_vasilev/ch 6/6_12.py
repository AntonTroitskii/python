class MyClass:
    def __init__(self, n):
        self.name = n


A = MyClass("A")
B = MyClass("B")


def hello(self):
    print("Это экземпляр", self.name, "- hello")


def hi(self):
    print(self.name, "- hi")


MyClass.say = hello
print("MyClass.say = hello")

A.say()
B.say()

MyClass.say(A)
MyClass.say(B)

MyClass.say = hi
print("MyClass.say = hi")

A.say()
B.say()

MyClass.say(A)
MyClass.say(B)


del MyClass.say

try:
    A.say()
except AttributeError:
    print("Такого метода нет")

try:
    B.say()
except AttributeError:
    print("Такого метода нет")

try:
    MyClass.say(A)
except AttributeError:
    print("Такого метода нет")