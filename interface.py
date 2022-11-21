from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QLineEdit
from PyQt5 import QtCore
import sys
import os

class Interface(QMainWindow):
    def __init__(self):
        super(Interface, self).__init__()

        self.setWindowTitle("Lab 3")
        # # self.setGeometry(300, 300, 400, 300)
        # self.setGeometry(0, 0, 650, 400)
        self.move(700, 300)
        self.resize(600, 500)

        # self.new_text = QtWidgets.QLabel("ss", self)
        # self.w_text = QLineEdit(self)

        self.text = QtWidgets.QLabel("Программа", self)
        self.text.move(170, 50)
        # self.text.setAlignment(QtCore.Qt.AlignLeft)
        self.text.adjustSize()

        self.button1 = QtWidgets.QPushButton("Аннотация", self)
        self.button1.move(78, 300)
        self.button1.clicked.connect(self.click_csv)
        self.button1.adjustSize()

        self.button2 = QtWidgets.QPushButton("Копирование", self)
        self.button2.move(150, 300)
        self.button2.clicked.connect(self.click_copy)
        self.button2.adjustSize()

        self.button3 = QtWidgets.QPushButton("Копирование со случайными номерами", self)
        self.button3.move(222, 300)
        self.button3.clicked.connect(self.click_rand)
        self.button3.adjustSize()
    
    def click_csv():
        pass
    
    def click_copy():
        pass
    
    def click_rand():
        pass

def create():
    app = QApplication(sys.argv)
    w = Interface()

    w.show()
    sys.exit(app.exec_())

create()
