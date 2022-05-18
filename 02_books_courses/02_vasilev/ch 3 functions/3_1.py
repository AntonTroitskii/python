def your_name():
    print('Добрый день!')

    name = input('Как Вкс зовут? ')
    return name


def say_hello(txt):
    print('Здрауствуйте,', txt + '!')


my_name = your_name()
say_hello(my_name)
