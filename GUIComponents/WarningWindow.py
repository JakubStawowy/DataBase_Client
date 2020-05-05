
from PyQt5.QtWidgets import QDialog

from MyButton import MyButton
from MyLabel import MyLabel


class WarningWindow(QDialog):
    """
    Warning Window class
    """
    def __init__(self, warningText:str):
        """
        Warning window class constructor
        :param warningText: text (str)
        """
        super().__init__()
        self.__windowTitle = 'Uwaga'
        self.__top=300
        self.__left=450
        self.__width = 250
        self.__height=150
        self.__buttons = MyButton(self)
        self.__Labels = MyLabel(self)
        self.__text = warningText
        self.InitWindow()

    def InitWindow(self):
        self.setGeometry(self.__left,self.__top,self.__width,self.__height)
        self.setFixedSize(250,150)
        self.setWindowTitle(self.__windowTitle)
        self.__Labels.createLabel(self.__text,50,45)
        self.__buttons.CreateButtons('Rozumiem',75,90,100,30,'none',0,0,'miau',self.close)
        self.show()