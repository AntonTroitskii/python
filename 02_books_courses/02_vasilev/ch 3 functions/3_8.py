def solve(f, x0, n):
    if n == 0:
        return x0
    else:
        return solve(f, f(x0), n - 1)


def eqn(x):
    return (x ** 2 + 5) / 6


def eqn_2(x):
    return (6 * x - 5) ** 0.5


x = solve(eqn, 0, 10)
print('Решение уравнения: x=', x)

x = solve(eqn_2, 3, 10)
print('Решение уравнения: x=', x)
