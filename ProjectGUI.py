import sys

from PyQt5.QtWidgets import QMainWindow, QComboBox, QDialog, QLineEdit, QApplication, QLabel

from MyButton import MyButton
from MyLabel import MyLabel
from ProjectController import ProjectController
from ProjectModel import ProjectModel
from Table import Table


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
        self.__ProjectController = ProjectController()
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
        self.__buttons.CreateButtons('Edytuj tabelę',550,275,200,30,'none',35,35,'Kliknij aby edytować tabelę',self.showStructure)
        self.__buttons.CreateButtons('Dodaj tabelę',550,325,200,30,'none',35,35,'Kliknij aby dodać nową tabelę',self.createTable)
        self.__buttons.CreateButtons('Usuń tabelę',550,375,200,30,'none',35,35,'Kliknij aby usunąć tabelę',self.removeTable)
        self.__buttons.CreateButtons('Zakończ',550,425,200,30,'none',35,35,'Kliknij aby wyjść z programu',self.Cancel)

        self.__comboBox1 = QComboBox(self)
        self.__comboBox1.move(400,125)
        self.__comboBox1.addItem('Wybierz tabele')
        self.__comboBox1.adjustSize()

        self.__comboBox2 = QComboBox(self)
        self.__comboBox2.move(400, 175)
        self.__comboBox2.addItem('Wybierz rekord')
        self.__comboBox2.adjustSize()

        self.show()

    def passFunc(self):
        pass

    def showStructure(self):

        self.__ProjectModel.showStructure()

    def createTable(self):
        """
        Create table function
        this function initates new AddTable object and adds table name to combobox
        """
        try:
            self.__AddTable=AddTable(self.__ProjectModel)
            self.__AddTable.setModal(True)
            self.__AddTable.exec()
            self.__ProjectController.checkTableName(self.__AddTable.getTableName())
            self.__comboBox1.addItem(self.__AddTable.getTableName())
        except Exception as e:
            print(e)


    def removeTable(self):
        """
        Remove table method
        this method calls out removeTAble method (ProjectModel)
        """
        try:
            currentText = self.__comboBox1.currentText()
            self.__ProjectController.checkRemovedTableName(currentText)
            self.confirmWindow()
            index=self.__ProjectModel.returnTableIndex(self.__ProjectModel.getStructure(),currentText)+1
            self.__ProjectModel.removeTable(currentText)
            self.__comboBox1.removeItem(index)
            #self.setComboBox1()

        except Exception as e:
            self.warningWindow(str(e))


    def Cancel(self):
        """
        Cancel function
        this function closes the current window
        """
        self.close()

    def warningWindow(self, warningText:str):
        """
        Warning window method
        this method initates new WaringWindow object
        :param warningText: warning message (str)
        """
        warning = WarningWindow(warningText)
        warning.setModal(True)
        warning.exec()

    def confirmWindow(self):
        """
        Confirm window method
        this method initates new ConfirmWindow object
        """
        confirm = ConfirmWindow(self.__ProjectModel)
        confirm.setModal(True)
        confirm.exec()


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
        self.__buttons.CreateButtons('Anuluj', 276.6, 160, 120.3, 30, 'none', 40, 40,'Kliknij aby dodać tabele', self.Cancel)

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

    def Cancel(self):
        """
        Cancel function
        this function closes the current window
        """
        self.close()

    def passFunc(self):
        pass

    def addColumn(self):
        """
        Add column method
        this method initializes new AddColumnWindow Object and sets counter label
        """
        self.__addColumn=AddColumnWindow(self.__ProjectModel,self.__newTable)
        self.__addColumn.setModal(True)
        self.__addColumn.exec()
        self.counterLabel.setText(str(self.__newTable.getNumberOfColumns()))
        print(self.__newTable)

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
            self.warningWindow(str(e))

    def warningWindow(self,text):
        """
        Warning window method
        this method initates new WaringWindow object
        :param text: warning message (str)
        """
        warning=WarningWindow(text)
        warning.setModal(True)
        warning.exec()

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
        self.comboBox.addItem('Liczba rzeczywista')
        self.comboBox.move(120, 60)

        self.buttons.CreateButtons('Dodaj kolumne', 10, 105, 120, 30, 'pics\Edit_Row.png', 40, 40,'Kliknij aby dodać kolumne', self.addColumn)
        self.buttons.CreateButtons('Anuluj', 160, 105, 120, 30, 'pics\Edit_Row.png', 40, 40,'Kliknij aby anulować', self.Cancel)

        self.show()

    def Cancel(self):

        self.close()

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
        except Exception as e:
            self.warinngWindow(str(e))

    def warinngWindow(self,text):
        """
        Warning window method
        this method initates new WaringWindow object
        :param text: warning message (str)
        """
        warning=WarningWindow(text)
        warning.setModal(True)
        warning.exec()

class WarningWindow(QDialog):

    def __init__(self, warningText):
        super().__init__()
        self.__windowTitle = 'Uwaga'
        self.__top=300
        self.__left=450
        self.__width = 250
        self.__height=150
        self.__buttons = MyButton(self)
        self.__Labels = MyLabel(self)
        self.__text = warningText
        self.InitWindow()

    def InitWindow(self):
        self.setGeometry(self.__left,self.__top,self.__width,self.__height)
        self.setFixedSize(250,150)
        self.setWindowTitle(self.__windowTitle)
        self.__Labels.createLabel(self.__text,80,45)
        self.__buttons.CreateButtons('Anuluj',75,90,100,30,'none',0,0,'miau',self.close)
        self.show()

class ConfirmWindow(QDialog):

    def __init__(self, ProjectModel):
        super().__init__()
        self.__windowTitle = 'Usunąć tabele?'
        self.__top=300
        self.__left=450
        self.__width = 250
        self.__height=150
        self.__buttons = MyButton(self)
        self.__Labels = MyLabel(self)
        self.__ProjectModel=ProjectModel
        self.InitWindow()

    def InitWindow(self):
        self.setGeometry(self.__left,self.__top,self.__width,self.__height)
        self.setFixedSize(250,150)
        self.setWindowTitle(self.__windowTitle)
        self.__Labels.createLabel(self.__windowTitle,90,45)
        self.__buttons.CreateButtons('Usuń',40,90,80,30,'none',0,0,'miau',self.close)
        self.__buttons.CreateButtons('Anuluj',130,90,80,30,'none',0,0,'miau',self.close)
        self.show()

    def Cancel(self):
        self.__ProjectModel.ProjectController.cancel()

if __name__=='__main__':

    App=QApplication(sys.argv)
    pm=ProjectModel()
    mytcMainWindow=MainWindow(pm)

    sys.exit(App.exec())