# Класс с конструктором и деструктором

class MyClass:
    # Конструктор
    def __init__(self):
        print("Всем привет!")

    # Деструктор
    def __del__(self):
        print("Все пока!")

print("Проверяем работу деструктора.")
obj = MyClass()
print("Экзепляр класса созадн. Удаяем его.")
# Удаляем эксземпляр класса
del obj
print("Выполнение программы завершено.")