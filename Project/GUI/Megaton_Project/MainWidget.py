import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QAction, QVBoxLayout, QHBoxLayout, QComboBox, QGridLayout, QMessageBox,
                            QDesktopWidget, QLabel, QLineEdit, QInputDialog, QFileDialog, QDialog, QTextEdit)
from PyQt5.QtCore import QCoreApplication, Qt
from energy import fileopen

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

        ## 기능 시작 버튼 - 파일을 읽기만 함!
        self.startProgram = QPushButton('시작하기', self)
        self.startProgram.move(530, 249)
        self.startProgram.resize(150, 72)
        self.startProgram.clicked.connect(self.dialogOpen)

        ## QDialog 설정
        self.dialog = QDialog()

        ## 프로그램 설명 버튼
        self.programExplanation = QPushButton('프로그램 설명', self)
        self.programExplanation.move(860, 400)
        self.programExplanation.resize(110, 40)
        self.programExplanation.clicked.connect(self.helpMe)

        ## 만든이 버튼
        self.madeByBtn = QPushButton('만든이', self)
        self.madeByBtn.move(860, 450)
        self.madeByBtn.resize(110, 40)
        self.madeByBtn.clicked.connect(self.madeByInfo)

        ## 사용자 정보 콤보박스
        self.userProfile = QComboBox(self)
        self.userProfile.addItem('직업을 선택하시오.')
        self.userProfile.addItem('학부생')
        self.userProfile.addItem('대학원생')
        self.userProfile.addItem('교수님')
        self.userProfile.addItem('연구원')
        self.userProfile.move(320, 250)
        self.userProfile.resize(170, 30)

        ## 
        self.btn = QPushButton('학과', self)
        self.btn.move(319, 290)
        self.btn.resize(50, 30)
        self.btn.clicked.connect(self.showDepartmentDialog)

        self.le = QLineEdit(self)
        self.le.move(380, 290)
        self.le.resize(110, 30)

    ## 만든이 정보 함수
    def madeByInfo(self):
        LEADERMadeBy = QLabel('Leader : 최지우')
        GUIMadeBy = QLabel('GUI : 한재범')
        DATABASEMadeby = QLabel('Database : 이경훈')
        btnMadeBy = QPushButton("Close", self.dialog)
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

    def helpMe(self):
        helpMe = QLabel(
            '''이 프로그램은 사용자의....... 활성화 에너지를 구해줍니다.
            문의 사항이 있으시면 리더에게 개인적으로 연락 바랍니다.''')
        btnHelpMe = QPushButton("Close", self.dialog)
        btnHelpMe.clicked.connect(self.dialogClose)

        gridOfHelpMe = QGridLayout()
        self.dialog.setLayout(gridOfHelpMe)

        gridOfHelpMe.addWidget(helpMe, 0, 0)
        gridOfHelpMe.addWidget(btnHelpMe, 1, 00)

        self.dialog.setWindowTitle('프로그램 설명')
        self.dialog.setWindowModality(Qt.ApplicationModal)

        self.dialog.resize(500, 500)
        self.dialog.setFixedSize(500, 500)
        self.dialog.show()

    ## 여기서부터 Dialog
    def dialogOpen(self):
        
        ## ok 버튼
        self.dialog.closeBtn = QPushButton("OK", self.dialog)
        self.dialog.closeBtn.move(570, 750)
        self.dialog.closeBtn.clicked.connect(self.dialogClose)
        self.dialog.textEdit = QTextEdit(self.dialog)
        self.dialog.textEdit.move(50, 20)
        self.dialog.textEdit.resize(1100, 700)

        fileLoadBtn = QPushButton("파일 불러오기", self.dialog)
        fileLoadBtn.move(200, 200)

        ## QDialog 세팅
        self.dialog.setWindowTitle('Dialog')
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.resize(1200, 800)

        fname = QFileDialog.getOpenFileName(self, 'Open File', '',
                                            'text File(*.txt)')
        if fname[0]:
            ## 텍스트 파일 내용 읽기
            f = open(fname[0], 'r', encoding='UTF8') ## Path 정보로 파일을 읽는다.
            with f:
                data = f.read()
                self.dialog.textEdit.setText(fileopen(data))
        else:
            QMessageBox.about(self, 'Warning', '파일을 선택하지 않았습니다.')


        self.dialog.show()

    ## Dialog 닫기 이벤트
    def dialogClose(self):
        self.dialog.close()
    
    def showDepartmentDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')

        if ok:
            self.le.setText(str(text))