from PyQt5 import QtCore, QtGui, QtWidgets
import random
import sys

class UIMainWindow(object):
    def __init__(self, MainWindow):
        self.correct = 0
        self.easy_correct = 0
        self.medium_correct = 0
        self.hard_correct = 0
        self.current_difficulty = None
        self.current_operator = None
        self.random_answer_str = None
        self.random_answer = None
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
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
        self.line_edit = QtWidgets.QLineEdit(self.central_widget)
        self.hard_question_label = QtWidgets.QLabel(self.frame)
        self.normal_question_label = QtWidgets.QLabel(self.frame)
        self.math_solver_label = QtWidgets.QLabel(self.frame)
        self.solve_label = QtWidgets.QLabel(self.central_widget)
        self.submit_button = QtWidgets.QPushButton(self.central_widget)
        self.username_label = QtWidgets.QLabel(self.frame)
        self.difficulty_label = QtWidgets.QLabel(self.central_widget)
        self.difficulty_combo = QtWidgets.QComboBox(self.central_widget)
        self.operator_label = QtWidgets.QLabel(self.central_widget)
        self.operator_combo = QtWidgets.QComboBox(self.central_widget)

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

        self.solve_label.setGeometry(QtCore.QRect(930, 311, 961, 61))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.solve_label.setFont(font)
        self.solve_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.solve_label.setObjectName("label_7")

        self.submit_button.setGeometry(QtCore.QRect(1045, 678, 361, 111))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.submit_button.setFont(font)
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

        # Difficulty label
        self.difficulty_label.setGeometry(QtCore.QRect(1030, 240, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.difficulty_label.setFont(font)
        self.difficulty_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.difficulty_label.setObjectName("difficultyLabel")

        # Difficulty combo box
        self.difficulty_combo.setGeometry(QtCore.QRect(1190, 240, 200, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.difficulty_combo.setFont(font)
        self.difficulty_combo.setStyleSheet("color: rgb(255, 255, 255);")
        self.difficulty_combo.setObjectName("difficultyCombo")
        self.difficulty_combo.addItems(["Легкий", "Средний", "Сложный"])
        self.difficulty_combo.setCurrentIndex(0)  # Set default to 'Легкий'

        # Operator label
        self.operator_label.setGeometry(QtCore.QRect(1420, 240, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.operator_label.setFont(font)
        self.operator_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.operator_label.setObjectName("operatorLabel")

        # Operator combo box
        self.operator_combo.setGeometry(QtCore.QRect(1580, 240, 200, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.operator_combo.setFont(font)
        self.operator_combo.setStyleSheet("color: rgb(255, 255, 255);")
        self.operator_combo.setObjectName("operatorCombo")
        self.operator_combo.addItems(["+", "-", "*", "/"])
        self.operator_combo.setCurrentIndex(0)  # Set default to '+'

        MainWindow.setCentralWidget(self.central_widget)
        self.build_ui(MainWindow)
        self.build_answer()  # Initialize with the first problem
        self.submit_button.clicked.connect(self.retranslateUi)
        self.difficulty_combo.currentIndexChanged.connect(self.build_answer)  # Regenerate question on difficulty change
        self.operator_combo.currentIndexChanged.connect(self.build_answer)  # Regenerate question on operator change

        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def build_answer(self):
        difficulty_map = {
            0: 'легкий',
            1: 'средний',
            2: 'сложный'
        }
        operator_map = {
            0: '+',
            1: '-',
            2: '*',
            3: '/'
        }

        difficulty_index = self.difficulty_combo.currentIndex()
        operator_index = self.operator_combo.currentIndex()
        self.current_difficulty = difficulty_map[difficulty_index]
        self.current_operator = operator_map[operator_index]

        def generate_example(difficulty, oper):
            if difficulty == 'легкий':
                a1 = random.randint(0, 10)
                a2 = random.randint(0, 10)
                variables = [a1, a2]
            elif difficulty == 'средний':
                a1 = random.randint(10, 100)
                a2 = random.randint(10, 100)
                a3 = random.randint(10, 100)
                variables = [a1, a2, a3]
            else:  # 'сложный'
                a1 = random.randint(100, 1000)
                a2 = random.randint(100, 1000)
                a3 = random.randint(100, 1000)
                a4 = random.randint(100, 1000)
                variables = [a1, a2, a3, a4]

            if oper == '/':
                if a2 == 0:
                    return generate_example(difficulty, oper)
                else:
                    result = round(a1 / a2, 2)
            elif oper == '+':
                result = sum(variables)
            elif oper == '-':
                result = variables[0]
                for var in variables[1:]:
                    result -= var
            else:  # for '*'
                result = 1
                for var in variables:
                    result *= var

            return result, variables

        self.random_answer, variables = generate_example(self.current_difficulty, self.current_operator)

        self.random_answer_str = ' '.join(f'{var} {self.current_operator}' for var in variables[:-1]) + f' {variables[-1]} = ?'

        self.solve_label.setText(self.translate("MainWindow", self.random_answer_str))

    def retranslateUi(self):
        user_answer = self.line_edit.text()
        try:
            if float(user_answer) == self.random_answer:
                self.correct += 1

                # Update the correct counter based on current difficulty
                if self.current_difficulty == 'легкий':
                    self.easy_correct += 1
                elif self.current_difficulty == 'средний':
                    self.medium_correct += 1
                elif self.current_difficulty == 'сложный':
                    self.hard_correct += 1

                self.completed_label.setText(self.translate("MainWindow", f"Выполнено примеров: {self.correct}"))
                self.update_difficulty_labels()
            else:
                self.completed_label.setText(self.translate("MainWindow", f"Правильный ответ: {self.random_answer}"))
        except ValueError:
            self.completed_label.setText(self.translate("MainWindow", "Некорректный ответ"))

        self.line_edit.clear()  # Clear the input field after submitting the answer
        self.build_answer()

    def update_difficulty_labels(self):
        # Update the labels for the number of solved problems based on difficulty
        self.easy_question_label.setText(self.translate("MainWindow", f"Легких: {self.easy_correct}"))
        self.normal_question_label.setText(self.translate("MainWindow", f"Средних: {self.medium_correct}"))
        self.hard_question_label.setText(self.translate("MainWindow", f"Сложных: {self.hard_correct}"))

    def build_ui(self, MainWindow):
        MainWindow.setWindowTitle(self.translate("MainWindow", "Math Solver"))
        self.math_solver_label.setText(self.translate("MainWindow", "MathSolver"))
        self.easy_question_label.setText(self.translate("MainWindow", "Легких: 0"))
        self.username_label.setText(self.translate("MainWindow", "Юзернейм:"))
        self.completed_label.setText(self.translate("MainWindow", "Выполнено примеров:"))
        self.hard_question_label.setText(self.translate("MainWindow", "Сложных: 0"))
        self.normal_question_label.setText(self.translate("MainWindow", "Средних: 0"))
        self.exit_button.setText(self.translate("MainWindow", "Выход"))
        self.solve_label.setText(self.translate("MainWindow", "Решите пример:"))
        self.submit_button.setText(self.translate("MainWindow", "Ввести ответ"))
        self.answer_label.setText(self.translate("MainWindow", ""))
        self.answer_label_2.setText(self.translate("MainWindow", "Ответ:"))
        self.difficulty_label.setText(self.translate("MainWindow", "Сложность:"))
        self.operator_label.setText(self.translate("MainWindow", "Оператор:"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UIMainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
