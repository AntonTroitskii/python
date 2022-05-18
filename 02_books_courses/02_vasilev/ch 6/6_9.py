# Создаем класс
class MyClass:
    pass


# Создаем экземпляр A
A = MyClass()

# Создаем экземпляр B
B = MyClass()

# экземпляру A добавляем
# поле first
A.first = "Экземпляр A"

# экземпляру B добавляем
# поле second
B.second = "Экземпляр B"

# Класс MyClass добалвяем
# поле total
MyClass.total = "Класс MyClass"

# Проверяем доступ к полям total и
# first через ссылку на экземпляр A
print(A.total, "->", A.first)

# Проверяем доступ к полю second
# через сслыку на экземпляр A
try:
    # Если поле second есть
    print(A.second)
# Если такого поля нет
except AttributeError:
    print("Такого поля у экзмепляра A нет!")

# проверяем доступ к полям total и
# second через ссылку на экземпляр B
print(B.total, "->", B.second)

# проверяем доступ к полю first
# через ссылку на экземпляр B
try:
    # Если поле есть
    print(B.first)
# Если поля нет
except AttributeError:
    print("Такого поля у экзмепляра B нет!")

# удаляем поле total класса MyClass
del MyClass.total
# Проверяем доустп к полю total
# через ссылку на экземпляр A
try:
    # Если поле есть
    print(A.total)

# Если поля нет
except AttributeError:
    print("Такого поля нет!")

# проверяем доступ к полю total
# через ссылку на экземпляр B
try:
    # Если поле есть
    print(B.total)

# Если поля нет
except AttributeError:
    print("Такого поля нет!")

# удаляем поле first экземляра A
del A.first
# проверяем доступ к полю first
# через ссылку на экземпляр A
try:
    print(A.first)
except AttributeError:
    print("Такого поля у экзмепляра A нет!")
