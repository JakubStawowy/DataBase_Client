
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QComboBox, QDialog, QLineEdit, QApplication, QLabel, QVBoxLayout, QTableWidget, \
    QTableWidgetItem, QPushButton

from MyButton import MyButton
from MyLabel import MyLabel

class ConfirmRemoveRowWindow(QDialog):

    def __init__(self, ProjectModel,comboBox ,tableName):
        super().__init__()
        self.__windowTitle = 'Usunąć wiersz?'
        self.__top=300
        self.__left=450
        self.__width = 250
        self.__height=150
        self.__buttons = MyButton(self)
        self.__Labels = MyLabel(self)
        self.__ProjectModel=ProjectModel
        self.__tableName=tableName
        self.__comboBox=comboBox
        self.InitWindow()

    def InitWindow(self):
        self.setGeometry(self.__left,self.__top,self.__width,self.__height)
        self.setFixedSize(250,150)
        self.setWindowTitle(self.__windowTitle)
        self.__Labels.createLabel(self.__windowTitle,90,45)
        self.__buttons.CreateButtons('Usuń',40,90,80,30,'none',0,0,'miau',self.remove)
        self.__buttons.CreateButtons('Anuluj',130,90,80,30,'none',0,0,'miau',self.close)
        self.show()

    def remove(self):
        try:
            x = self.__comboBox.currentText().strip('[]')
            y = x.split(', ')
            l = [y[z].strip('\'') for z in range(len(y))]
            self.__comboBox.removeItem(self.__ProjectModel.getRowIndex(self.__tableName, str(l)) + 1)
            self.__ProjectModel.removeRow(self.__tableName, l)
            self.close()
        except Exception as e:
            print(e)