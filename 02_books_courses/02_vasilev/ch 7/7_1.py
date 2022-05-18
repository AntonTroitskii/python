class BaseClass:
    name_base = 'Класс BaseClass'

    def say_base(self):
        print("Метод say_base()")


class NewClass(BaseClass):
    name_new = "Класс NewClass"

    def say_new(self):
        print("Метод say_new()")


print("Класс BaseClass и экземпляр obj_base:")
obj_base = BaseClass()
obj_new = NewClass()
print(BaseClass.name_base)
obj_base.say_base()

print("\nКласс NewClass и экземпляр obj_new:")

print(NewClass.name_base)
obj_new.say_base()
print(NewClass.name_new)
obj_new.say_new()
