import math


def solve_deqn(f, x0, y0, x):
    n = 100000
    dx = (x - x0) / n
    x = x0
    y = y0

    for k in range(1, n + 1):
        y = y + dx * f(x, y)
        x = x + dx

    return y


def diff_eqn(x, y):
    return 2 * x - y


def y(x):
    return 2 * (x - 1) + 5 * math.exp(-x)


h = 0.5
for k in range(0, 6):
    x = k * h
    print('Числовое решение:')
    deqn = solve_deqn(diff_eqn, 0, 3, x)
    print('x = ', x, ' -> y(x) =', deqn)
    f = y(x)
    print('x = ', x, ' -> y(x) =', f)
    print('Y(x) - y(x) = ', deqn - f, '(Y(x) - примерное решение)')
