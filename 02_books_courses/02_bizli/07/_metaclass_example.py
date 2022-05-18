class_name = "Foo"  # Имя класса
class_parents = (object,)  # Базовые классы
class_body = """ # Тело класса
def __init__(self, x):
    self.x = x

def blah(self):
    print('Hello World')
"""

# globals = {}
class_dict = {}

# Выполнить тело класса с использованием локального словаря class_dict
exec(class_body, globals(), class_dict)

print(class_dict)
Foo = type(class_name, class_parents, class_dict)

# Созадние и использование объекта Класса Foo
foo = Foo(1)
foo.blah()
