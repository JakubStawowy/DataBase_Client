
from PyQt5.QtWidgets import QDialog, QLineEdit

from GUIComponents.WarningWindow import WarningWindow
from MyButton import MyButton
from MyLabel import MyLabel
from ProjectModel import ProjectModel

class WriteFile(QDialog):
    """
    Write to file window class
    """
    def __init__(self, projectModel:ProjectModel):
        """
        Write to file class constructor

        :param ProjectModel: Project model (ProjectModel)
        """
        super().__init__()
        self.__title='Zapisać strukturę?'
        self.__top=400
        self.__left=400
        self.__width=400
        self.__height=150
        self.__buttons=MyButton(self)
        self.__labels=MyLabel(self)
        self.__projectModel=projectModel
        self.InitWindow()
    def InitWindow(self):
        """
        Init Window method
        this method sets all window widgets
        """
        self.setWindowTitle(self.__title)
        self.setGeometry(self.__left, self.__top, self.__width, self.__height)
        self.setFixedSize(400, 150)

        self.__lineedit = QLineEdit(self)
        self.__lineedit.setGeometry(100,50,250,20)
        #self.__lineedit.move(100, 50)

        self.__labels.createLabel('Ścieżka:', 40, 50)
        self.__buttons.CreateButtons('Zapisz', 10, 110, 180, 30, 'none', 40, 40, 'Kliknij aby zapisać strukturę', self.write)
        self.__buttons.CreateButtons('Nie zapisuj', 210, 110, 180, 30, 'none', 40, 40, 'Nie zapisuj struktury',self.close)

    def write(self):
        """
        write method
        this method calls out writeToFile method (ProjectModel)
        """
        try:
            path=self.__lineedit.text()
            self.__projectModel.writeToFile(path)

            self.close()
        except:
            warning=WarningWindow('Błąd zapisywania!')
            warning.setModal(True)
            warning.exec()
