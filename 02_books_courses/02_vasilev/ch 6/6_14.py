from copy import copy, deepcopy

class MyClass:
    def __init__(self, name, nums):
        self.name = name
        self.nums = nums

    def show(self):
        print("_name ->", self.name)
        print("nums ->", self.nums)


x = MyClass("Python", [1, 2, 3])
print("Экземпляр x:")
x.show()

y=copy(x)
z=deepcopy(x)
print("Экземпляр y:")
y.show()
print("Экземпляр Z:")
z.show()
print("Поля экземпляра x изменяются!")
x.name = "Java"
x.nums[0] = 0

print("Экземпляр x:")
x.show()
print("Экземпляр y:")
y.show()
print("Экземпляр Z:")
z.show()
