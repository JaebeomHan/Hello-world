import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *

class MainWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.setMainWidget()

    def setMainWidget(self):

        ## 제목과 부제목
        mainTitle = QLabel('Megaton Project', self)
        mainTitle.setAlignment(Qt.AlignCenter)
        mainTitle.move(0,-100)
        mainTitle.resize(1000,500)

        subTitle = QLabel('활성화 에너지 구해줌', self)
        subTitle.setAlignment(Qt.AlignCenter)
        subTitle.move(0,-50)
        subTitle.resize(1000,500)

        ## 글씨 크기와 모양 설정
        mainTitleFont = mainTitle.font()
        mainTitleFont.setPointSize(30)

        subTitleFont = subTitle.font()
        subTitleFont.setPointSize(15)

        mainTitle.setFont(mainTitleFont)
        subTitle.setFont(subTitleFont)

        labelLayout = QHBoxLayout()
        labelLayout.addWidget(mainTitle)
        labelLayout.addWidget(subTitle)

        # 사용자 정보 입력 버튼
        self.userInfoBtn = QPushButton('시작하기', self)
        self.userInfoBtn.move(520, 250)
        self.userInfoBtn.resize(100, 30)

        # 프로그램 설명 버튼
        self.programExplanation = QPushButton('프로그램 설명', self)
        self.programExplanation.move(850, 400)
        self.programExplanation.resize(110, 40)

        # 만든이 버튼
        self.madeByBtn = QPushButton('만든이', self)
        self.madeByBtn.move(850, 450)
        self.madeByBtn.resize(110, 40)
        self.madeByBtn.clicked.connect(self.madeByInfo)

        # 사용자 정보 콤보박스
        userPrifile = QComboBox(self)
        userPrifile.addItem('학부생')
        userPrifile.addItem('대학원생')
        userPrifile.addItem('교수님')
        userPrifile.addItem('연구원')
        userPrifile.move(350, 250)
        userPrifile.resize(150, 30)

    def inputUserInfo(self):
        text, ok = QInputDialog.getText(self, 'Welcome', '소속을 입력하세요.')

        if ok:
            self.userInfoSlot.setText(str(text))
            ok.clicked.connect(self.madeByInfo)

    def madeByInfo(self):
        LEADERMadeBy = QLabel('Leader : 최지우')
        GUIMadeBy = QLabel('GUI : 한재범')
        DATABASEMadeby = QLabel('Database : 이경훈')
        btnMadeBy = QPushButton("OK", self.dialog)
        btnMadeBy.clicked.connect(self.dialogClose)

        self.dialog.setWindowTitle('만든이')
        self.dialog.setWindowModality(Qt.ApplicationModal)

        gridOfMadeBy = QGridLayout()
        self.dialog.setLayout(gridOfMadeBy)

        gridOfMadeBy.addWidget(LEADERMadeBy, 0, 0)
        gridOfMadeBy.addWidget(GUIMadeBy, 1, 0)
        gridOfMadeBy.addWidget(DATABASEMadeby, 2, 0)
        gridOfMadeBy.addWidget(btnMadeBy, 3, 0)

        self.dialog.resize(300, 250)
        self.dialog.setFixedSize(200, 180)
        self.dialog.show()

    def dialogClose(self):
        self.dialog.close()

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()
