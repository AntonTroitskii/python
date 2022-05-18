class A():
    def __init__(self):
        self.__X = 3    # Будет изменено на self._A__X
                        # Будет изменено на _A__spam()

    def __spam(self):
        pass            # Вызовет только метод A.__spam()

    def bar(self):
        self.__spam()


class B(A):
    def __init__(self):
        A.__init__(self)
        self.__X = 37       # Будет изменено на self._B__X

    def __spam(self):       # Будет изменено на _B__spam()
        pass
