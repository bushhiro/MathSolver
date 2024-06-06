import os.path

from PyQt5 import QtWidgets, uic

ui_folder = os.path.join("ui")
entry_ui_file, _ = uic.loadUiType(os.path.join(ui_folder, "entry.ui"))
login1_ui_file, _ = uic.loadUiType(os.path.join(ui_folder, "login1.ui"))


class EntryUI(QtWidgets.QMainWindow, entry_ui_file):
    def __init__(self, parent=None):
        super(EntryUI, self).__init__(parent)
        self.setupUi(self)


class LoginUIDialog(QtWidgets.QMainWindow, login1_ui_file):
    def __init__(self, parent=None):
        super(LoginUIDialog, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    entry_ui = EntryUI()
    login1_ui = LoginUIDialog()
    widget_stack = QtWidgets.QStackedWidget()
    widget_stack.addWidget(entry_ui)
    widget_stack.addWidget(login1_ui)
    entry_ui.sign_up_button.clicked.connect(lambda: widget_stack.setCurrentIndex(1))
    widget_stack.show()
    sys.exit(app.exec_())
