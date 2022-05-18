import math


class Vector:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        txt = '<' + str(self.x) + '|'
        txt += str(self.y) + '|'
        txt += str(self.z) + '>'

        return txt

    # obj + x
    def __add__(self, other):
        t = Vector()
        t.x = self.x + other.x
        t.y = self.y + other.y
        t.z = self.z + other.z

        return t

    # x + obj
    def __iadd__(self, other):
        self = self + other
        return self

    # obj * x
    def __mul__(self, other):
        if isinstance(other, Vector):
            x = self.x * other.x
            y = self.y * other.y
            z = self.z * other.z
            res = x + y + z

            return res
        else:
            self.x *= other
            self.y *= other
            self.z *= other

            return self

    # x * obj
    def __rmul__(self, other):

        return self * other

    def __neg__(self):
        t = Vector()

        t.x = -self.x
        t.y = -self.y
        t.z = -self.z

        return t

    # obj - other
    def __sub__(self, other):
        return -other + self

    # obj -= x
    def __isub__(self, other):
        self = self - other

    # other - x
    def __rsub__(self, other):
        return -self + other

    def __abs__(self):
        return math.sqrt(self * self)

    def __truediv__(self, other):
        return self * (1 / other)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return not (self == other)

    # obj < other
    def __lt__(self, other):
        return abs(self) < abs(other)

    # obj > other
    def __gt__(self, other):
        return abs(self) > abs(other)

    # obj <= other
    def __le__(self, other):
        return abs(self) <= abs(other)

    # obj >= other
    def __ge__(self, other):
        return abs(self) >= abs(other)

    # Побитовая инверсия для вектора
    # ~obj
    def __invert__(self):
        self.x = 10 - self.x
        self.y = 10 - self.y
        self.z = 10 - self.z

        return self

    """ Количестово последовательных пререстновок определяется значением числового
        операнда. Направление (влево или вправо) перестановки определяется оператором
        и порядком аргументов. Перестановки влево происходят для команд вида экземпляр<<число и
        число>>экземпляр, а перестановка врпаво выполняется для команд вида экземпляр>> число
        и число>>экземпляр.
    """

    # obj << x
    def __lshift__(self, other):
        for i in range(other):
            self.x, self.y, self.z = self.y, self.z, self.x
        return self

    # other << obj
    def __rlshift__(self, other):
        return self >> other

    # obj >> x
    def __rshift__(self, other):
        for i in range(other):
            self.x, self.y, self.z = self.z, self.x, self.y
        return self

    # x >> obj
    def __rrshift__(self, other):
        return self << other


if __name__ == '__main__':
    pass
