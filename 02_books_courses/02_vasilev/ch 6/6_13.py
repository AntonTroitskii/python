class MyClass:
    def __init__(self, n):
        self.name = n

    def say(self):
        print("Класс MyClass:", self.name)


A = MyClass("A")
B = MyClass("B")

A.say()
B.say()

F = A.say
F()

A.say = "Поле экземпляра А"
print(A.say)

try:
    A.say()
except TypeError:
    print("Неверная команда")
B.say()
F()
