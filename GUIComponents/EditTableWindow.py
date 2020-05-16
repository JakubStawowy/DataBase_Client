
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QTableWidget, \
    QTableWidgetItem, QPushButton

from Errors import *
from GUIComponents.WarningWindow import WarningWindow
from ProjectController import ProjectController
from ProjectModel import ProjectModel


class editTableWindow(QDialog):
    """
    Edit table class
    """
    def __init__(self,projectModel:ProjectModel, tableName:str):
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
        self.__tableName=tableName
        self.__ProjectModel=projectModel
        self.__ProjectController = ProjectController()
        self.__title=self.__ProjectModel.getTable(tableName).getTableName()
        self.__numberOfRows=self.__ProjectModel.getTable(tableName).getNumberOfRows()
        self.__numberOfColumns=self.__ProjectModel.getTable(tableName).getNumberOfColumns()
        self.__columnDict=self.__ProjectModel.getTable(tableName).getColumnDict()
        self.__content=self.__ProjectModel.getTable(tableName).getContent()


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
        for x, y in zip(self.__ProjectModel.getTable(self.__tableName).getColumnDict(),self.__ProjectModel.getTable(self.__tableName).getColumnDict().values()):
            columnNames=columnNames+x+' ['+self.__ProjectModel.getTypeDict()[y]+']'+','

        self.tableWidget.setHorizontalHeaderLabels(columnNames.split(','))
        for x in range(self.__numberOfRows):
            for y in range(self.__numberOfColumns):
                self.tableWidget.setItem(x,y,QTableWidgetItem(self.__content[x][y]))


    def createButton1(self):
        self.button1 = QPushButton('Dodaj wiersz',self)
        self.button1.clicked.connect(self.AddRow)
    def createButton2(self):
        self.button2 = QPushButton('Zapisz tabele',self)
        self.button2.clicked.connect(self.SaveData)

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
        Save data method
        this method swap's table old content with new content (loaded from editTable window)
        """
        global content
        try:
            content = []
            self.__ProjectModel.getTable(self.__tableName).setNumberOfRows(0)
            for x in range(self.__numberOfRows):
                row = []
                helpIndex=0
                for y in range(self.__numberOfColumns):

                    self.__ProjectController.checkEnteredType(self.tableWidget.item(x,y).text(),self.__ProjectModel.getTable(self.__tableName).getColumnTypesList()[helpIndex])
                    row.append(self.tableWidget.item(x,y).text())
                    helpIndex = helpIndex+1
                self.__ProjectModel.getTable(self.__tableName).numberOfRowsIncrement()
                content.append(row)

            self.close()

        except BadEnteredTypeException as e:
            content = self.__ProjectModel.getTable(self.__tableName).getContent()
            print('Ustawiam kontencik: ',content)
            warning = WarningWindow(str(e))
            warning.setModal(True)
            warning.exec()

        except Exception:

            warning = WarningWindow("Problemy z zapisywaniem danych")
            warning.setModal(True)
            warning.exec()

        finally:
            
            self.__ProjectModel.getTable(self.__tableName).setNumberOfRows(len(content))
            self.__ProjectModel.getTable(self.__tableName).setContent(content)