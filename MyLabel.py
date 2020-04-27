
from PyQt5.QtWidgets import QPushButton, QLabel


class MyLabel():
    """
    MyLabel class
    """
    def __init__(self,window):
        """
        MyLabel class constructor

        :param window: window object (type(window))
        """
        self.__window=window

    def createLabel(self,text:str,x:float,y:float):
        """
        Create label function

        :param text: label content (str)
        :param x: x axis coordinate (float)
        :param y: y axis coordinate (float)
        """
        label = QLabel(self.__window)
        label.setText(text)
        label.adjustSize()
        label.move(x, y)

