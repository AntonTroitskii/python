from abc import ABCMeta, abstractmethod


class CplusDObserver():
    """
    Абстрактный суперкласс для всех наблюдателей.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def modelIsChanged(self):
        """
        Метод который будет вызван у наблюдателя при изменении модели.
        """
        pass
