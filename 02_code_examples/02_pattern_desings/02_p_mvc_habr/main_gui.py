import sys

from PySide6.QtWidgets import QApplication

from controller.cplusd_controller import CplusDController
from model.cplusd_model import CplusDModel


def main():
    app = QApplication(sys.argv)

    # создаём модель
    model = CplusDModel()

    # создаём контроллер и передаём ему ссылку на модель
    controller_ = CplusDController(model)

    app.exec()


if __name__ == '__main__':
    sys.exit(main())
