import time
from PyQt5 import QtWidgets
from windows import *
import sys


def login():
    print("Ф")


def show_regWindow():
    global MainWindow

    for widget in current_window.widgets:
        widget.deleteLater()

    reg_window = RegWindow()
    MainWindow = QtWidgets.QMainWindow()
    reg_window.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.update()


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
login_window = LoginWindow()
login_window.setupUi(MainWindow)

current_window = login_window

login_button = login_window.pushButton
login_button.clicked.connect(login)

reg_button = login_window.pushButton_2
reg_button.clicked.connect(show_regWindow)

MainWindow.show()
sys.exit(app.exec_())
