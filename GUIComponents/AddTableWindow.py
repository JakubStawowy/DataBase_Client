
from PyQt5.QtWidgets import QDialog, QLineEdit, QLabel

from GUIComponents.AddColumnWindow import AddColumnWindow
from GUIComponents.WarningWindow import WarningWindow
from MyButton import MyButton
from MyLabel import MyLabel
from ProjectController import ProjectController
from ProjectModel import ProjectModel
from Table import Table

class AddTable(QDialog):
    """
    Add table class
    """
    def __init__(self, ProjectModel:ProjectModel):
        """
        Add table class constructor

        :param ProjectModel:
            ProjectModel
        """
        super().__init__()
        self.__title = 'Stwórz tabelę'
        self.__top=400
        self.__left=400
        self.__width=405
        self.__height = 200
        self.__buttons = MyButton(self)
        self.__labels = MyLabel(self)
        self.__ProjectModel=ProjectModel
        self.__ProjectController = ProjectController()
        self.__newTable = Table()
        self.getTableName = lambda : self.__newTable.getTableName()
        self.getNumberOfColumns = lambda : self.__newTable.getNumberOfColumns()
        self.InitWindow()

    def InitWindow(self):
        """
        Init Window method
        this method sets all window widgets
        """
        self.setWindowTitle('Dodaj tabele')
        self.setGeometry(self.__left, self.__top, self.__width, self.__height)
        self.setFixedSize(405,200)

        self.__lineedit = QLineEdit(self)
        self.__lineedit.move(130, 50)
        self.CreateCounterLabel(str(self.__newTable.getNumberOfColumns()),130,100)

        self.__labels.createLabel('Nazwa tabeli', 50, 50)
        self.__labels.createLabel('Liczba kolumn', 50, 100)


        self.__buttons.CreateButtons('Dodaj kolumne', 10, 160, 120.3, 30, 'none', 40, 40,'Kliknij aby dodać nową kolumne do tabeli', self.addColumn)
        self.__buttons.CreateButtons('Dodaj tabele', 143.3, 160, 120.3, 30, 'none', 40, 40,'Kliknij aby dodać tabele', self.addTable)
        self.__buttons.CreateButtons('Anuluj', 276.6, 160, 120.3, 30, 'none', 40, 40,'Kliknij aby dodać tabele', self.close)

        self.show()

    def CreateCounterLabel(self,text,x,y):
        """
        Create counter label method
        this method creates new label which displays number of columns in created table

        :param text: text (str)
        :param x: x axis coordinate
        :param y: y axis coordinate
        """
        self.counterLabel = QLabel(self)
        self.counterLabel.setText(text)
        self.counterLabel.adjustSize()
        self.counterLabel.move(x, y)

    def addColumn(self):
        """
        Add column method
        this method initializes new AddColumnWindow Object and sets counter label
        """
        self.__addColumn=AddColumnWindow(self.__ProjectModel,self.__newTable)
        self.__addColumn.setModal(True)
        self.__addColumn.exec()
        self.counterLabel.setText(str(self.__newTable.getNumberOfColumns()))

    def addTable(self):
        """
        Add table method
        this method calls out addTable method (ProjectModel)
        """
        try:
            self.__ProjectController.checkTableName(self.__lineedit.text())
            self.__ProjectController.checkNumberOfcolumns(self.__newTable.getNumberOfColumns())
            self.__newTable.setTableName(self.__lineedit.text())
            self.__ProjectModel.addTable(self.__newTable)
            self.close()
        except Exception as e:
            warning=WarningWindow(str(e))
            warning.setModal(True)
            warning.exec()