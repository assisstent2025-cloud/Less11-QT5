import sys
from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Калькулятор')
        self.setGeometry(100, 100, 300, 400)

        layout = QVBoxLayout()

        self.result_label = QLabel("Результат сложения")
        self.result_label1 = QLabel("Результат вычитания")
        self.result_label2 = QLabel("Результат умножения")
        self.result_label3 = QLabel("Результат деления")

        for i in [self.result_label, self.result_label1, self.result_label2, self.result_label3]:
            layout.addWidget(i)

        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Введите")
        layout.addWidget(self.input_field)

        self.input_field1 = QLineEdit(self)
        self.input_field1.setPlaceholderText("Введите")
        layout.addWidget(self.input_field1)

        self.btn_plus = QPushButton("Плюс", self)
        self.btn_plus.clicked.connect(self.plus)
        layout.addWidget(self.btn_plus)

        self.btn_minus = QPushButton("Минус", self)
        self.btn_minus.clicked.connect(self.minus)
        layout.addWidget(self.btn_minus)

        self.btn_mult = QPushButton("Умножение", self)
        self.btn_mult.clicked.connect(self.mult)
        layout.addWidget(self.btn_mult)

        self.btn_div = QPushButton("Деление", self)
        self.btn_div.clicked.connect(self.div)
        layout.addWidget(self.btn_div)

        self.resetButton = QPushButton("Сброс", self)
        self.resetButton.clicked.connect(self.resset)
        layout.addWidget(self.resetButton)

        self.exit_button = QPushButton("Выход", self)
        self.exit_button.clicked.connect(QApplication.instance().quit)
        layout.addWidget(self.exit_button)

        self.setLayout(layout)

    def get_numbers(self):

        num1 = float(self.input_field.text())
        num2 = float(self.input_field1.text())
        return num1, num2

    def plus(self):
        try:
            n1, n2 = self.get_numbers()
            self.result_label.setText(f"Результат: {n1 + n2}")
            self.result_label.setStyleSheet("color: green;")
        except ValueError:
            self.result_label.setText("Ошибка: введите числа")
            self.result_label.setStyleSheet("color: red;")

    def minus(self):
        try:
            n1, n2 = self.get_numbers()
            self.result_label1.setText(f"Результат: {n1 - n2}")
            self.result_label1.setStyleSheet("color: green;")
        except ValueError:
            self.result_label1.setText("Ошибка: введите числа!")
            self.result_label1.setStyleSheet("color: red;")

    def mult(self):
        try:
            n1, n2 = self.get_numbers()
            self.result_label2.setText(f"Результат: {n1 * n2}")
            self.result_label2.setStyleSheet("color: green;")
        except ValueError:
            self.result_label2.setText("Ошибка: введите числа!")
            self.result_label2.setStyleSheet("color: red;")

    def div(self):
        try:
            n1, n2 = self.get_numbers()
            if n2 == 0:
                raise ZeroDivisionError
            self.result_label3.setText(f"Результат: {n1 / n2}")
            self.result_label3.setStyleSheet("color: green;")
        except ZeroDivisionError:
            self.result_label3.setText("Ошибка: деление на ноль")
            self.result_label3.setStyleSheet("color: red;")
        except ValueError:
            self.result_label3.setText("Ошибка: введите числа")
            self.result_label3.setStyleSheet("color: red;")

    def resset(self):
        self.input_field.clear()
        self.input_field1.clear()
        self.result_label.setText("Результат")
        self.result_label1.setText("Результат")
        self.result_label2.setText("Результат")
        self.result_label3.setText("Результат")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
