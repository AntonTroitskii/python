def show_me(first, second, *other):
    print("Первый аргумент:", first)
    print('Второй аргумент:', second)

    n = len(other)

    print('Еще осталось ', n, 'аргумента:')

    print(other)


show_me(10, 20, 30, 40, 50)
