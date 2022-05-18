class MyClass:
    Nmax = 5

    def __init__(self):
        n = MyClass.Nmax
        self.nums = [0 for i in range(n)]

    def __str__(self):
        txt = "| "
        for s in self.nums:
            txt += " " + str(s) + " |"
        return txt

    def index_nums(self, key):
        return key % len(self.nums)

    def __setitem__(self, key, value):
        k = self.index_nums(key)
        self.nums[k] = value

    def __getitem__(self, item):
        k = self.index_nums(item)
        return self.nums[k]

    def __delitem__(self, key):
        k = self.index_nums(key)
        self.nums[k] = '*'


obj = MyClass()

print(obj)

obj[0] = 100
obj[2] = -3
obj[24] = 123

print(obj)
print('Элемет с индексом 4:', obj[4])
print('Элемет с индексом 7:', obj[7])

del obj[0]
del obj[9]

print(obj)
