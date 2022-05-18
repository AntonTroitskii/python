import time


class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def now():
        t = time.localtime()
        return Date(t.tm_year, t.tm_mon, t.tm_day)

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


# Несколько примеров создания экземпляров
a = Date(1967, 4, 9)
b = Date.now()  # Вызовет статический метод now()
c = Date.tomorrow()  # Вызовет статический метод tomorrow()

a = Date.now()
