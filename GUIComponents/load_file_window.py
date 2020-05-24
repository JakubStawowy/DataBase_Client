from PyQt5.QtWidgets import QComboBox, QDialog, QLineEdit
from GUIComponents.warning_window import WarningWindow
from my_button import MyButton
from my_label import MyLabel
from project_model import ProjectModel


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
        self.setFixedSize(400, 150)

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
