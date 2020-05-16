import random

from PyQt5.QtWidgets import QComboBox, QDialog, QLineEdit

from Errors import BadLambdaExpressionException
from GUIComponents.EditRowWindow import EditRowsWindow
from GUIComponents.WarningWindow import WarningWindow
from MyButton import MyButton
from MyLabel import MyLabel
from ProjectModel import ProjectModel
from Table import Table


class BrowseWindow(QDialog):

    """
    Load from file class
    """
    def __init__(self, projectModel:ProjectModel, tableName):
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
        self.__lineedit.setGeometry(120,50,230,20)

        self.__labels.createLabel('Lambda-wyrażenie:', 20, 50)
        self.__buttons.CreateButtons('Szukaj', 10, 110, 180, 30, 'none', 40, 40, 'Kliknij aby dodać nową kolumne do tabeli', self.browse)
        self.__buttons.CreateButtons('Anuluj', 210, 110, 180, 30, 'none', 40, 40, 'Kliknij aby dodać tabele',self.close)
        self.__buttons.CreateButtons('?', 360, 50, 20, 20, 'none', 40, 40, 'Kliknij aby wyświetlić przykładowe wyrażenie-lambda',self.help)

    def browse(self):
        """
        Browse method
        this method loads lambda-expression (typed by user) and displays table with rows (only those for which lambda-expression returns True value)
        :return:
        """
        try:
            x=self.__projectModel.lambdaBrowse(self.__tableName,self.__lineedit.text())
            self.close()
            try:

                editTable=EditRowsWindow(self.__projectModel,Table(self.__tableName,self.__projectModel.getTable(self.__tableName).getNumberOfColumns(),len(x),self.__projectModel.getTable(self.__tableName).getColumnDict(),x))

            except:
                raise BadLambdaExpressionException(expression=x)
            else:
                editTable.setModal(True)
                editTable.exec()

        except BadLambdaExpressionException as e:
            warning = WarningWindow(str(e))
            warning.setModal(True)
            warning.exec()

        except Exception as e:
            warning = WarningWindow("Wystąpił problem z wyszukiwaniem danych")
            warning.setModal(True)
            warning.exec()
    def help(self):

        self.__lineedit.setText(self.__projectModel.generateLambdaExpression(self.__tableName))

