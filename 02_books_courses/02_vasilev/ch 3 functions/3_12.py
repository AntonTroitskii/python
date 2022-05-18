def test_vars():
    print('В теле фукнции x =', x)


x = 'глобальная переменная'

test_vars()

print('Вне функции x =', x)
