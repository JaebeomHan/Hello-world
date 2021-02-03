import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from fileInputWindow import *

class mainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.mainWindow()

    def mainWindow(self):

        ## 창 제목 및 크기
        self.setWindowTitle('Welcome to Megaton Project')
        self.setGeometry(300, 300, 1000, 600)

        ## 상태 표시줄
        self.statusBar().showMessage('imcomplete version')

        ## 메뉴 - Exit
        exitAction = QAction(QIcon('Project\GUI\Megaton_Project\exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        ## Exit 툴바
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        ## 창을 화면 중앙으로
        self.center()

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
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        