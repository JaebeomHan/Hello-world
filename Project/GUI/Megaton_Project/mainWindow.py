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
        exitAction.triggered.connect(qApp.quit)

        openFileAction = QAction('Open', self)
        openFileAction = QAction(QIcon('Megaton_Project\file.png'), 'Open', self)
        openFileAction.setShortcut('Ctrl+O')
        openFileAction.setStatusTip('Open New File')
        openFileAction.triggered.connect(self.openFileAction)

        ## 메뉴바에 FIle 추가
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)
        filemenu.addAction(openFileAction)

        ## 툴바
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        self.toolbar = self.addToolBar('Open')
        self.toolbar.addAction(openFileAction)

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

    def openFileAction(self): # 파일 오픈 누르면 뜨는 창
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def inputUserInfo(self):
        text, ok = QInputDialog.getText(self, 'Welcome', 'Please enter your affiliation:')

        if ok:
            self.userInfoSlot.setText(str(text))



