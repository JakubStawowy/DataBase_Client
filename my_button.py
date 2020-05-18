from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QPushButton


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
        self.__window.button = QPushButton(text, self.__window)
        self.__window.button.setGeometry(QRect(x_coordinate, y_coordinate, width, height))
        self.__window.button.setToolTip(tip)
        self.__window.button.clicked.connect(fun)
