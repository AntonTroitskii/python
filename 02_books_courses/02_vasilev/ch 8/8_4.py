def show_me(first, second, *other, **byname):
    print('first ->', first)
    print('second ->', second)
    print('other ->', other)
    print('byname ->', byname)


print('1-й способ вызова функции.')
show_me(10, 20, 30, 40, 50, 60, 70)
print('2-й способ вызова функции.')
show_me(10, 20, 30, 40, 50, 60, 70, third=30, fourth=40)
print('3-й способ вызова функции.')
show_me(10, 20, third=30, fourth=40)
print('4-й способ вызова функции.')
show_me(second=20, first=10)
print('5-й способ вызова функции.')
show_me(first=10, second=20, third=30, fourth=40)
