
from PyQt5.QtWidgets import QLabel


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