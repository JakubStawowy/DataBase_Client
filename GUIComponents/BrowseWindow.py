
from PyQt5.QtWidgets import QComboBox, QDialog, QLineEdit

from GUIComponents.EditRowWindow import EditRowsWindow
from MyButton import MyButton
from MyLabel import MyLabel
from ProjectModel import ProjectModel
from Table import Table


class BrowseWindow(QDialog):
    """
    Load from file class
    """
    def __init__(self, ProjectModel:ProjectModel, tableName):
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
        self.__ProjectModel=ProjectModel
        self.__tableName=tableName
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
        self.__lineedit.setGeometry(120,50,250,20)

        self.__labels.createLabel('Lambda-wyrażenie:', 20, 50)
        self.__buttons.CreateButtons('Szukaj', 10, 110, 180, 30, 'none', 40, 40, 'Kliknij aby dodać nową kolumne do tabeli', self.browse)
        self.__buttons.CreateButtons('Anuluj', 210, 110, 180, 30, 'none', 40, 40, 'Kliknij aby dodać tabele',self.close)

    def browse(self):
        try:
            x=self.__ProjectModel.lambdaBrowse(self.__tableName,self.__lineedit.text())
            self.close()
            editTable=EditRowsWindow(self.__ProjectModel,Table(self.__tableName,self.__ProjectModel.getTable(self.__tableName).getNumberOfColumns(),len(x),self.__ProjectModel.getTable(self.__tableName).getColumnDict(),x))
            editTable.setModal(True)
            editTable.exec()
        except Exception as e:
            print(e)

