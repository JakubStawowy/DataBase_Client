from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QMainWindow, QComboBox, QDialog, QLineEdit, QLabel, QVBoxLayout, QPushButton, QTableWidget, \
    QTableWidgetItem

from errors import NoColumnTypeChosenException, EmptyColumnNameException, EmptyTableNameException, \
    NoColumnTableException, ExistingTableException, BadEnteredTypeException, BadLambdaExpressionException
from database_logic import ProjectController
from database_logic import ProjectModel
from database_logic import Table


class MainWindow(QMainWindow):
    """
    Main window class
    """

    def __init__(self, project_model: ProjectModel):
        """
        Main window class constructor

        :param project_model: ProjectModel
        """
        super().__init__()

        self.__title = 'MyTableCreator'
        self.__top = 150
        self.__left = 350
        self.__height = 500
        self.__width = 800
        self.__buttons = MyButton(self)
        self.__labels = MyLabel(self)
        self.__project_model = project_model
        self.__project_controller = ProjectController()
        self.init_window()

    def init_window(self):
        """
        Init Window function
        this function sets all window widgets
        """
        self.setWindowTitle(self.__title)
        self.setGeometry(self.__left, self.__top, self.__width, self.__height)
        self.setFixedSize(self.__width, self.__height)

        self.button_1 = self.__buttons.create_button('Wyszukaj', 550, 75, 200, 30, 'Kliknij aby przeszukać tabele',
                                                     self.browse)
        self.button_1.setEnabled(False)

        self.button_2 = self.__buttons.create_button('Edytuj wiersz', 550, 125, 200, 30, 'Kliknij aby edytować wiersz',
                                                     self.edit_row)
        self.button_2.setEnabled(False)

        self.button_3 = self.__buttons.create_button('Dodaj wiersz', 550, 175, 200, 30, 'Kliknij aby dodać wiersz',
                                                     self.add_row)

        self.button_3.setEnabled(False)

        self.button_4 = self.__buttons.create_button('Usuń wiersz', 550, 225, 200, 30, 'Kliknij aby usunąć wiersz',
                                                     self.remove_row)

        self.button_4.setEnabled(False)

        self.button_5 = self.__buttons.create_button('Edytuj tabelę', 550, 275, 200, 30, 'Kliknij aby edytować tabelę',
                                                     self.edit_table)

        self.button_5.setEnabled(False)

        self.button_6 = self.__buttons.create_button('Dodaj tabelę', 550, 325, 200, 30, 'Kliknij aby dodać nową tabelę',
                                                     self.create_table)
        self.button_7 = self.__buttons.create_button('Usuń tabelę', 550, 375, 200, 30, 'Kliknij aby usunąć tabelę',
                                                     self.remove_table)

        self.button_7.setEnabled(False)

        self.button_8 = self.__buttons.create_button('Otwórz plik', 300, 425, 200, 30, 'Kliknij aby otworzyć plik',
                                                     self.load_structure)
        self.button_9 = self.__buttons.create_button('Zakończ', 550, 425, 200, 30, 'Kliknij aby wyjść z programu',
                                                     self.end)

        self.__combo_box_1 = QComboBox(self)
        self.__combo_box_1.move(400, 125)
        self.__combo_box_1.addItem('Wybierz tabele')
        self.__combo_box_1.adjustSize()
        self.__combo_box_1.currentTextChanged.connect(self.set_combo_box_2)

        self.__combo_box_2 = QComboBox(self)
        self.__combo_box_2.move(400, 175)
        self.__combo_box_2.addItem('Wybierz rekord')
        self.__combo_box_2.adjustSize()
        self.__combo_box_2.currentTextChanged.connect(self.combo_box_2_changed)

        self.show()

    def end(self):
        """
        End method
        this method initializes new writeFile object (window)
        after executing write to file procedure, window is closed
        :return:
        """
        self.writeFile = WriteFile(self.__project_model)
        self.writeFile.setModal(True)
        self.writeFile.exec()
        self.close()

    def browse(self):
        """
        browse method
        this method checks if table was chosen from combo box 1 and initializes new BrowseWindow object
        :return:
        """
        try:
            current_table = self.__combo_box_1.currentText()
            self.__project_controller.check_removed_table_name(current_table)
            browse_window = BrowseWindow(self.__project_model, current_table)
            browse_window.setModal(True)
            browse_window.exec()
            self.set_combo_box_2()
        except Exception as exception:
            warning = WarningWindow(str(exception))
            warning.setModal(True)
            warning.exec()

    def edit_row(self):
        """
        edit row method
        this method checks if table and raw were chosen from combo boxes and initializes new EditRowsWindow object
        :return:
        """
        try:
            current_table = self.__combo_box_1.currentText()
            current_row = self.__combo_box_2.currentText()
            self.__project_controller.check_removed_table_name(current_table)
            self.__project_controller.check_removed_row(current_row)

            new_table = Table(current_table, self.__project_model.get_table(current_table).get_number_of_columns(), 1,
                              self.__project_model.get_table(current_table).get_column_dict(), [
                                  self.__project_model.get_table_row(current_table,
                                                                     self.__project_model.get_row_index(current_table,
                                                                                                        current_row))])

            edit_row_window = EditRowsWindow(self.__project_model, new_table)
            edit_row_window.setModal(True)
            edit_row_window.exec()
            self.set_combo_box_2()

        except Exception as exception:

            warning = WarningWindow(str(exception))
            warning.setModal(True)
            warning.exec()

    def remove_row(self):
        """
        removeRow method
        this method checks if table and row were chosen from combo boxes and initializes new ConfirmRemoveWindow object
        """
        try:
            table_name = self.__combo_box_1.currentText()
            row = self.__combo_box_2.currentText()
            self.__project_controller.check_removed_table_name(table_name)
            self.__project_controller.check_removed_row(row)

            confirm_remove_row = ConfirmRemoveRowWindow(self.__project_model, self.__combo_box_2, table_name)
            confirm_remove_row.setModal(True)
            confirm_remove_row.exec()

        except Exception as exception:
            warning = WarningWindow(str(exception))
            warning.setModal(True)
            warning.exec()

    def load_structure(self):
        """
        Load structure method
        this method initializes new LoadFile object (window)
        """
        load_file = LoadFile(self.__project_model, self.__combo_box_1)
        load_file.setModal(True)
        load_file.exec()


    def edit_table(self):
        """
        edit table method
        this method checks if table was chosen from combo box 1 and initializes new editTable object (editTable's constructor argument is chosen table in comboBox1)
        """
        try:
            current_table = self.__combo_box_1.currentText()
            self.__project_controller.check_removed_table_name(current_table)
            edit_table = EditTableWindow(self.__project_model, current_table)
            edit_table.setModal(True)
            edit_table.exec()
            self.set_combo_box_2()
        except Exception as exception:
            warning = WarningWindow(str(exception))
            warning.setModal(True)
            warning.exec()

    def set_combo_box_2(self):
        """
        set comboBox 2 method
        this method adds rows from chosen table to comboBox2
        """
        try:
            table_name = self.__combo_box_1.currentText()
            index = len(self.__combo_box_2) - 1
            while (index > 0):
                self.__combo_box_2.removeItem(index)
                index = index - 1
            for index in range(self.__project_model.get_table_number_of_rows(table_name)):
                self.__combo_box_2.addItem(str(self.__project_model.get_table_row(table_name, index)))

            self.button_1.setEnabled(True)
            self.button_3.setEnabled(True)
            self.button_5.setEnabled(True)
            self.button_7.setEnabled(True)

        except Exception:

            self.button_1.setEnabled(False)
            self.button_3.setEnabled(False)
            self.button_5.setEnabled(False)
            self.button_7.setEnabled(False)

    def combo_box_2_changed(self):
        """
        combo box 2 changed method
        this method adjusts combo box 2 size to current row size
        :return:
        """
        if self.__combo_box_2.currentText() == 'Wybierz rekord':
            self.__combo_box_2.move(400, 175)
            self.__combo_box_2.setFixedSize(100, 20)
            self.__combo_box_2.adjustSize()
            self.button_2.setEnabled(False)
            self.button_4.setEnabled(False)
        else:
            self.__combo_box_2.move(500 - (len(self.__combo_box_2.currentText()) + 5) * 5, 175)
            self.__combo_box_2.setFixedSize((len(self.__combo_box_2.currentText()) + 5) * 5, 20)
            print(self.__combo_box_2.currentText())
            print(len(self.__combo_box_2.currentText()))
            self.__combo_box_2.adjustSize()
            self.button_2.setEnabled(True)
            self.button_4.setEnabled(True)

    def create_table(self):
        """
        create table method
        this method initializes new AddTable object and adds table name to combo box 1
        """
        try:
            add_table = AddTableWindow(self.__project_model)
            add_table.setModal(True)
            add_table.exec()
            self.__project_controller.check_table_name(add_table.get_table_name())
            self.__combo_box_1.addItem(add_table.get_table_name())
        except Exception as exception:
            print(exception)

    def add_row(self):
        """
        Add row method
        this method checks if table was chosen from combo box 1 and initializes new Add row window object (if table is chosen)
        """
        try:
            current_table = self.__combo_box_1.currentText()
            self.__project_controller.check_removed_table_name(current_table)
            add_row_window = AddRowWindow(self.__project_model, current_table)
            add_row_window.setModal(True)
            add_row_window.exec()
            self.set_combo_box_2()
        except Exception as exception:
            warning = WarningWindow(str(exception))
            warning.setModal(True)
            warning.exec()

    def remove_table(self):
        """
        Remove table method
        this method checks if table was chosen from combo box 1 and initializes new ConfirmRemoveTableWindow object
        """
        try:
            table_name = self.__combo_box_1.currentText()
            self.__project_controller.check_removed_table_name(table_name)
            confirm = ConfirmRemoveTableWindow(self.__project_model, self.__combo_box_1, table_name)
            confirm.setModal(True)
            confirm.exec()

        except Exception as exception:
            warning = WarningWindow(str(exception))
            warning.setModal(True)
            warning.exec()


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
        this method loads chosen column name, type and calls out addColumn method (Table)
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

class BrowseWindow(QDialog):
    """
    BrowseWindowClass
    """
    def __init__(self, project_model: ProjectModel, table_name: str):
        """
        Load from file class constructor
        :param project_model: ProjectModel
        :param table_name: str
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
        self.setFixedSize(self.__width, self.__height)

        self.__lineedit = QLineEdit(self)
        self.__lineedit.setGeometry(120, 50, 230, 20)

        self.__labels.createLabel('Lambda-wyrażenie:', 20, 50)
        self.button_1 = self.__buttons.create_button('Szukaj', 10, 110, 180, 30, 'Kliknij aby dodać nową kolumne do tabeli',
                                     self.browse)
        self.button_2 = self.__buttons.create_button('Anuluj', 210, 110, 180, 30, 'Kliknij aby dodać tabele', self.close)

        self.button_3 = self.__buttons.create_button('?', 360, 50, 20, 20, 'Kliknij aby wyświetlić przykładowe wyrażenie-lambda',
                                     self.help)

    def browse(self):
        """
        Browse method
        this method loads lambda-expression (typed by user) and displays table only with rows returned by lambda_browse method from ProjectModel
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
        """
        help method
        this method fills lineedit with lambda-expression generated with generate_lambda_expression from ProjectModel
        :return:
        """
        try:
            self.__lineedit.setText(self.__project_model.generate_lambda_expression(self.__table_name))
        except:
            self.close()
            warning = WarningWindow("Brak rekordów w tabeli!")
            warning.setModal(True)
            warning.exec()

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



class EditTableWindow(QDialog):
    """
    Edit table class
    """

    def __init__(self, project_model: ProjectModel, table_name: str):
        """
        Edit table class constructor

        :param project_model: ProjectModel
        :param table_name: str
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

        self.button1 = QPushButton('Dodaj wiersz', self)
        self.button1.clicked.connect(self.add_row)

        self.button2 = QPushButton('Zapisz tabele', self)
        self.button2.clicked.connect(self.save_data)

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
        save_data method
        this method checks if all data typed by user have correct type and
        sets table content in project_model::structure with content loaded from edit_row_window
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


class ConfirmRemoveRowWindow(QDialog):
    """
    Confirm Remove Row window class
    """

    def __init__(self, project_model: ProjectModel, combo_box, table_name):
        """
        Confirm Remove Row window class constructor

        :param project_model: ProjectModel
        :param combo_box: QComboBox
        :param table_name: str
        """
        super().__init__()
        self.__window_title = 'Usunąć wiersz?'
        self.__top = 300
        self.__left = 450
        self.__width = 250
        self.__height = 150
        self.__buttons = MyButton(self)
        self.__Labels = MyLabel(self)
        self.__project_model = project_model
        self.__table_name = table_name
        self.__combo_box = combo_box
        self.init_window()

    def init_window(self):
        """
        Init Window method
        this method sets all window widgets
        """
        self.setGeometry(self.__left, self.__top, self.__width, self.__height)
        self.setFixedSize(self.__width, self.__height)
        self.setWindowTitle(self.__window_title)
        self.__Labels.createLabel(self.__window_title, 90, 45)

        self.button_1 = self.__buttons.create_button('Usuń', 40, 90, 80, 30, 'miau', self.remove)
        self.button_2 = self.__buttons.create_button('Anuluj', 130, 90, 80, 30, 'miau', self.close)

        self.show()

    def remove(self):
        """
        Remove method
        This method removes row from table. This method is called when user clicks the remove button
        :return:
        """
        try:
            chosen_row = self.__combo_box.currentText().strip('[]')
            chosen_row = chosen_row.split(', ')
            chosen_row = [chosen_row[index].strip('\'') for index in range(len(chosen_row))]
            self.__combo_box.removeItem(self.__project_model.get_row_index(self.__table_name, str(chosen_row)) + 1)
            self.__project_model.remove_row(self.__table_name, chosen_row)
            self.close()
        except Exception as e:
            print(e)
            w = WarningWindow('Wystąpiły problemy z usuwaniem wiersza')
            w.setModal(True)
            w.exec()



class ConfirmRemoveTableWindow(QDialog):
    """
    Confirm remove table window class
    """

    def __init__(self, project_model: ProjectModel, combo_box, table_name):
        """
        Confirm remve table window class constructor
        :param projectModel: ProjectModel
        :param comboBox: QComboBox
        :param tableName: str
        """
        super().__init__()
        self.__window_title = 'Usunąć tabele?'
        self.__top = 300
        self.__left = 450
        self.__width = 250
        self.__height = 150
        self.__buttons = MyButton(self)
        self.__Labels = MyLabel(self)
        self.__project_model = project_model
        self.__table_name = table_name
        self.__combo_box = combo_box
        self.init_window()

    def init_window(self):
        """
        Init Window method
        this method sets all window widgets
        """
        self.setGeometry(self.__left, self.__top, self.__width, self.__height)
        self.setFixedSize(self.__width, self.__height)
        self.setWindowTitle(self.__window_title)
        self.__Labels.createLabel(self.__window_title, 90, 45)
        self.button_1 = self.__buttons.create_button('Usuń', 40, 90, 80, 30, 'miau', self.remove)
        self.button_2 = self.__buttons.create_button('Anuluj', 130, 90, 80, 30, 'miau', self.close)
        self.show()

    def remove(self):
        """
        Remove method
        this method is called when user confirm to delete the table by clicking remove button
        :return:
        """
        try:
            index = self.__project_model.return_table_index(self.__project_model.get_structure(), self.__table_name) + 1
            self.__project_model.remove_table(self.__table_name)
            self.__combo_box.removeItem(index)
            self.close()
        except:
            w = WarningWindow('Wystąpiły problemy z usuwaniem wiersza')
            w.setModal(True)
            w.exec()


class WriteFile(QDialog):
    """
    Write to file window class
    """

    def __init__(self, project_model: ProjectModel):
        """
        Write to file class constructor

        :param ProjectModel: Project model (ProjectModel)
        """
        super().__init__()
        self.__title = 'Zapisać strukturę?'
        self.__top = 400
        self.__left = 400
        self.__width = 400
        self.__height = 150
        self.__buttons = MyButton(self)
        self.__labels = MyLabel(self)
        self.__project_model = project_model
        self.init_window()

    def init_window(self):
        """
        Init Window method
        this method sets all window widgets
        """
        self.setWindowTitle(self.__title)
        self.setGeometry(self.__left, self.__top, self.__width, self.__height)
        self.setFixedSize(self.__width, self.__height)

        self.__lineedit = QLineEdit(self)
        self.__lineedit.setGeometry(100, 50, 250, 20)

        self.__labels.createLabel('Ścieżka:', 40, 50)
        self.button_1 = self.__buttons.create_button('Zapisz', 10, 110, 180, 30, 'Kliknij aby zapisać strukturę',
                                     self.write)
        self.button_2 = self.__buttons.create_button('Nie zapisuj', 210, 110, 180, 30, 'Nie zapisuj struktury',
                                     self.close)

    def write(self):
        """
        write method
        this method loads filename from lineedit and calls writeToFile method (ProjectModel)
        """
        try:
            path = self.__lineedit.text()
            self.__project_model.write_to_file(path)

            self.close()
        except:
            warning = WarningWindow('Błąd zapisywania!')
            warning.setModal(True)
            warning.exec()


class LoadFile(QDialog):
    """
    Load from file class
    """

    def __init__(self, project_model: ProjectModel, combo_box: QComboBox):
        """
        Load from file class constructor
        :param project_model: ProjectModel
        :param combo_box: QComboBox
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
        self.__combo_box = combo_box
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
        self.__lineedit.setGeometry(100, 50, 250, 20)

        self.__labels.createLabel('Ścieżka:', 40, 50)
        self.button_1 = self.__buttons.create_button('Wczytaj', 10, 110, 180, 30,
                                     'Kliknij aby dodać nową kolumne do tabeli', self.load)
        self.button_2 = self.__buttons.create_button('Anuluj', 210, 110, 180, 30, 'Kliknij aby dodać tabele', self.close)

    def load(self):
        """
        Load method
        this method calls out readFromFile method (ProjectModel) and adds table names from file to comboBox
        """
        try:

            path = self.__lineedit.text()
            self.__project_model.read_from_file(path)

            self.__combo_box.clear()
            self.__combo_box.addItem('Wybierz tabele')
            for table in self.__project_model.get_structure():
                self.__combo_box.addItem(table.get_table_name())
            self.close()

        except Exception as exception:
            self.close()
            warning = WarningWindow(str(exception))
            warning.setModal(True)
            warning.exec()



class WarningWindow(QDialog):
    """
    Warning Window class
    """

    def __init__(self, warning_text: str):
        """
        Warning window class constructor
        :param warning_text: str
        """
        super().__init__()
        self.__window_title = 'Uwaga'
        self.__top = 300
        self.__left = 450
        self.__width = 250
        self.__height = 150
        self.__buttons = MyButton(self)
        self.__labels = MyLabel(self)
        self.__text = warning_text
        self.init_window()

    def init_window(self):
        """
        Init Window function
        this function sets all window widgets
        """
        self.setGeometry(self.__left, self.__top, self.__width, self.__height)
        self.setFixedSize(self.__width, self.__height)
        self.setWindowTitle(self.__window_title)
        self.__labels.createLabel(self.__text, 50, 45)
        self.button_1 = self.__buttons.create_button('Rozumiem', 75, 90, 100, 30, 'miau', self.close)
        self.show()


class MyButton:
    """
    MyButton class
    """

    def __init__(self, window):
        """
        MyButton class constructor

        :param window: window object (type(window))
        """
        self.__window = window

    def create_button(self, text, x_coordinate, y_coordinate, width, height, tip, fun):
        """
        Create buttons function

        :param text: button content (str)
        :param x_coordinate: x axis coordinate (float)
        :param y_coordinate: y axis coordinate (float)
        :param width: button width (float)
        :param height: button height (float)
        :param tip: button tip (str)
        :param fun: button clicked function (function)
        """
        button = QPushButton(text, self.__window)
        button.setGeometry(QRect(x_coordinate, y_coordinate, width, height))
        button.setToolTip(tip)
        button.clicked.connect(fun)

        return button


class MyLabel:
    """
    MyLabel class
    """
    def __init__(self,window):
        """
        MyLabel class constructor

        :param window: window object (type(window))
        """
        self.__window=window

    def createLabel(self,text,x_coordinate, y_coordinate):
        """
        Create label function

        :param text: label content (str)
        :param x_coordinate: x axis coordinate (float)
        :param y_coordinate: y axis coordinate (float)
        """
        label = QLabel(self.__window)
        label.setText(text)
        label.adjustSize()
        label.move(x_coordinate, y_coordinate)