import sys

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QTableWidget, \
    QTableWidgetItem, QPushButton, QApplication

from Errors import BadEnteredTypeException
from GUIComponents.WarningWindow import WarningWindow
from ProjectController import ProjectController
from ProjectModel import ProjectModel
from Table import Table


class EditRowsWindow(QDialog):
    """
    Edit table class
    """
    def __init__(self,projectModel:ProjectModel, table:Table):
        """
        Edit table class constructor

        :param ProjectModel: Project model (ProjectModel)
        :param tableName: table name (str)
        """
        super().__init__()

        self.__top=100
        self.__left=100
        self.__width=720
        self.__height=600
        self.__ProjectModel=projectModel
        self.__table=table
        self.__tableName=self.__table.getTableName()
        self.__ProjectController = ProjectController()
        self.__title=self.__tableName
        self.__numberOfRows=self.__table.getNumberOfRows()
        self.__numberOfColumns=self.__table.getNumberOfColumns()
        self.__columnDict=self.__table.getColumnDict()
        self.__content=self.__table.getContent()

        self.InitWindow()

    def InitWindow(self):
        """
        Init Window method
        this method sets all window widgets
        """
        self.setWindowTitle(self.__title)
        self.setGeometry(self.__left,self.__top,self.__width,self.__height)

        self.setTable()

        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.addWidget(self.tableWidget)

        self.createButton1()
        self.createButton2()

        self.vBoxLayout.addWidget(self.button1)
        self.vBoxLayout.addWidget(self.button2)
        self.setLayout(self.vBoxLayout)
        self.show()

    def setTable(self):
        """
        Set table method
        this method creates new QTableWidget object and fills it with table content
        """
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(self.__numberOfRows)
        self.tableWidget.setColumnCount(self.__numberOfColumns)
        columnNames=''
        for x, y in zip(self.__columnDict,self.__columnDict.values()):
            columnNames=columnNames+x+' ['+self.__ProjectModel.getTypeDict()[y]+']'+','

        self.tableWidget.setHorizontalHeaderLabels(columnNames.split(','))
        for x in range(self.__numberOfRows):
            for y in range(self.__numberOfColumns):
                self.tableWidget.setItem(x,y,QTableWidgetItem(self.__content[x][y]))


    def createButton1(self):
        self.button1 = QPushButton('Zapisz',self)
        self.button1.clicked.connect(self.SaveData)
    def createButton2(self):
        self.button2 = QPushButton('Wyjdz',self)
        self.button2.clicked.connect(self.close)

    def AddRow(self):
        """
        Add row method
        this methods increases table's number of rows and adds new empty row to displayed table
        """
        self.__numberOfRows=self.__numberOfRows+1
        self.tableWidget.setRowCount(self.__numberOfRows)
        for y in range(self.__numberOfColumns):

            self.tableWidget.setItem(self.__numberOfRows-1,y,QTableWidgetItem(''))


    def SaveData(self):
        """
                Add row method
                this methods increases table's number of rows and adds new empty row to displayed table
                """
        try:
            for y in range(self.__numberOfRows):
                row = []
                helpIndex=0
                for x in range(self.__numberOfColumns):
                    self.__ProjectController.checkEnteredType(self.tableWidget.item(y, x).text(),self.__ProjectModel.getTable(self.__tableName).getColumnTypesList()[helpIndex])
                    row.append(self.tableWidget.item(y, x).text())
                    helpIndex=helpIndex+1
                self.__ProjectModel.editRow(self.__tableName, self.__content[y], row)
            self.__ProjectModel.getTable(self.__tableName).setContent(self.__ProjectModel.getTable(self.__tableName).getContent())
            self.close()

        except BadEnteredTypeException as e:
            warning = WarningWindow(str(e))
            warning.setModal(True)
            warning.exec()

        except:
            warning = WarningWindow("Problemy z zapisywaniem danych")
            warning.setModal(True)
            warning.exec()

