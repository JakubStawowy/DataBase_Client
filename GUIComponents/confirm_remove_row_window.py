from PyQt5.QtWidgets import QDialog
from GUIComponents.warning_window import WarningWindow
from my_button import MyButton
from my_label import MyLabel
from project_model import ProjectModel


class ConfirmRemoveRowWindow(QDialog):
    """
    Confirm Remove Row window class
    """

    def __init__(self, project_model: ProjectModel, combo_box, table_name):
        """
        Confirm Remove Row window class constructor

        :param projectModel: ProjectModel
        :param comboBox: QComboBox
        :param tableName: str
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

        self.setGeometry(self.__left, self.__top, self.__width, self.__height)
        self.setFixedSize(250, 150)
        self.setWindowTitle(self.__window_title)
        self.__Labels.createLabel(self.__window_title, 90, 45)
        self.__buttons.create_button('Usuń', 40, 90, 80, 30, 'miau', self.remove)
        self.__buttons.create_button('Anuluj', 130, 90, 80, 30, 'miau', self.close)
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
        except:
            w = WarningWindow('Wystąpiły problemy z usuwaniem wiersza')
            w.setModal(True)
            w.exec()
