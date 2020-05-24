from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QDialog
from errors import BadEnteredTypeException
from GUIComponents.warning_window import WarningWindow
from project_controller import ProjectController
from project_model import ProjectModel
from table import Table


class EditRowsWindow(QDialog):
    """
    Edit table class
    """

    def __init__(self, project_model: ProjectModel, table: Table):
        """
        Edit table class constructor

        :param project_model: ProjectModel
        :param table: Table
        """
        super().__init__()

        self.__top = 100
        self.__left = 100
        self.__width = 720
        self.__height = 600
        self.__project_model = project_model
        self.__table = table
        self.__table_name = self.__table.get_table_name()
        self.__project_controller = ProjectController()
        self.__title = self.__table_name
        self.__number_of_rows = self.__table.get_number_of_rows()
        self.__number_of_columns = self.__table.get_number_of_columns()
        self.__column_dict = self.__table.get_column_dict()
        self.__content = self.__table.get_content()

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

        self.button1 = QPushButton('Zapisz', self)
        self.button1.clicked.connect(self.save_data)

        self.button2 = QPushButton('Wyjdz', self)
        self.button2.clicked.connect(self.close)

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
        for keys, values in zip(self.__column_dict, self.__column_dict.values()):
            column_names = column_names + keys + ' [' + self.__project_model.get_type_dict()[values] + ']' + ','

        self.table_widget.setHorizontalHeaderLabels(column_names.split(','))

        for index_1 in range(self.__number_of_rows):
            for index_2 in range(self.__number_of_columns):
                self.table_widget.setItem(index_1, index_2, QTableWidgetItem(self.__content[index_1][index_2]))

    def save_data(self):
        """
        save_data method
        this method checks if all data typed by user have correct type and
        sets table content in project_model::structure with content loaded from edit_row_window
        """
        try:
            for index_1 in range(self.__number_of_rows):
                row = []
                help_index = 0
                for index_2 in range(self.__number_of_columns):
                    self.__project_controller.check_entered_type(self.table_widget.item(index_1, index_2).text(),
                                                               self.__project_model.get_table(
                                                                   self.__table_name).get_column_types_list()[help_index])
                    row.append(self.table_widget.item(index_1, index_2).text())
                    help_index = help_index + 1
                self.__project_model.edit_row(self.__table_name, self.__content[index_1], row)
            self.__project_model.get_table(self.__table_name).set_content(
                self.__project_model.get_table(self.__table_name).get_content())
            self.close()

        except BadEnteredTypeException as exception:
            warning = WarningWindow(str(exception))
            warning.setModal(True)
            warning.exec()

        except:
            warning = WarningWindow("Problemy z zapisywaniem danych")
            warning.setModal(True)
            warning.exec()
