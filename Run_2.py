import sys

from PyQt5.QtWidgets import QApplication

from database_graphical import MainWindow
from database_logic import ProjectModel

if __name__ == '__main__':
    App = QApplication(sys.argv)
    MainWindow(ProjectModel())
    sys.exit(App.exec())