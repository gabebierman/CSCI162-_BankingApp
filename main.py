import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow
from account_model import AccountModel
from account_controller import AccountController


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)

    model = AccountModel()
    controller = AccountController(model, window, ui)

    window.show()
    sys.exit(app.exec())
