def factor(mode=True):
    def sf(n): # single factorial
        s = 1
        i = n
        while i > 1:
            s *= i
            i -= 1
        return s

    def df(n): # double factorial
        s = 1
        i = n
        while i > 1:
            s *= i
            i -= 2
        return s

    if mode:
        return sf
    else:
        return df


print('5! =', factor()(5))
print('5! =', factor(True)(5))

print('5!! =', factor(False)(5))
