
from PyQt5.QtWidgets import QComboBox, QDialog, QLineEdit

from GUIComponents.WarningWindow import WarningWindow
from MyButton import MyButton
from MyLabel import MyLabel
from ProjectModel import ProjectModel

class LoadFile(QDialog):
    """
    Load from file class
    """
    def __init__(self, projectModel:ProjectModel, comboBox:QComboBox):
        """
        Load from file class constructor
        :param ProjectModel: project model (ProjectModel)
        :param comboBox: combo box (QComboBox)
        """
        super().__init__()

        self.__title='Otwórz'
        self.__top=400
        self.__left=400
        self.__width=400
        self.__height=150
        self.__buttons=MyButton(self)
        self.__labels=MyLabel(self)
        self.__projectModel=projectModel
        self.__comboBox=comboBox
        self.InitWindow()

    def InitWindow(self):
        """
        Init Window method
        this method sets all window widgets
        """
        self.setWindowTitle('Dodaj tabele')
        self.setGeometry(self.__left, self.__top, self.__width, self.__height)
        self.setFixedSize(400, 150)

        self.__lineedit = QLineEdit(self)
        self.__lineedit.setGeometry(100,50,250,20)

        self.__labels.createLabel('Ścieżka:', 40, 50)
        self.__buttons.CreateButtons('Wczytaj', 10, 110, 180, 30, 'none', 40, 40, 'Kliknij aby dodać nową kolumne do tabeli', self.load)
        self.__buttons.CreateButtons('Anuluj', 210, 110, 180, 30, 'none', 40, 40, 'Kliknij aby dodać tabele',self.close)

    def load(self):
        """
        Load method
        this method calls out readFromFile method (ProjectModel) and adds table names from file to comboBox
        """
        try:
            path=self.__lineedit.text()
            newTables=self.__projectModel.readFromFile(path)
            for x in newTables:
                self.__comboBox.addItem(x)
            self.close()
        except:
            warning=WarningWindow('Wprowadzono błędną ścieżkę!')
            warning.setModal(True)
            warning.exec()
