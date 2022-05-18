class Alpha:
    def hi():
        print("Класс Alpha")


class Bravo:
    def hi():
        print("Класс Bravo")


class Charlie:
    def hi():
        print("Класс Charlie")


class Delta(Alpha):
    pass


class Echo(Delta):
    pass


class Foxtrot(Bravo, Alpha):
    pass


class Golf(Foxtrot):
    pass


class Hotel(Echo, Charlie, Golf):
    pass


# Вызываем функции классов
Echo.hi()
Golf.hi()
Hotel.hi()
print(Hotel.__mro__)
