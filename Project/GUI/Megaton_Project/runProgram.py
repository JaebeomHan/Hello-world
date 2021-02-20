
import sys
sys.dont_write_bytecode = True
from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    runProgram = MainWindow()
    sys.exit(app.exec_())