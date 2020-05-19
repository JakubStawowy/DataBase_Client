from PyQt5.QtWidgets import QMainWindow, QComboBox

from GUIComponents.add_row_window import AddRowWindow
from GUIComponents.add_table_window import AddTableWindow
from GUIComponents.browse_window import BrowseWindow
from GUIComponents.confirm_remove_row_window import ConfirmRemoveRowWindow
from GUIComponents.confirm_remove_table_window import ConfirmRemoveTableWindow
from GUIComponents.edit_row_window import EditRowsWindow
from GUIComponents.edit_table_window import EditTableWindow
from GUIComponents.load_file_window import LoadFile
from GUIComponents.warning_window import WarningWindow
from GUIComponents.write_file_window import WriteFile
from my_button import MyButton
from my_label import MyLabel
from project_controller import ProjectController
from project_model import ProjectModel
from table import Table


class MainWindow(QMainWindow):
    """
    Main window class
    """

    def __init__(self, project_model: ProjectModel):
        """
        Main window class constructor
        Constructor sets basic parameters (title, position, MyButton class, MyLabel class)

        Argument 1: ProjectModel class (Data storage class with logical methods)
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
        :return:
        """
        self.writeFile = WriteFile(self.__project_model)
        self.writeFile.setModal(True)
        self.writeFile.exec()
        self.close()

    def browse(self):
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
        this method calls out removeRow method (ProjectModel)
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
        self.button_1.setEnabled(True)

    def edit_table(self):
        """
        Edit table method
        this method initializes new editTable object (editTable's constructor argument is chosen table in comboBox1)
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
        Set comboBox2 method
        this method adds chosen table's (from comboBox1) rows to comboBox2
        """
        try:
            table_name = self.__combo_box_1.currentText()
            index = len(self.__combo_box_2) - 1
            while (index > 0):
                self.__combo_box_2.removeItem(index)
                index = index - 1
            for index in range(self.__project_model.get_table_number_of_rows(table_name)):
                self.__combo_box_2.addItem(str(self.__project_model.get_table_row(table_name, index)))

            self.button_3.setEnabled(True)
            self.button_5.setEnabled(True)
            self.button_7.setEnabled(True)

        except Exception:

            self.button_3.setEnabled(False)
            self.button_5.setEnabled(False)
            self.button_7.setEnabled(False)

    def combo_box_2_changed(self):
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
        Create table function
        this function initializes new AddTable object and adds table name to combobox
        """
        try:
            add_table = AddTableWindow(self.__project_model)
            add_table.setModal(True)
            add_table.exec()
            self.__project_controller.check_table_name(add_table.get_table_name())
            self.__combo_box_1.addItem(add_table.get_table_name())
            self.button_1.setEnabled(True)
        except Exception as exception:
            print(exception)

    def add_row(self):
        """
        Add row method
        this method initializes new Add row window object (if table is chosen)
        """
        try:
            current_table = self.__combo_box_1.currentText()
            self.__project_controller.check_removed_table_name(current_table)
            add_row_window = AddRowWindow(self.__project_model, current_table)
            add_row_window.setModal(True)
            add_row_window.exec()
        except Exception as exception:
            warning = WarningWindow(str(exception))
            warning.setModal(True)
            warning.exec()

    def remove_table(self):
        """
        Remove table method
        this method calls out removeTAble method (ProjectModel)
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
