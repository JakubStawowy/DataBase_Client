from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QPushButton
from errors import BadEnteredTypeException
from GUIComponents.warning_window import WarningWindow
from model_controller import ProjectController
from model_controller import ProjectModel


class AddRowWindow(QDialog):
    """
    AddRowWindow class
    """

    def __init__(self, project_model: ProjectModel, table_name: str):
        """
        Edit table class constructor

        :param project_model: Project model (ProjectModel)
        :param table_name: table name (str)
        """
        super().__init__()

        self.__top = 100
        self.__left = 100
        self.__width = 720
        self.__height = 100
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

        self.button_1 = QPushButton('Dodaj wiersz', self)
        self.button_1.clicked.connect(self.add_row)

        self.button_2 = QPushButton('Anuluj', self)
        self.button_2.clicked.connect(self.close)

        self.v_box_layout.addWidget(self.button_1)
        self.v_box_layout.addWidget(self.button_2)
        self.setLayout(self.v_box_layout)
        self.show()

    def set_table(self):
        """
        Set table method
        this method creates new QTableWidget object and fills it with table content
        """
        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(1)
        self.table_widget.setColumnCount(self.__number_of_columns)
        column_names = ''
        for name, type in zip(self.__project_model.get_table(self.__table_name).get_column_dict(),
                        self.__project_model.get_table(self.__table_name).get_column_dict().values()):
            column_names = column_names + name + ' [' + self.__project_model.get_type_dict()[type] + ']' + ','

        self.table_widget.setHorizontalHeaderLabels(column_names.split(','))
        for index in range(self.__number_of_columns):
            self.table_widget.setItem(0, index, QTableWidgetItem(''))

    def add_row(self):
        """
        Add row method
        this methods checks if all column types are correct and no column is empty (except int - auto_increment type)
        If there was no exception, add_row method from project_model is called
        """
        try:
            row = []
            help_index = 0
            for index in range(self.__number_of_columns):
                self.__project_controller.check_entered_type(self.table_widget.item(0, index).text(),
                                                          self.__project_model.get_table(
                                                              self.__table_name).get_column_types_list()[help_index])
                row.append(self.table_widget.item(0, index).text())
                help_index = help_index + 1
            self.__project_model.add_row(self.__table_name, row)
            self.close()

        except BadEnteredTypeException as exception:

            warning = WarningWindow(str(exception))
            warning.setModal(True)
            warning.exec()

        except Exception:

            warning = WarningWindow("Problemy z zapisywaniem danych")
            warning.setModal(True)
            warning.exec()
