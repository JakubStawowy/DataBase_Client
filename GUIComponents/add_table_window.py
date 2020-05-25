from PyQt5.QtWidgets import QDialog, QLineEdit, QLabel

from errors import EmptyTableNameException, ExistingTableException
from errors import NoColumnTableException
from GUIComponents.add_column_window import AddColumnWindow
from GUIComponents.warning_window import WarningWindow
from my_widgets import MyButton
from my_widgets import MyLabel
from model_controller import ProjectController
from model_controller import ProjectModel
from table import Table


class AddTableWindow(QDialog):
    """
    Add table class
    """

    def __init__(self, project_model: ProjectModel):
        """
        Add table class constructor

        :param ProjectModel:
            ProjectModel
        """
        super().__init__()
        self.__title = 'Stwórz tabelę'
        self.__top = 400
        self.__left = 400
        self.__width = 405
        self.__height = 200
        self.__buttons = MyButton(self)
        self.__labels = MyLabel(self)
        self.__project_model = project_model
        self.__project_controller = ProjectController()
        self.__new_table = Table()
        self.get_table_name = lambda: self.__new_table.get_table_name()
        self.get_number_of_columns = lambda: self.__new_table.get_number_of_columns()
        self.init_window()

    def init_window(self):
        """
        Init Window method
        this method sets all window widgets
        """
        self.setWindowTitle('Dodaj tabele')
        self.setGeometry(self.__left, self.__top, self.__width, self.__height)
        self.setFixedSize(self.__width, self.__height)

        self.__lineedit = QLineEdit(self)
        self.__lineedit.move(130, 50)
        self.create_counter_label(str(self.__new_table.get_number_of_columns()), 130, 100)

        self.__labels.createLabel('Nazwa tabeli', 50, 50)
        self.__labels.createLabel('Liczba kolumn', 50, 100)

        self.button_1 = self.__buttons.create_button('Dodaj kolumne', 10, 160, 120.3, 30, 'Kliknij aby dodać nową kolumne do tabeli', self.add_column)
        self.button_2 = self.__buttons.create_button('Dodaj tabele', 143.3, 160, 120.3, 30, 'Kliknij aby dodać tabele', self.add_table)
        self.button_3 = self.__buttons.create_button('Anuluj', 276.6, 160, 120.3, 30, 'Kliknij aby dodać tabele', self.close)

        self.show()

    def create_counter_label(self, text, x_coordinate, y_coordinate):
        """
        Create counter label method
        this method creates new label which displays number of columns in created table

        :param text: str
        :param x_coordinate: int
        :param y_coordinate: int
        """
        self.counter_label = QLabel(self)
        self.counter_label.setText(text)
        self.counter_label.adjustSize()
        self.counter_label.move(x_coordinate, y_coordinate)

    def add_column(self):
        """
        Add column method
        this method initializes new AddColumnWindow Object and sets counter label
        """
        self.__addColumn = AddColumnWindow(self.__project_model, self.__new_table)
        self.__addColumn.setModal(True)
        self.__addColumn.exec()
        self.counter_label.setText(str(self.__new_table.get_number_of_columns()))

    def add_table(self):
        """
        Add table method
        this method loads table name and checks if created table number of columns is not equal 0.
        If there was no exception, add_table method from ProjectModel is called
        """
        try:
            self.__project_controller.check_table_name(self.__lineedit.text())
            self.__project_controller.check_number_of_columns(self.__new_table.get_number_of_columns())
            self.__new_table.set_table_name(self.__lineedit.text())
            self.__project_model.add_table(self.__new_table)
            self.close()

        except (EmptyTableNameException, NoColumnTableException, ExistingTableException) as exception:
            warning = WarningWindow(str(exception))
            warning.setModal(True)
            warning.exec()

        except Exception:
            warning = WarningWindow("Wystąpiły problemy z dodawaniem tabeli")
            warning.setModal(True)
            warning.exec()
