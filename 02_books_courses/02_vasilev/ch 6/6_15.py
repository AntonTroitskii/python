class CompNum:

    def __init__(self, x=0, y=0):
        if type(x) == CompNum:
            self.Re = x.Re
            self.Im = x.Im
        else:
            self.Re = x
            self.Im = y

    def show(self):
        print("Re = ", self.Re)
        print("Im = ", self.Im)


a = CompNum(1, 2)
b = CompNum(a)
print("Экземпляр a:")
a.show()

print("Экземпляр b:")
b.show()

a.Re = 10
a.Im = 20
print("Экземпляр a:")
a.show()
print("Экземпляр b:")
b.show()
