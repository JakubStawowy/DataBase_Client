from PyQt5.QtWidgets import QComboBox, QDialog, QLineEdit

from errors import NoColumnTypeChosenException, EmptyColumnNameException
from my_button import MyButton
from my_label import MyLabel
from project_controller import ProjectController
from project_model import ProjectModel
from table import Table
from GUIComponents.warning_window import WarningWindow


class AddColumnWindow(QDialog):
    """
    AddColumnWindow class
    """

    def __init__(self, project_model: ProjectModel, table: Table):
        """
        AddColumnWindow class constructor

        :param ProjectModel: ProjectModel object (ProjectModel)
        :param Table: Table object (Table)
        """
        super().__init__()
        self.__left = 400
        self.__top = 400
        self.__width = 300
        self.__height = 145
        self.buttons = MyButton(self)
        self.labels = MyLabel(self)
        self.__project_model = project_model
        self.__project_controller = ProjectController()
        self.__table = table
        self.init_window()

    def init_window(self):
        """
        InitWindow method
        this method sets all window widgets
        """
        self.setWindowTitle('Dodaj kolumne')
        self.setGeometry(self.__left, self.__top, self.__width, self.__height)
        self.labels.createLabel('Nazwa kolumny', 30, 30)
        self.labels.createLabel('Typ danych', 30, 60)
        self.lineedit = QLineEdit(self)
        self.lineedit.move(120, 30)

        self.combo_box = QComboBox(self)
        self.combo_box.addItem('Wybierz Typ')
        self.combo_box.addItem('Tekst')
        self.combo_box.addItem('Liczba całkowita')
        self.combo_box.addItem('Liczba porządkowa')
        self.combo_box.addItem('Liczba rzeczywista')
        self.combo_box.move(120, 60)

        self.button_1 = self.buttons.create_button('Dodaj kolumne', 10, 105, 120, 30, 'Kliknij aby dodać kolumne', self.add_column)
        self.button_2 = self.buttons.create_button('Anuluj', 160, 105, 120, 30, 'pics\Edit_Row.png', self.close)

        self.show()

    def add_column(self):
        """
        Add Column method
        this method calls out addColumn method (Table)
        """
        try:
            column_type = self.combo_box.currentText()
            column_name = self.lineedit.text()
            self.__project_controller.check_column_name(column_name)
            self.__project_controller.check_column_type(column_type)
            self.__table.add_column(column_name, column_type)
            self.close()

        except (NoColumnTypeChosenException, EmptyColumnNameException) as exception:

            warning = WarningWindow(str(exception))
            warning.setModal(True)
            warning.exec()

        except:
            warning = WarningWindow("Wystąpiły problemy z dodawaniem kolumny")
            warning.setModal(True)
            warning.exec()
