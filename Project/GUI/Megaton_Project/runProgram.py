import sys
from PyQt5.QtWidgets import *
from mainWindow import mainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    firstProgram = mainWindow()
    sys.exit(app.exec_())