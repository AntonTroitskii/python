class MyClass:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __setattr__(self, key, value):
        if key == 'name':
            self.__dict__[key] = value
        else:
            print('Операция не завершена!')

    # Вызывается при обращении к несущестующему атрибуту
    def __getattr__(self, item):
        return 'Такого поля нет!'

    def __delattr__(self, item):
        print('Удалять поля запрещено!')


obj = MyClass('Исходное значение')
print(obj)
obj.name = 'Новое значение'
print(obj)

obj.bumber = 100
print('print(obj.number)')
print(obj.number)
print('print(obj.name)')
print(obj.name, '\n')

del obj.name
print(obj)
