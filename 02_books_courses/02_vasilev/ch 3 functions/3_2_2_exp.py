import math

import numpy as np


def my_exp_comparison(x, res, er, stat=False):
    k = 0
    q = 1
    s = q

    while abs(res - s) > er and q > 1e-323:
        k += 1
        q *= x / (k)
        s += q
        if stat:
            print(k, abs(res - s), q, s, res)
        if k > 1000:
            break
    return k, s


def exp_comparison(x, er, stat=False):
    exp = math.exp(x)
    k, s = my_exp_comparison(x, exp, er, stat)
    print('x = {}, Членов в ряде: {}, Сумма: {}, Значение exp(x) = {}'.format(x, k, s, exp))


def print_evaluation_stat(er, stat=False):
    for x in np.linspace(0, 25, 6):
        exp_comparison(x, er, stat,)


for er in [1e-0, 1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6]:
    print('er=', er)
    print_evaluation_stat(er)

# exp_comparison(25, 1e-5, True)
