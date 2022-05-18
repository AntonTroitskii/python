class Foo():
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Имя должно быть строкой!")
        self.__name = value

    @name.deleter
    def name(self):
        raise TypeError("Невозможно удалить атрибут name")

    def spam(self, x):
        print("%s %s", self.name, x)


f = Foo('Гвидо')
s = f.spam
s("test")  # вызов метода с помощью оператора ()

f = Foo("Гвидо")
n = f.name  # вызовет f.name() – вернет функцию
f.name = "Монти"  # вызовет метод изменения name(f,”Монти”)
f.name = 45  # вызовет метод изменения name(f,45) -> TypeError
del f.name  # вызовет метод удаления name(f) -> TypeError
