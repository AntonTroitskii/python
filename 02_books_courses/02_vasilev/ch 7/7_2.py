class BaseClass:
    name = "Поле name"

    def say(self):
        print("Метод say()")


class NewClass(BaseClass):
    pass


obj = NewClass()
print(NewClass.name)
obj.say()

BaseClass.name = "Новое значение поля name"


def hello(self):
    print("Новый метод hello()")


BaseClass.say = hello

print(NewClass.name)
obj.say()
