# Создаем класс

class MyClass:
    # Поле класса
    name = "Класс MyClass"

    # Метод для присваивания значыения
    # полю экземпляра класса
    def set(self, n):
        self.nickname = n

    # Метод для отображения значыения
    # поля экзампляра класса
    def get(self):
        print("Значение поля: ", self.nickname)

    # Конструктор
    def __init__(self, n):
        # Полю экземпляра класса
        # Присваивается значение
        self.set(n)
        # Отображается сообщение
        print("Создан экземпляр класса.")
        # Отображается значаение поля экемляра
        self.get()


# Первый экземпляр (переменная green)
green = MyClass("Зеленый")
# Проверям значения поля _name
# Через экзмпляр green
print("Принадлежность :", green.name)

# Второй экземпляр (переменная red)
red = MyClass("Красный")
# Проверяем значнеие поля _name
# через экземпляр red
print("Принадлежность :", red.name, "\n")

# Изменяем значнеие поля _name
# через экземпляр green
green.name = "Здесь был Зеленый"

# Проверяем значение поля _name
# через экземпляр red
print("Спрашивает Красный: ", red.name)

# Проверяем значение поля _name
# через экземпляр green
print("Спрашивает Зеленый: ", green.name)

# Изменяем значение поля _name
# через объект класса MyClass
MyClass.name = "Здесь могла быть Ваша реклама!"

# Проверяем значение поля _name
# через экземпляр red
print("Спрашивает Красный: ", red.name)

# Проверяем значение поля _name
# через экземпляр green
print("Спрашивает Зеленый: ", green.name)

# Удаляемя поле _name экземпляра green
del green.name

# Проверяем значение поля _name
# через экземпляр green
print("Спрашивает Зеленый: ", green.name)
