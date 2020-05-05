
from PyQt5.QtWidgets import QMainWindow, QComboBox

from GUIComponents.AddRowWindow import AddRowWindow
from GUIComponents.AddTableWindow import AddTable
from GUIComponents.ConfirmRemoveRowWindow import ConfirmRemoveRowWindow
from GUIComponents.ConfirmWindow import ConfirmWindow
from GUIComponents.EditRowWindow import editTableWindow
from GUIComponents.LoadFileWindow import LoadFile
from GUIComponents.WarningWindow import WarningWindow
from GUIComponents.WriteFileWindow import WriteFile
from MyButton import MyButton
from MyLabel import MyLabel
from ProjectController import ProjectController
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
        self.__buttons.CreateButtons('Dodaj wiersz',550,175,200,30,'none',35,35,'Kliknij aby dodać wiersz',self.addRow)
        self.__buttons.CreateButtons('Usuń wiersz',550,225,200,30,'none',35,35,'Kliknij aby usunąć wiersz',self.removeRow)
        self.__buttons.CreateButtons('Edytuj tabelę',550,275,200,30,'none',35,35,'Kliknij aby edytować tabelę',self.editTable)
        self.__buttons.CreateButtons('Dodaj tabelę',550,325,200,30,'none',35,35,'Kliknij aby dodać nową tabelę',self.createTable)
        self.__buttons.CreateButtons('Usuń tabelę',550,375,200,30,'none',35,35,'Kliknij aby usunąć tabelę',self.removeTable)
        self.__buttons.CreateButtons('Otwórz plik',300,425,200,30,'none',35,35,'Kliknij aby wyjść z programu',self.loadStructure)
        self.__buttons.CreateButtons('Zakończ',550,425,200,30,'none',35,35,'Kliknij aby wyjść z programu',self.end)

        self.__comboBox1 = QComboBox(self)
        self.__comboBox1.move(400,125)
        self.__comboBox1.addItem('Wybierz tabele')
        self.__comboBox1.adjustSize()
        self.__comboBox1.currentTextChanged.connect(self.setComboBox2)

        self.__comboBox2 = QComboBox(self)
        self.__comboBox2.move(400, 175)
        self.__comboBox2.addItem('Wybierz rekord')
        self.__comboBox2.adjustSize()

        self.show()

    def end(self):
        """
        End method
        this method initializes new writeFile object (window)
        :return:
        """
        self.writeFile=WriteFile(self.__ProjectModel)
        self.writeFile.setModal(True)
        self.writeFile.exec()
        self.close()
    def passFunc(self):
        pass
    def removeRow(self):
        """
        removeRow method
        this method calls out removeRow method (ProjectModel)
        """
        try:
            tableName = self.__comboBox1.currentText()
            row=self.__comboBox2.currentText()
            self.__ProjectController.checkRemovedTableName(tableName)
            self.__ProjectController.checkRemovedRow(row)

            confirmRemoveRow = ConfirmRemoveRowWindow(self.__ProjectModel,self.__comboBox2,tableName)
            confirmRemoveRow.setModal(True)
            confirmRemoveRow.exec()
        except Exception as e:
            warning = WarningWindow(str(e))
            warning.setModal(True)
            warning.exec()

    def loadStructure(self):
        """
        Load structure method
        this method initializes new LoadFile object (window)
        """
        self.loadFile=LoadFile(self.__ProjectModel, self.__comboBox1)
        self.loadFile.setModal(True)
        self.loadFile.exec()


    def editTable(self):
        """
        Edit table method
        this method initializes new editTable object (editTable's constructor argument is chosen table in comboBox1)
        """
        try:
            currentTable = self.__comboBox1.currentText()
            self.__ProjectController.checkRemovedTableName(currentTable)
            editTable = editTableWindow(self.__ProjectModel,currentTable)
            editTable.setModal(True)
            editTable.exec()
        except Exception as e:
            warning = WarningWindow(str(e))
            warning.setModal(True)
            warning.exec()
    def setComboBox2(self):
        """
        Set comboBox2 method
        this method adds chosen table's (from comboBox1) rows to comboBox2
        """
        try:
            tableName = self.__comboBox1.currentText()
            y = len(self.__comboBox2)-1
            while(y>0):
                self.__comboBox2.removeItem(y)
                y=y-1
            for x in range(self.__ProjectModel.getTableNumberOfRows(tableName)):
                self.__comboBox2.addItem(str(self.__ProjectModel.getTableRow(tableName, x)))
        except Exception as e:
            print(e)

    def createTable(self):
        """
        Create table function
        this function initializes new AddTable object and adds table name to combobox
        """
        try:
            self.__AddTable=AddTable(self.__ProjectModel)
            self.__AddTable.setModal(True)
            self.__AddTable.exec()
            self.__ProjectController.checkTableName(self.__AddTable.getTableName())
            self.__comboBox1.addItem(self.__AddTable.getTableName())
        except Exception as e:
            print(e)

    def addRow(self):
        """
        Add row method
        this method initializes new Add row window object (if table is chosen)
        """
        try:
            currentTable = self.__comboBox1.currentText()
            self.__ProjectController.checkRemovedTableName(currentTable)
            addRowWindow = AddRowWindow(self.__ProjectModel,currentTable)
            addRowWindow.setModal(True)
            addRowWindow.exec()
        except Exception as e:
            warning = WarningWindow(str(e))
            warning.setModal(True)
            warning.exec()

    def removeTable(self):
        """
        Remove table method
        this method calls out removeTAble method (ProjectModel)
        """
        try:
            tableName = self.__comboBox1.currentText()
            self.__ProjectController.checkRemovedTableName(tableName)
            confirm = ConfirmWindow(self.__ProjectModel, self.__comboBox1, tableName)
            confirm.setModal(True)
            confirm.exec()

        except Exception as e:
            warning = WarningWindow(str(e))
            warning.setModal(True)
            warning.exec()