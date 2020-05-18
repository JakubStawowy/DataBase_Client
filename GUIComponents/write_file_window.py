from PyQt5.QtWidgets import QDialog, QLineEdit

from GUIComponents.warning_window import WarningWindow
from my_button import MyButton
from my_label import MyLabel
from project_model import ProjectModel


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
        self.setFixedSize(400, 150)

        self.__lineedit = QLineEdit(self)
        self.__lineedit.setGeometry(100, 50, 250, 20)

        self.__labels.createLabel('Ścieżka:', 40, 50)
        self.__buttons.create_button('Zapisz', 10, 110, 180, 30, 'Kliknij aby zapisać strukturę',
                                     self.write)
        self.__buttons.create_button('Nie zapisuj', 210, 110, 180, 30, 'Nie zapisuj struktury',
                                     self.close)

    def write(self):
        """
        write method
        this method calls out writeToFile method (ProjectModel)
        """
        try:
            path = self.__lineedit.text()
            self.__project_model.write_to_file(path)

            self.close()
        except:
            warning = WarningWindow('Błąd zapisywania!')
            warning.setModal(True)
            warning.exec()
