import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
<<<<<<< HEAD
from PyQt5.QtGui import *
from fileInputWindow import *

class mainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.mainWindow()

    def mainWindow(self):
=======
from PyQt5.QtGui import * # 어떤 클래스를 썼는지 확인이 힘듦
from MainWidget import MainWidget

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setMainWindow()

    def setMainWindow(self):
>>>>>>> f7c77dfeeb2bf75198fa3dd3b50059d66c014f4f

        ## 창 제목 및 크기
        self.setWindowTitle('Welcome to Megaton Project')
        self.setGeometry(300, 300, 1000, 600)
<<<<<<< HEAD

        ## 상태 표시줄
        self.statusBar().showMessage('imcomplete version')

        ## 메뉴 - Exit
        exitAction = QAction(QIcon('Project\GUI\Megaton_Project\exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

=======
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
>>>>>>> f7c77dfeeb2bf75198fa3dd3b50059d66c014f4f
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

<<<<<<< HEAD
        ## Exit 툴바
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
=======
        ## MainWidget 객체 생성
        setMainWidget = MainWidget()
        self.setCentralWidget(setMainWidget)
>>>>>>> f7c77dfeeb2bf75198fa3dd3b50059d66c014f4f

        ## 창을 화면 중앙으로
        self.center()

<<<<<<< HEAD
        layout = QVBoxLayout()
        layout.addStretch(1)
        label = QLabel("사용자 정보를 입력하세요.")
        label.setAlignment(Qt.AlignCenter)
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)

        self.label = label

        btn = QPushButton("입력")
        btn.clicked.connect(self.onButtonClicked)
        layout.addWidget(label)
        layout.addWidget(btn)
        layout.addStretch(1)
        centralWidget = QWidget()
        centralWidget.setLayout(layout)

        self.setCentralWidget(centralWidget)

        ## 창 보여줘!
        self.show()

    def onButtonClicked(self):
        win = SubWindow()
        r = win.showModal()
        if r:
            text = win.edit.text()
            self.label.setText(text)

    def show(self):
        super().show()

    def center(self):
=======
        ## 창 보여줘!
        self.show()

    def center(self): # 창 중앙으로 띄워주는 함수 정의
>>>>>>> f7c77dfeeb2bf75198fa3dd3b50059d66c014f4f
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

<<<<<<< HEAD
        
=======
    def closeEvent(self, event): # 창 닫을 때 다시 한번 물어보기
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

>>>>>>> f7c77dfeeb2bf75198fa3dd3b50059d66c014f4f
