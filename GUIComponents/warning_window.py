from PyQt5.QtWidgets import QDialog

from my_button import MyButton
from my_label import MyLabel


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
        self.setFixedSize(250, 150)
        self.setWindowTitle(self.__window_title)
        self.__labels.createLabel(self.__text, 50, 45)
        self.button_1 = self.__buttons.create_button('Rozumiem', 75, 90, 100, 30, 'miau', self.close)
        self.show()
