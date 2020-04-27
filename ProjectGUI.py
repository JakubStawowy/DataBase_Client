import sys

from PyQt5.QtWidgets import QMainWindow, QComboBox, QDialog, QLineEdit, QApplication

from MyButton import MyButton
from MyLabel import MyLabel
from ProjectModel import ProjectModel


class MainWindow(QMainWindow):
    """
    Main window class
    """

    def __init__(self,ProjectModel:ProjectModel):
        """
        Main window class constructor
        Constructor sets basic parameters (title, position, MyButton class, MyLabel class)

        Argument 1: ProjectModel class (Data storage class with logical methods)
        """
        super().__init__()

        self.__title='MyTableCreator'
        self.__top=150
        self.__left=350
        self.__height=500
        self.__width=800
        self.__buttons=MyButton(self)
        self.__labels=MyLabel(self)
        self.__ProjectModel=ProjectModel
        self.InitWindow() #Initating window

    def InitWindow(self):
        """
        Init Window function
        this function sets all window widgets
        """
        self.setWindowTitle(self.__title)
        self.setGeometry(self.__left, self.__top, self.__width, self.__height)
        self.setFixedSize(self.__width, self.__height)

        self.__buttons.CreateButtons('Edytuj wiersz',550,125,200,30,'none',40,40,'Kliknij aby edytować wiersz',self.passFunc)
        self.__buttons.CreateButtons('Dodaj wiersz',550,175,200,30,'none',35,35,'Kliknij aby dodać wiersz',self.passFunc)
        self.__buttons.CreateButtons('Usuń wiersz',550,225,200,30,'none',35,35,'Kliknij aby usunąć wiersz',self.passFunc)
        self.__buttons.CreateButtons('Edytuj tabelę',550,275,200,30,'none',35,35,'Kliknij aby edytować tabelę',self.passFunc)
        self.__buttons.CreateButtons('Dodaj tabelę',550,325,200,30,'none',35,35,'Kliknij aby dodać nową tabelę',self.createTable)
        self.__buttons.CreateButtons('Usuń tabelę',550,375,200,30,'none',35,35,'Kliknij aby usunąć tabelę',self.passFunc)
        self.__buttons.CreateButtons('Zakończ',550,425,200,30,'none',35,35,'Kliknij aby wyjść z programu',self.Cancel)

        self.comboBox1 = QComboBox(self)
        self.comboBox1.move(400,125)
        self.comboBox1.addItem('Wybierz tabele')
        self.comboBox1.adjustSize()

        self.comboBox2 = QComboBox(self)
        self.comboBox2.move(400, 175)
        self.comboBox2.addItem('Wybierz rekord')
        self.comboBox2.adjustSize()

        self.show()

    def passFunc(self):
        pass

    def createTable(self):
        """
        Create table function
        this function initates new AddTable object
        """
        self.__AddTable=AddTable(self.__ProjectModel)
        self.__AddTable.setModal(True)
        self.__AddTable.exec()

    def Cancel(self):
        """
        Cancel function
        this function closes the current window
        """
        self.close()




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

        self.__labels.createLabel('Nazwa tabeli', 50, 50)
        self.__labels.createLabel('Liczba kolumn', 50, 100)

        self.__buttons.CreateButtons('Dodaj kolumne', 10, 160, 120.3, 30, 'none', 40, 40,'Kliknij aby dodać nową kolumne do tabeli', self.passFunc)
        self.__buttons.CreateButtons('Dodaj tabele', 143.3, 160, 120.3, 30, 'none', 40, 40,'Kliknij aby dodać tabele', self.passFunc)
        self.__buttons.CreateButtons('Anuluj', 276.6, 160, 120.3, 30, 'none', 40, 40,'Kliknij aby dodać tabele', self.Cancel)

        self.show()

    def Cancel(self):
        """
        Cancel function
        this function closes the current window
        """
        self.close()

    def passFunc(self):
        pass

