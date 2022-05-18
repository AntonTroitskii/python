def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def dfactorial(n):
    if n == 1 or n == 2:
        return n
    else:
        return n * dfactorial(n - 2)


def factor(mode=True):
    return factorial if mode else dfactorial


print('5! =', factor()(5))
print('5! =', factor(True)(5))

print('5!! =', factor(False)(5))
