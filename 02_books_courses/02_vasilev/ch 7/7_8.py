class Box:

    def __init__(self, widht, height, depth):
        self.width = widht
        self.height = height
        self.depth = depth

    def __call__(self):
        volume = self.width * self.height * self.depth

        print("Объем равен", volume)


obj = Box(10, 20, 30)
obj()
