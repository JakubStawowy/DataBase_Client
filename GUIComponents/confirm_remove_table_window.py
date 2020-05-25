from PyQt5.QtWidgets import QDialog

from GUIComponents.warning_window import WarningWindow
from my_widgets import MyButton
from my_widgets import MyLabel
from model_controller import ProjectModel


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
