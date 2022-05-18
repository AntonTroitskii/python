from math import exp, sin, cos, tan


def F(f):
    res = lambda x: exp(-f(x) ** 2)

    return res


def Q(f):
    # Внутренная функция
    def q(x):
        return tan(f(x))

    return q


# Функция с декаратором
@F  # Декоратор
def f(x):
    return sin(x)


# Функция с декаратором
@F  # Декоратор
def g(x):
    return cos(x)


# Функция с двумя декараторам
@Q
@F
def h(x):
    return x


n = 5

print('Функция f():')

for i in range(n + 1):
    z = i / n
    print(f(z), '->', exp(-sin(z) ** 2))

print('Функция g():')
for i in range(n + 1):
    z = i / n
    print(g(z), '->', exp(-cos(z) ** 2))

print('Функция h():')
for i in range(n + 1):
    z = i / n
    print(h(z), '->', tan(exp(-z ** 2)))
