from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QLineEdit
from PyQt5 import QtCore
import sys
import os
import copy_
import rand
import write_csv

class Interface(QMainWindow):
    def __init__(self):
        super(Interface, self).__init__()

        self.setWindowTitle("ROSE and TULIP")
        self.move(700, 200)
        self.resize(600, 500)

        self.w_text = QLineEdit(self)
        self.w_text.move(10, 20)
        self.w_text.adjustSize()
        
        self.text = QtWidgets.QLabel("Введите путь к исходному датасету:", self)
        self.text.move(10, 0)
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
        
        
    
    def click_csv(self):
        if not self.w_text.text():
            self.w = New_Interface()
            self.w.new_path()
        elif not os.path.isdir(self.w_text.text()): 
            self.w = New_Interface()
            self.w.not_path()
        else:
          # "D:\Lab Python\Lab_1\dataset\ rose" 
          self.d_text, self.ok = QInputDialog.getText(self, "Аннотация", "Введите путь для сохранения:") 
          print(self.d_text)  
          write_csv.write_csv(self.w_text.text(), self.d_text, "rose")   
          write_csv.write_csv(self.w_text.text(), self.d_text, "tulip")   

    def click_copy(self):
        if not self.w_text.text():
            self.w = New_Interface()
            self.w.new_path()
            
        elif not os.path.isdir(self.w_text.text()): 
            self.w = New_Interface()
            self.w.not_path()
        else:
            self.d_text, self.ok = QInputDialog.getText(self, "Копирование", "Введите путь для копирования:")
            print(self.d_text)
            copy_.copy_dataset(self.w_text.text(), self.d_text, "rose")
            copy_.copy_dataset(self.w_text.text(), self.d_text, "tulip")
    
    def click_rand(self):
        if not self.w_text.text():
            self.w = New_Interface()
            self.w.new_path()
            
        elif not os.path.isdir(self.w_text.text()): 
            self.w = New_Interface()
            self.w.not_path()
            
        else:
            self.d_text, self.ok = QInputDialog.getText(self, "Копирование со случайными номерами", "Введите путь для копирования:")
            print(self.d_text)  
            rand.copy_dataset(self.w_text.text(), self.d_text, "rose")
            rand.copy_dataset(self.w_text.text(), self.d_text, "tulip")

class New_Interface(QMainWindow):
    def __init__(self):
        super(New_Interface, self).__init__()
    
    def new_path(self):
        self.setWindowTitle("Предупреждение")
        self.move(700, 200)
        self.resize(300, 150)
        self.wtext = QtWidgets.QLabel("Введите путь к исходному датасету", self)
        self.wtext.move(55, 60)
        self.wtext.adjustSize()
        self.show()
    
    def not_path(self):
        self.setWindowTitle("Предупреждение")
        self.move(700, 200)
        self.resize(300, 150)
        self.wtext = QtWidgets.QLabel("Указанного датасета не существует", self)
        self.wtext.move(55, 60)
        self.wtext.adjustSize()
        self.show()   
        
def create():
    app = QApplication(sys.argv)
    w = Interface()

    w.show()
    sys.exit(app.exec_())

create()
