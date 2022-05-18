class Alpha:
    "Класс Aplha и внутренний класс Bravo"

    def hello(self):
        pass

    class Bravo:
        pass


class Charlie(Alpha):
    "Класс Charilie наследуется от класса Alpha"
    pass


class Delta(Charlie):
    pass


obj = Alpha()

print("Gjkt __class__")
print("Экземпляр obj:", obj.__class__)

print("Класс Alpha:", Alpha.__class__)
print("Класс Aplpha.Bravo:", Alpha.Bravo.__class__)
print("Класс Charile:", Charlie.__class__)

print("\nПоля __bases__ и __mro__")
print("Класс Delta, поле __bases__:", Delta.__bases__)
print("Класс Delta, поле __mro__:", Delta.__mro__)
print("Класс Alpha, поле __bases__:", Alpha.__bases__)
print("Класс Alpha, поле __mro__:", Alpha.__mro__)

print("\nПоле __doc__")
print("Описание класса Alpha:", Alpha.__doc__)
print("Описание класса Charlie:", Charlie.__doc__)
Delta.__doc__ = "Класс Delta наследует класс Charlie"
print("Описчание класса Delta:", Delta.__doc__)

print("\nПоле __module__")
print("Модуль класса Alpha:", Alpha.__module__)

print("\nПоле __dict__")
print('Атрибуты класса Alpha:', Alpha.__dict__)
print('Атрибуты класса Alpha.Bravo:', Alpha.Bravo.__dict__)
print('Атрибуты класса Delta:', Delta.__dict__)

print('\nПоля __name__ и __qualname__')
print("Класс Aplha, поле __name__:", Alpha.__name__)
print("Класс Aplha, поле __qualname__:", Alpha.__qualname__)

print("Класс Aplha.Bravo, поле __name__:", Alpha.Bravo.__name__)
print("Класс Aplha.Bravo, поле __qualname__:", Alpha.Bravo.__qualname__)

print("Класс Delta, поле __name__:", Delta.__name__)
print("Класс Delta, поле __qualname__:", Delta.__qualname__)
