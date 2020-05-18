from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QPushButton

from errors import BadEnteredTypeException
from GUIComponents.warning_window import WarningWindow
from project_controller import ProjectController
from project_model import ProjectModel


class EditTableWindow(QDialog):
    """
    Edit table class
    """

    def __init__(self, project_model: ProjectModel, table_name: str):
        """
        Edit table class constructor

        :param ProjectModel: Project model (ProjectModel)
        :param tableName: table name (str)
        """
        super().__init__()

        self.__top = 100
        self.__left = 100
        self.__width = 720
        self.__height = 600
        self.__table_name = table_name
        self.__project_model = project_model
        self.__project_controller = ProjectController()
        self.__title = self.__project_model.get_table(table_name).get_table_name()
        self.__number_of_rows = self.__project_model.get_table(table_name).get_number_of_rows()
        self.__number_of_columns = self.__project_model.get_table(table_name).get_number_of_columns()
        self.__column_dict = self.__project_model.get_table(table_name).get_column_dict()
        self.__content = self.__project_model.get_table(table_name).get_content()

        self.init_window()

    def init_window(self):
        """
        Init Window method
        this method sets all window widgets
        """
        self.setWindowTitle(self.__title)
        self.setGeometry(self.__left, self.__top, self.__width, self.__height)
        self.set_table()

        self.v_box_layout = QVBoxLayout()
        self.v_box_layout.addWidget(self.table_widget)

        self.create_button_1()
        self.create_button_2()

        self.v_box_layout.addWidget(self.button1)
        self.v_box_layout.addWidget(self.button2)
        self.setLayout(self.v_box_layout)
        self.show()

    def set_table(self):
        """
        Set table method
        this method creates new QTableWidget object and fills it with table content
        """
        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(self.__number_of_rows)
        self.table_widget.setColumnCount(self.__number_of_columns)
        column_names = ''
        for keys, values in zip(self.__project_model.get_table(self.__table_name).get_column_dict(),
                                self.__project_model.get_table(self.__table_name).get_column_dict().values()):
            column_names = column_names + keys + ' [' + self.__project_model.get_type_dict()[values] + ']' + ','

        self.table_widget.setHorizontalHeaderLabels(column_names.split(','))
        for index_1 in range(self.__number_of_rows):
            for index_2 in range(self.__number_of_columns):
                self.table_widget.setItem(index_1, index_2, QTableWidgetItem(self.__content[index_1][index_2]))

    def create_button_1(self):
        self.button1 = QPushButton('Dodaj wiersz', self)
        self.button1.clicked.connect(self.add_row)

    def create_button_2(self):
        self.button2 = QPushButton('Zapisz tabele', self)
        self.button2.clicked.connect(self.save_data)

    def add_row(self):
        """
        Add row method
        this methods increases table's number of rows and adds new empty row to displayed table
        """
        self.__number_of_rows = self.__number_of_rows + 1
        self.table_widget.setRowCount(self.__number_of_rows)
        for index in range(self.__number_of_columns):
            self.table_widget.setItem(self.__number_of_rows - 1, index, QTableWidgetItem(''))

    def save_data(self):
        """
        Save data method
        this method swap's table old content with new content (loaded from editTable window)
        """
        global content
        try:
            content = []
            self.__project_model.get_table(self.__table_name).set_number_of_rows(0)
            for index_1 in range(self.__number_of_rows):
                row = []
                help_index = 0
                for index_2 in range(self.__number_of_columns):
                    self.__project_controller.check_entered_type(self.table_widget.item(index_1, index_2).text(),
                                                               self.__project_model.get_table(
                                                                   self.__table_name).get_column_types_list()[help_index])
                    row.append(self.table_widget.item(index_1, index_2).text())
                    help_index = help_index + 1
                self.__project_model.get_table(self.__table_name).number_of_rows_increment()
                content.append(row)

            self.close()

        except BadEnteredTypeException as exception:
            content = self.__project_model.get_table(self.__table_name).get_content()
            warning = WarningWindow(str(exception))
            warning.setModal(True)
            warning.exec()

        except Exception:

            warning = WarningWindow("Problemy z zapisywaniem danych")
            warning.setModal(True)
            warning.exec()

        finally:

            self.__project_model.get_table(self.__table_name).set_number_of_rows(len(content))
            self.__project_model.get_table(self.__table_name).set_content(content)
