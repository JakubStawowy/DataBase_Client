
from PyQt5.QtWidgets import QComboBox, QDialog, QLineEdit

from Errors import NoColumnTypeChosenException, EmptyColumnNameException
from MyButton import MyButton
from MyLabel import MyLabel
from ProjectController import ProjectController
from ProjectModel import ProjectModel
from Table import Table
from GUIComponents.WarningWindow import WarningWindow

class AddColumnWindow(QDialog):
    """
    AddColumnWindow class
    """
    def __init__(self,ProjectModel:ProjectModel, Table:Table):
        """
        AddColumnWindow class constructor

        :param ProjectModel: ProjectModel object (ProjectModel)
        :param Table: Table object (Table)
        """
        super().__init__()
        self.__left=400
        self.__top=400
        self.__width=300
        self.__height=145
        self.buttons=MyButton(self)
        self.labels=MyLabel(self)
        self.__ProjectModel=ProjectModel
        self.__ProjectController = ProjectController()
        self.__Table=Table
        self.InitWindow()

    def InitWindow(self):
        """
        InitWindow method
        this method sets all window widgets
        """
        self.setWindowTitle('Dodaj kolumne')
        self.setGeometry(self.__left,self.__top,self.__width,self.__height)
        self.labels.createLabel('Nazwa kolumny',30,30)
        self.labels.createLabel('Typ danych',30,60)
        self.lineedit = QLineEdit(self)
        self.lineedit.move(120, 30)

        self.comboBox = QComboBox(self)
        self.comboBox.addItem('Wybierz Typ')
        self.comboBox.addItem('Tekst')
        self.comboBox.addItem('Liczba całkowita')
        self.comboBox.addItem('Liczba porządkowa')
        self.comboBox.addItem('Liczba rzeczywista')
        self.comboBox.move(120, 60)

        self.buttons.CreateButtons('Dodaj kolumne', 10, 105, 120, 30, 'pics\Edit_Row.png', 40, 40,'Kliknij aby dodać kolumne', self.addColumn)
        self.buttons.CreateButtons('Anuluj', 160, 105, 120, 30, 'pics\Edit_Row.png', 40, 40,'Kliknij aby anulować', self.close)

        self.show()

    def addColumn(self):
        """
        Add Column method
        this method calls out addColumn method (Table)
        """
        try:
            columnType=self.comboBox.currentText()
            columnName=self.lineedit.text()
            self.__ProjectController.checkColumnName(columnName)
            self.__ProjectController.checkColumnType(columnType)
            self.__Table.addColumn(columnName,columnType)
            self.close()

        except (NoColumnTypeChosenException, EmptyColumnNameException) as e:

            warning = WarningWindow(str(e))
            warning.setModal(True)
            warning.exec()

        except:
            warning = WarningWindow("Wystąpiły problemy z dodawaniem kolumny")
            warning.setModal(True)
            warning.exec()
