from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLineEdit
from errors import BadLambdaExpressionException
from GUIComponents.edit_row_window import EditRowsWindow
from GUIComponents.warning_window import WarningWindow
from my_button import MyButton
from my_label import MyLabel
from project_model import ProjectModel
from table import Table


class BrowseWindow(QDialog):
    """
    Load from file class
    """

    def __init__(self, project_model: ProjectModel, table_name: str):
        """
        Load from file class constructor
        :param ProjectModel: project model (ProjectModel)
        :param comboBox: combo box (QComboBox)
        """
        super().__init__()
        self.__title = 'Otwórz'
        self.__top = 400
        self.__left = 400
        self.__width = 400
        self.__height = 150
        self.__buttons = MyButton(self)
        self.__labels = MyLabel(self)
        self.__project_model = project_model
        self.__table_name = table_name
        self.init_window()

    def init_window(self):

        """
        Init Window method
        this method sets all window widgets
        """
        self.setWindowTitle('Dodaj tabele')
        self.setGeometry(self.__left, self.__top, self.__width, self.__height)
        self.setFixedSize(400, 150)

        self.__lineedit = QLineEdit(self)
        self.__lineedit.setGeometry(120, 50, 230, 20)

        self.__labels.createLabel('Lambda-wyrażenie:', 20, 50)
        self.__buttons.create_button('Szukaj', 10, 110, 180, 30, 'Kliknij aby dodać nową kolumne do tabeli',
                                     self.browse)
        self.__buttons.create_button('Anuluj', 210, 110, 180, 30, 'Kliknij aby dodać tabele', self.close)
        self.__buttons.create_button('?', 360, 50, 20, 20, 'Kliknij aby wyświetlić przykładowe wyrażenie-lambda',
                                     self.help)

    def browse(self):
        """
        Browse method
        this method loads lambda-expression (typed by user) and displays table with rows (only those for which lambda-expression returns True value)
        :return:
        """
        try:
            new_table = self.__project_model.lambda_browse(self.__table_name, self.__lineedit.text())
            self.close()
            try:

                editTable = EditRowsWindow(self.__project_model,
                                           Table(self.__table_name, self.__project_model.get_table(
                                               self.__table_name).get_number_of_columns(), len(new_table),
                                                 self.__project_model.get_table(
                                                     self.__table_name).get_column_dict(), new_table))

            except:
                raise BadLambdaExpressionException(expression=new_table)
            else:
                editTable.setModal(True)
                editTable.exec()

        except BadLambdaExpressionException as exception:
            warning = WarningWindow(str(exception))
            warning.setModal(True)
            warning.exec()

        except Exception:
            warning = WarningWindow("Wystąpił problem z wyszukiwaniem danych")
            warning.setModal(True)
            warning.exec()

    def help(self):
        self.__lineedit.setText(self.__project_model.generate_lambda_expression(self.__table_name))
