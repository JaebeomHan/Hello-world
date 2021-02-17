import sys
from PyQt5.QtWidgets import *
from MainWindow import MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    runProgram = MainWindow()
    sys.exit(app.exec_())