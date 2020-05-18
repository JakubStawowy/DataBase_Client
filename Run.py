import sys

from PyQt5.QtWidgets import QApplication

from GUIComponents.main_window import MainWindow
from project_model import ProjectModel

if __name__=='__main__':

    App=QApplication(sys.argv)
    MainWindow(ProjectModel())
    sys.exit(App.exec())