class MyClass:
    def __setattr__(self, key, value):
        print('Выполняется метод __setattr__():')
        txt = '*\tПолю ' + str(key)
        txt += ' присваивается значение ' + str(value)
        print(txt)
        self.__dict__[key] = value
        print('Метод __setattr__() выполнен.')

    def __getattribute__(self, item):
        print('Выполняется метод __getattribute__():')
        txt = '*\tСчитывается значения поля \'' + str(item) + '\''
        print(txt)

        try:
            res = object.__getattribute__(self, item)
        except AttributeError:
            res = 'У экземпляра поля \'' + str(item) + '\' нет!'
        print('Метод __getattibute__() завершает работу.')
        return res

    def __delattr__(self, item):
        print('Выполняется мтеод __delattr__():')
        txt = '*\tУдаляется поле \'' + str(item) + '\''
        print(txt)
        try:
            del self.__dict__[item]
        except KeyError:
            print('Нельзя удалить поле ' + str(item))
        print('Метод __delattr__() выполнен.')


obj = MyClass()

print('obj.name = \'Python\'')
obj.name = 'Python'
print('\nprint(\'Значение поля name:\', obj.name)')
print('Значение поля name:', obj.name)

print('\ndel obj.name')
del obj.name

print('\nprint(obj.name)')
print(obj.name)

print('\ndel obj.name')
del obj.name
