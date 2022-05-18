x = 100


def test_vars():
    global x, y
    print('В теле функции x = ', x)

    y = 200

    print('В теле функии y = ', y)

    x = 300


test_vars()
print('Вне функции x = ', x)
print('Вне функции y = ', y)
