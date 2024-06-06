from PyQt5 import QtCore, QtGui, QtWidgets
import random
import sys


class UIMainWindow(object):
    def __init__(self, MainWindow):

        self.correct = 0
        self.random_answer_str = None
        self.random_answer = None
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)  # -*- coding: utf-8 -*-

        MainWindow.setMinimumSize(QtCore.QSize(1920, 1080))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        MainWindow.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.translate = QtCore.QCoreApplication.translate

        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.frame = QtWidgets.QFrame(self.central_widget)

        self.answer_label = QtWidgets.QLabel(self.central_widget)
        self.answer_label_2 = QtWidgets.QLabel(self.central_widget)
        self.completed_label = QtWidgets.QLabel(self.frame)
        self.easy_question_label = QtWidgets.QLabel(self.frame)
        self.exit_button = QtWidgets.QPushButton(self.frame)
        self.line_edit = QtWidgets.QLineEdit(self.central_widget)  ###кнопка
        self.hard_question_label = QtWidgets.QLabel(self.frame)
        self.normal_question_label = QtWidgets.QLabel(self.frame)
        self.math_solver_label = QtWidgets.QLabel(self.frame)
        self.solve_label = QtWidgets.QLabel(self.central_widget)
        self.submit_button = QtWidgets.QPushButton(self.central_widget)
        self.username_label = QtWidgets.QLabel(self.frame)

        self.setup_ui(MainWindow)

    def setup_ui(self, MainWindow):

        self.central_widget.setObjectName("centralwidget")
        self.frame.setGeometry(QtCore.QRect(0, 0, 531, 1081))
        self.frame.setStyleSheet("background-color: rgb(86, 86, 86)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.math_solver_label.setGeometry(QtCore.QRect(50, 50, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.math_solver_label.setFont(font)
        self.math_solver_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.math_solver_label.setObjectName("label")
        self.easy_question_label.setGeometry(QtCore.QRect(50, 282, 461, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.easy_question_label.setFont(font)
        self.easy_question_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.easy_question_label.setObjectName("label_2")
        self.username_label.setGeometry(QtCore.QRect(50, 125, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.username_label.setFont(font)
        self.username_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.username_label.setObjectName("label_3")

        self.completed_label.setGeometry(QtCore.QRect(50, 200, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.completed_label.setFont(font)
        self.completed_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.completed_label.setObjectName("label_4")

        self.hard_question_label.setGeometry(QtCore.QRect(50, 425, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.hard_question_label.setFont(font)
        self.hard_question_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.hard_question_label.setObjectName("label_5")

        self.normal_question_label.setGeometry(QtCore.QRect(50, 346, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.normal_question_label.setFont(font)
        self.normal_question_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.normal_question_label.setObjectName("label_6")

        self.exit_button.setGeometry(QtCore.QRect(50, 982, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.exit_button.setFont(font)
        self.exit_button.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(167,167,167)")
        self.exit_button.setObjectName("pushButton_4")

        self.solve_label.setGeometry(QtCore.QRect(1030, 311, 391, 61))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.solve_label.setFont(font)
        self.solve_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.solve_label.setObjectName("label_7")

        self.submit_button.setGeometry(QtCore.QRect(1045, 678, 361, 111))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.submit_button.setFont(font)  ###кнопка ответа
        self.submit_button.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(167,167,167)")
        self.submit_button.setObjectName("pushButton")

        self.answer_label.setGeometry(QtCore.QRect(810, 429, 825, 61))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.answer_label.setFont(font)
        self.answer_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.answer_label.setAlignment(QtCore.Qt.AlignCenter)
        self.answer_label.setObjectName("label_8")

        self.answer_label_2.setGeometry(QtCore.QRect(940, 550, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.answer_label_2.setFont(font)
        self.answer_label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.answer_label_2.setObjectName("label_9")

        self.line_edit.setGeometry(QtCore.QRect(1111, 550, 411, 57))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.line_edit.setFont(font)
        self.line_edit.setStyleSheet("color: rgb(255, 255, 255);")
        self.line_edit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.central_widget)
        self.build_ui(MainWindow)
        self.build_answer()
        self.submit_button.clicked.connect(self.retranslateUi)
        # def myFunction(self):
        #    global username
        #    username = self.lineEdit.text()
        # self.pushButton.clicked.connect(self.myFunction)

        # self.pushButton.clicked.connect(self.username = self.lineEdit.text())

        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def build_answer(self):
        a1 = random.randint(0, 100)
        a2 = random.randint(0, 100)
        operation = random.choice(['+', '-', '*', '/'])
        self.random_answer_str = f'{a1} {operation} {a2}'
        match operation:
            case '+':
                self.random_answer = a1 + a2
            case '-':
                self.random_answer = a1 - a2
            case '*':
                self.random_answer = a1 * a2
            case '/':
                self.random_answer = round(a1 / a2, 2)
    def retranslateUi(self):

        user_answer = self.line_edit.text()
        print(user_answer)

        if str(self.random_answer) == user_answer:
            self.correct += 1
            # self.submit_button.setText(self.translate("MainWindow", "Вы решили правильно!"))
            self.completed_label.setText(self.translate("MainWindow", f"Выполнено примеров: {self.correct}"))
            print("Вы решили правильно!")
        else:
            # self.submit_button.setText(self.translate("MainWindow", f"Вы решили неправильно! ({self.random_answer})"))
            print(f"Вы решили неправильно! ({self.random_answer})")
        self.build_answer()
        self.answer_label.setText(self.translate("MainWindow", self.random_answer_str))

    def build_ui(self, MainWindow):

        MainWindow.setWindowTitle(self.translate("MainWindow", "MainWindow"))
        self.math_solver_label.setText(self.translate("MainWindow", "MathSolver"))
        self.easy_question_label.setText(self.translate("MainWindow", "Легких: 0"))
        self.username_label.setText(self.translate("MainWindow", "Юзернейм:"))
        self.completed_label.setText(self.translate("MainWindow", "Выполнено примеров:"))
        self.hard_question_label.setText(self.translate("MainWindow", "Сложных: 0"))
        self.normal_question_label.setText(self.translate("MainWindow", "Средних: 0"))
        self.exit_button.setText(self.translate("MainWindow", "Выход"))
        self.solve_label.setText(self.translate("MainWindow", "Решите пример:"))
        self.submit_button.setText(self.translate("MainWindow", "Ввести ответ"))
        self.answer_label.setText(self.translate("MainWindow", self.random_answer_str))
        self.answer_label_2.setText(self.translate("MainWindow", "Ответ2:"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UIMainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
