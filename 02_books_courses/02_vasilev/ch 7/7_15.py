class Adder:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        txt = 'Значение поля number = '
        txt += str(self.number)
        return txt

    def __add__(self, other):
        if isinstance(other, Adder):
            number = self.number + other.number
        elif isinstance(other, int) or isinstance(other, float):
            number = self.number + other
        return Adder(number)


a = Adder(10)
b = a + 5
print(a)
print(b)

c = Adder(15)
d = Adder(20)
e = c + d
print(c)
print(d)
print(e)
