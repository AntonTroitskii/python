class BoxSize():
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def volume(self):
        return self.width & self.height * self.depth

    def show(self):
        print("Размер и объем объем ящика:")
        print("Ширина:", self.width)
        print("Высота", self.height)
        print("Глубина", self.depth)
        print("Объем:", self.volume())


class BoxParams:
    def __init__(self, weight, color):
        self.weight = weight
        self.color = color

    def show(self):
        print("Дополнительные парамеры ящика:")
        print("Вес (масса):", self.weight)
        print("Цвет:", self.color)


class Box(BoxSize, BoxParams):

    def __init__(self, width, height, depth, weight, color):
        BoxSize.__init__(self, width, height, depth)
        BoxParams.__init__(self, weight, color)
        self.show()

    def show(self):
        BoxSize.show(self)
        BoxParams.show(self)


obj = Box(10, 20, 30, 5, 'зеленый')
