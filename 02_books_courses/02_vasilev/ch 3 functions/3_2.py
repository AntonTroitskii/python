import math


def my_exp(x, n):
    s = 0  # начальное значение суммы раяда
    q = 1  # начальное значение добавки

    for k in range(n + 1):
        s += q
        q *= x / (k + 1)

    return s


x = 50

k_sum = 100

for n in range(k_sum):
    print('n= ', n, '->', my_exp(x, n, ))



