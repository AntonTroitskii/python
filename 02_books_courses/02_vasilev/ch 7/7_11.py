class MyClass:
    def __init__(self, txt):
        self.name = txt

    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.name)

    def __index__(self):
        p = self.name.count(" ") + 1
        return p

    def __round__(self):
        self.name = "Сброс значыения"

        return self


txt = "Раз, два, три, чыетрые, пять. "
txt += "\nВышел Зайчик погулять."

obj = MyClass(txt)

print(obj)
print("Количество букву (символов)", len(obj))
print("Количество слов:", obj.__index__())
print("В двоичном коде:", bin(obj))
print("В восьмеричном коде:", oct(obj))
print("В шестнадцетеричном коде:", hex(obj))
print("Выполняем \"Округление\" экземпляра класса:", round(obj))
print("Выводим на печать экземпляр класса:", print(obj))
