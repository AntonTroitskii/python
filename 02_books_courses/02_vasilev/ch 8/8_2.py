def show_me(*args):
    i = 0
    print('Аргументы(ы) функции:')
    for s in args:
        i += 1
        print(str(i) + '-й \'аргумент:\'', s)
    print('Выполнение функции завершено.')


show_me()
show_me(100)

nums = [10, 55, 2 + 3j, 0.123]
show_me(*nums)

show_me('Python', 'Java')