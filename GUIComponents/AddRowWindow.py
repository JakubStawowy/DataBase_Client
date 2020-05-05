
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton
from ProjectController import ProjectController
from ProjectModel import ProjectModel

class AddRowWindow(QDialog):
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
        self.__height=100
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
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(self.__numberOfColumns)
        columnNames = ''
        for x, y in zip(self.__ProjectModel.getTable(self.__tableName).getColumnDict(),
                        self.__ProjectModel.getTable(self.__tableName).getColumnDict().values()):
            columnNames = columnNames + x + ' [' + self.__ProjectModel.getTypeDict()[y] + ']' + ','

        self.tableWidget.setHorizontalHeaderLabels(columnNames.split(','))
        for y in range(self.__numberOfColumns):

            self.tableWidget.setItem(0,y,QTableWidgetItem(''))



    def createButton1(self):

        self.button1 = QPushButton('Dodaj wiersz',self)
        self.button1.clicked.connect(self.AddRow)

    def createButton2(self):

        self.button2 = QPushButton('Anuluj',self)
        self.button2.clicked.connect(self.close)

    def AddRow(self):
        """
        Add row method
        this methods increases table's number of rows and adds new empty row to displayed table
        """
        row = []
        for x in range(self.__numberOfColumns):
            row.append(self.tableWidget.item(0,x).text())
        self.__ProjectModel.addRow(self.__tableName,row)
        self.close()