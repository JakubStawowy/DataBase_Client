
from PyQt5.QtWidgets import QDialog

from GUIComponents.WarningWindow import WarningWindow
from MyButton import MyButton
from MyLabel import MyLabel

class ConfirmRemoveTableWindow(QDialog):
    """
    Confirm remove table window class
    """
    def __init__(self, projectModel,comboBox ,tableName):
        """
        Confirm remve table window class constructor
        :param projectModel: ProjectModel
        :param comboBox: QComboBox
        :param tableName: str
        """
        super().__init__()
        self.__windowTitle = 'Usunąć tabele?'
        self.__top=300
        self.__left=450
        self.__width = 250
        self.__height=150
        self.__buttons = MyButton(self)
        self.__Labels = MyLabel(self)
        self.__projectModel=projectModel
        self.__tableName=tableName
        self.__comboBox=comboBox
        self.InitWindow()

    def InitWindow(self):
        self.setGeometry(self.__left,self.__top,self.__width,self.__height)
        self.setFixedSize(250,150)
        self.setWindowTitle(self.__windowTitle)
        self.__Labels.createLabel(self.__windowTitle,90,45)
        self.__buttons.CreateButtons('Usuń',40,90,80,30,'none',0,0,'miau',self.remove)
        self.__buttons.CreateButtons('Anuluj',130,90,80,30,'none',0,0,'miau',self.close)
        self.show()

    def remove(self):
        """
        Remove method
        this method is called when user confirm to delete the table by clicking remove button
        :return:
        """
        try:
            index = self.__projectModel.returnTableIndex(self.__projectModel.getStructure(), self.__tableName) + 1
            self.__projectModel.removeTable(self.__tableName)
            self.__comboBox.removeItem(index)
            self.close()
        except:
            w = WarningWindow('Wystąpiły problemy z usuwaniem wiersza')
            w.setModal(True)
            w.exec()