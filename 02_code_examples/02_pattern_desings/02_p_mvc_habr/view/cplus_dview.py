from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QMainWindow

from utility.cplusd_meta import CplusDMeta
from utility.cplusd_observer import CplusDObserver
from view.mainwindow import Ui_MainWindow


class CplusDView(QMainWindow, CplusDObserver):
    """
    Класс отвечающий за визуальное представление CplusDModel.
    """
    __metaclass__ = CplusDMeta

    def __init__(self, inController, inModel, parent=None):
        """
        Конструктор принимает ссылки на модель и контроллер.
        """
        # super(QMainWindow, self).__init__(parent)
        super(QMainWindow, self).__init__(parent)
        self.mController = inController
        self.mModel = inModel

        # подключаем визуальное представление
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # регистрируем представление в качестве наблюдателя
        self.mModel.addObserver(self)

        # устанавливаем валидаторы полей ввода данных
        self.ui.le_c.setValidator(QDoubleValidator())
        self.ui.le_d.setValidator(QDoubleValidator())

        # связываем событие завершения редактирования с методом контроллера
        self.ui.le_c.editingFinished(self.mController.setC())
        # self.connect(self.ui.le_c, SIGNAL("editingFinished()"),
        #              self.mController.setC)
        self.ui.le_d.editingFinished(self.mController.setD)
        # self.connect(self.ui.le_d, SIGNAL("editingFinished()"),
        #              self.mController.setD)

    def modelIsChanged(self):
        """
        Метод вызывается при изменении модели.
        Запрашивает и отображает значение суммы.
        """
        sum = str(self.mModel.sum)
        self.ui.le_result.setText(sum)
