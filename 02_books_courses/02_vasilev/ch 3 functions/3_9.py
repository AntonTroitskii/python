def find_val(f, x):
    print('x=', x, '-> f(x) =', f(x))


my_func = lambda x: 1 / (1 + x ** 2)

find_val(my_func, 2.0)

func1 = lambda x: 1 / x
func2 = lambda x: 1 / x ** 3

for i in range(1, 100, 6):
    print('x=', i, '1/x=', func1(i), '1/x^3=', func2(i))
