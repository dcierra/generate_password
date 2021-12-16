from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from random import choice


class Ui_GeneratePassword(object):
    def setupUi(self, GeneratePassword):
        GeneratePassword.setObjectName("GeneratePassword")
        GeneratePassword.resize(400, 200)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        GeneratePassword.setFont(font)
        GeneratePassword.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(GeneratePassword)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_generate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_generate.setGeometry(QtCore.QRect(229, 140, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.btn_generate.setFont(font)
        self.btn_generate.setStyleSheet("background-color: rgb(255, 251, 55);")
        self.btn_generate.setObjectName("btn_generate")
        self.checkBox_numbers = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_numbers.setGeometry(QtCore.QRect(0, 60, 211, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_numbers.setFont(font)
        self.checkBox_numbers.setStyleSheet("background-color: rgb(217, 255, 212);")
        self.checkBox_numbers.setObjectName("checkBox_numbers")
        self.checkBox_lowercaseLetters = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_lowercaseLetters.setGeometry(QtCore.QRect(0, 100, 211, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_lowercaseLetters.setFont(font)
        self.checkBox_lowercaseLetters.setStyleSheet("background-color: rgb(217, 255, 212);")
        self.checkBox_lowercaseLetters.setObjectName("checkBox_lowercaseLetters")
        self.checkBox_uppercaseLetters = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_uppercaseLetters.setGeometry(QtCore.QRect(0, 140, 211, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_uppercaseLetters.setFont(font)
        self.checkBox_uppercaseLetters.setStyleSheet("background-color: rgb(217, 255, 212);")
        self.checkBox_uppercaseLetters.setObjectName("checkBox_uppercaseLetters")
        self.checkBox_punctuation = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_punctuation.setGeometry(QtCore.QRect(0, 175, 211, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_punctuation.setFont(font)
        self.checkBox_punctuation.setStyleSheet("background-color: rgb(217, 255, 212);")
        self.checkBox_punctuation.setObjectName("checkBox_punctuation")
        self.lenght_password = QtWidgets.QSpinBox(self.centralwidget)
        self.lenght_password.setGeometry(QtCore.QRect(250, 90, 111, 25))
        self.lenght_password.setStyleSheet("background-color: rgb(255, 251, 130);")
        self.lenght_password.setObjectName("lenght_password")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 60, 141, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 251, 130);")
        self.label_2.setObjectName("label_2")
        self.output_password = QtWidgets.QTextEdit(self.centralwidget)
        self.output_password.setGeometry(QtCore.QRect(0, 0, 400, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.output_password.setFont(font)
        self.output_password.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255, 255, 255);")
        self.output_password.setObjectName("output_password")
        GeneratePassword.setCentralWidget(self.centralwidget)

        self.retranslateUi(GeneratePassword)
        QtCore.QMetaObject.connectSlotsByName(GeneratePassword)

        self.show_result()
        self.gen_pas = []

        self.error = QMessageBox()


    def retranslateUi(self, GeneratePassword):
        _translate = QtCore.QCoreApplication.translate
        GeneratePassword.setWindowTitle(_translate("GeneratePassword", "Генератор паролей"))
        self.btn_generate.setText(_translate("GeneratePassword", "Сгенерировать"))
        self.checkBox_numbers.setText(_translate("GeneratePassword", "Включать цифры"))
        self.checkBox_lowercaseLetters.setText(_translate("GeneratePassword", "Включать строчные буквы"))
        self.checkBox_uppercaseLetters.setText(_translate("GeneratePassword", "Включать прописные буквы"))
        self.checkBox_punctuation.setText(_translate("GeneratePassword", "Включать символы"))
        self.label_2.setText(_translate("GeneratePassword", "Укажите длину пароля:"))


    def show_result(self):
        self.btn_generate.clicked.connect(self.check_checkBox)

    def check_checkBox(self):
        if self.checkBox_numbers.isChecked():
            self.gen_pas.extend('0123456789')
        if self.checkBox_lowercaseLetters.isChecked():
            self.gen_pas.extend('abcdefghijklmnopqrstuvwxyz')
        if self.checkBox_uppercaseLetters.isChecked():
            self.gen_pas.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        if self.checkBox_punctuation.isChecked():
            self.gen_pas.extend('!#$%&*+-=?@^_')

        lenght = int(self.lenght_password.text())
        if lenght > 0 and lenght < 31:
            password = ''
            if not self.gen_pas:
                self.error.setWindowTitle('Ошибка')
                self.error.setText('Выберите хотя бы один пункт')
                self.error.setIcon(QMessageBox.Warning)
                self.error.exec_()
            else:
                for i in range(lenght):
                    password += choice(self.gen_pas)
                self.output_password.setText(f'Пароль: {password}')
                self.gen_pas = []
        else:
            self.error.setWindowTitle('Ошибка')
            self.error.setText('Длина пароля должна быть не меньше 1 и не больше 30')
            self.error.setIcon(QMessageBox.Warning)
            self.error.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GeneratePassword = QtWidgets.QMainWindow()
    ui = Ui_GeneratePassword()
    ui.setupUi(GeneratePassword)
    GeneratePassword.show()
    sys.exit(app.exec_())
