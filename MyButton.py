
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QPushButton

class MyButton():
    """
    MyButton class
    """
    def __init__(self, window):
        """
        MyButton class constructor

        :param window: window object (type(window))
        """
        self.__window=window

    def CreateButtons(self, text: str, x:float, y:float, w:float, h:float, icon: str, ix:float, iy:float, tip: str,fun):
        """
        Create buttons function

        :param text: button content (str)
        :param x: x axis coordinate (float)
        :param y: y axis coordinate (float)
        :param w: button width (float)
        :param h: button height (float)
        :param icon: button icon path (str)
        :param ix: button icon width (float)
        :param iy: button icon height (float)
        :param tip: button tip (str)
        :param fun: button clicked function (function)
        """
        self.__window.button = QPushButton(text, self.__window)
        self.__window.button.setGeometry(QRect(x, y, w, h))
        self.__window.button.setIcon(QtGui.QIcon(icon))
        self.__window.button.setIconSize(QtCore.QSize(ix, iy))
        self.__window.button.setToolTip(tip)
        self.__window.button.clicked.connect(fun)

