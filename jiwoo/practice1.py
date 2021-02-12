import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class helloWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        self.lbl.setText('result here')

        mainTitle = QLabel('Megaton Project', self)
        mainTitle.setAlignment(Qt.AlignCenter)
        mainTitle.move(0,-100)
        mainTitle.resize(1000,500)

        subTitle = QLabel('활성화 에너지 구해줌', self)
        subTitle.setAlignment(Qt.AlignVCenter)
        subTitle.move(430,-50)
        subTitle.resize(1000,500)

        madeBy = QLabel('만든이 : 최지우 이경훈 한재범', self)
        madeBy.setAlignment(Qt.AlignCenter)
        madeBy.move(300,200)
        madeBy.resize(1000,500)

        result = QLabel('result : ', self)
        result.setAlignment(Qt.AlignCenter)
        result.move(100,100)
        result.resize(1000,500)

        font1 = mainTitle.font()
        font1.setPointSize(30)

        font2 = subTitle.font()
        font2.setFamily('Times New Roman')
        font2.setBold(True)

        mainTitle.setFont(font1)
        subTitle.setFont(font2)

        layout = QVBoxLayout()
        layout.addWidget(mainTitle)
        layout.addWidget(subTitle)
        layout.addWidget(madeBy)

        layout.addWidget(self.lbl)

        # 하단 Megaton 문구
        self.statusBar().showMessage('Megaton')
        self.resize(1000, 600)
        self.center()

        # 종료 단축키
        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        # 파일 오픈 단축키
        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open New File')
        openFile.triggered.connect(self.openFile)

        # 메뉴바와 File탭
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(openFile)
        filemenu.addAction(exitAction)

        # 종료 버튼
        exitBtn = QPushButton('Quit', self)
        exitBtn.move(800, 500)
        exitBtn.resize(exitBtn.sizeHint())
        exitBtn.clicked.connect(QCoreApplication.instance().quit)

        # 사용자 정보 입력 버튼
        self.userInfoBtn = QPushButton('ID', self)
        self.userInfoBtn.move(250,250)
        self.userInfoBtn.clicked.connect(self.inputUserInfo)

        self.run = QPushButton('run', self)
        self.run.move(250,250)
        self.run.clicked.connect(self.function_open)

        # 사용자 정보 입력 칸
        self.userInfoSlot = QLineEdit(self)
        self.userInfoSlot.move(370, 250)
        self.userInfoSlot.resize(300, 30)

        # 제목
        self.setWindowTitle('Welcome to Megaton Project')

        # 화면 띄우는 메소드
        self.show()

    def inputUserInfo(self):
        text, ok = QInputDialog.getText(self, 'Welcome', 'Please enter your affiliation:')

        if ok:
            self.userInfoSlot.setText(str(text))

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def openFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def function_open(self) :
        energy1 = float(self.calculate_reactant1_energy.text('gv5_w10.txt'))
        self.lbl.setNum(energy1)
        self.lbl.adjustSize()

    def calculate_reactant1_energy(file):
        with open(file, 'r', encoding='UTF8') as f:
            saved_data = []
            hf_list = []
            for line in f.readlines()[::-1]:
                if 'HF=' in line:
                    text = line.split("\\")
                    saved_data.extend(text)

                    break

            for text in saved_data:
                if 'HF=' in text:
                    hf_list.append(text)
                    energy = [i.lstrip('HF=') for i in hf_list]






if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = helloWindow()
   sys.exit(app.exec_())