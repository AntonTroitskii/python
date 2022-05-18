import time


class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def tomorrow():
        t = time.localtime(time.time() + 86400)
        return Date(t.tm_year, t.tm_mon, t.tm_day)

    @classmethod
    def now(cls):
        t = time.localtime()

        # Создать объект соответствующего типа
        return cls(t.tm_year, t.tm_month, t.tm_day)


class EuroDate(Date):
    # Изменена строка преобразования, чтобы обеспечить возможность
    # представления дат в европейском формате
    def __str__(self):
        return "%02d/%02d/%4d" % (self.day, self.month, self.year)


class Times(object):
    factor = 1

    @classmethod
    def mul(cls, x):
        return cls.factor * x


class TwoTimes(Times):
    factor = 2


class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def now(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_day)

    @staticmethod
    def tomorrow():
        t = time.localtime(time.time() + 86400)
        return Date(t.tm_year, t.tm_mon, t.tm_day)

    @classmethod
    def now(cls):
        t = time.localtime()

        # Создать объект соответствующего типа
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


class EuroDate(Date):
    # Изменена строка преобразования, чтобы обеспечить возможность
    # представления дат в европейском формате
    def __str__(self):
        return "%02d/%02d/%4d" % (self.day, self.month, self.year)


x = TwoTimes.mul(4)  # Вызовет Times.mul(TwoTimes, 4) -> 8
print(x)

a = Date.now()  # Вызовет Date.now(Date) и вернет Date
b = EuroDate.now()  # Вызовет Date.now(EuroDate) и вернет EuroDate
print(type(a), type(b))
