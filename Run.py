import sys

from PyQt5.QtWidgets import QApplication

from GUIComponents.MainWindow import MainWindow
from ProjectModel import ProjectModel

if __name__=='__main__':

    App=QApplication(sys.argv)
    MainWindow(ProjectModel())
    sys.exit(App.exec())