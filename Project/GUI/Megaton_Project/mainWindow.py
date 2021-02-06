import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import * # 어떤 클래스를 썼는지 확인이 힘듦
from MainWidget import MainWidget

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setMainWindow()

    def setMainWindow(self):

        ## 창 제목 및 크기
        self.setWindowTitle('Welcome to Megaton Project')
        self.setGeometry(300, 300, 1000, 600)
        self.setFixedSize(1000, 600)

        ## 상태 표시줄
        self.statusBar().showMessage('imcomplete version')
        self.statusBar()

        ## 단축키 설정
        exitAction = QAction('Exit', self)
        exitAction = QAction(QIcon('Project\GUI\Megaton_Project\exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QApplication.quit)

        ## 메뉴바에 FIle 추가
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        ## MainWidget 객체 생성
        setMainWidget = MainWidget()
        self.setCentralWidget(setMainWidget)

        ## 창을 화면 중앙으로
        self.center()

        ## 창 보여줘!
        self.show()

    def center(self): # 창 중앙으로 띄워주는 함수 정의
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event): # 창 닫을 때 다시 한번 물어보기
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

