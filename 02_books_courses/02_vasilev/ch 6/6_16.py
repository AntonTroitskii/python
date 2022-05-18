class MyClass:

    def __init__(self, arg, nums=None):
        if type(arg) == MyClass:
            self.name = arg.name[:]
            self.nums = arg.nums[:]
        else:
            self.name = arg
            self.nums = nums

    def show(self):
        print("_name ->", self.name)
        print("nums -> ", self.nums)


x = MyClass("Python", [1, 2, 3])
print("x = MyClass(\"Python\", [1, 2, 3])")
print("Экземпляр x:")
x.show()
y = MyClass(x)
y.show()

print("Поля экземпляра x изменяются!")
x.name = "Java"
x.nums[0] = 0
print("Экземпляр x:")
x.show()
print("Экземпляр y:")
y.show()

print()
x = MyClass("Python", [[1, 2], 3])
print("x = MyClass(\"Python\", [[1, 2], 3])")
print("Экземпляр x:")
x.show()
y = MyClass(x)
y.show()

print("Поля экземпляра x изменяются!")
x.name = "Java"
x.nums[0][0] = 0
print("Экземпляр x:")
x.show()
print("Экземпляр y:")
y.show()
