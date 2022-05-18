def show(a: 'Первый аргумент', b: int = 0) -> None:

    """
    :param a: Первый аргумент
    :param b: Второй аргумент
    :return:
    :rtype: None
    """
    print('a = ', a)
    print('b = ', b)

    return 1


show(10)
show(10, 20)

print('Ввывод show.__doc__')
print(show.__doc__)
print('Ввывод show.__annotations__')
print(show.__annotations__)
annt = show.__annotations__['a']
print('Аргументы a:', annt)
res = show.__annotations__['return']
print('Возвращаемы результат:', res)

# Важно понимать, что наличие аннотациий не влияет на алогиртм выполнения кода функции,
# равно как наличие аннтации для руезльтата функции реально не ограничивает свободу программитса
# в лпане тип возвращаемого функцией значыения.
res = show(10)
print(res)

show(10, 20.0)