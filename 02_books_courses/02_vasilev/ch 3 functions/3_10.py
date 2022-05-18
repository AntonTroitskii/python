def my_pow(n):
    return lambda x: x ** n


for n in range(1, 5):
    for x in range(1, 11):
        print(my_pow(n)(x), end=' ')
    print()

f = lambda x=1: 1 / x
print(f())
print(f(2))
