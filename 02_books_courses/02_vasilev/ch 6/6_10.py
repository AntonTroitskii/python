class MyClass:
    def say(self):
        print("Всем привет!")


obj = MyClass()  # Создаем экземпляр класса
obj.say()  # Вызываем метод экземпляра. Аргументов нет.

MyClass.say(obj)  # вызываем фукнцию класса. Аргумент - экземпляр класса

# вызываем фукнцию класса. Аргумент - просто текстЫ
MyClass.say("Какой-то текст")