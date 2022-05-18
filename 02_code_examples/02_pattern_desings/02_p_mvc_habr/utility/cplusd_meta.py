"""
Модуль реализации метакласса, необходимого для работы представления.

pyqtWrapperType - метакласс общий для оконных компонентов Qt.
ABCMeta - метакласс для реализации абстрактных суперклассов.

CplusDMeta - метакласс для представления.
"""

# from PySide6.QtCore import pyqtWrapperType
from abc import ABCMeta


#
# class CplusDMeta( pyqtWrapperType, ABCMeta ): pass
class CplusDMeta(ABCMeta):
    pass
