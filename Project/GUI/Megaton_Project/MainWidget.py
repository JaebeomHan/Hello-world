import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QAction, QVBoxLayout, QHBoxLayout, QComboBox, QGridLayout, QMessageBox,
                            QDesktopWidget, QLabel, QLineEdit, QInputDialog, QFileDialog, QDialog, QTextEdit)
from PyQt5.QtCore import QCoreApplication, Qt
from calculate_reactant1_energy import calculate_reactant1_energy

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

        ## 기능 시작 버튼
        self.startProgram = QPushButton('시작하기', self)
        self.startProgram.move(530, 249)
        self.startProgram.resize(150, 72)
        self.startProgram.clicked.connect(self.programRunDialog)

        ## dialog 설정
        self.programRunDialog = QDialog()
        self.madeByDialog = QDialog()
        self.helpMeDialog = QDialog()

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
        LEADER = QLabel('Leader : 최지우')
        GUI = QLabel('GUI : 한재범')
        DATABASE = QLabel('Database : 이경훈')
        btnMadeBy = QPushButton("Close", self.madeByDialog)
        btnMadeBy.clicked.connect(self.closeDialog)

        self.madeByDialog.setWindowTitle('만든이')
        self.madeByDialog.setWindowModality(Qt.ApplicationModal)

        LEADER.move(50, 50)
        btnMadeBy.resize(100, 30)
        btnMadeBy.move(100, 160)

        self.madeByDialog.setFixedSize(200, 180)
        self.madeByDialog.show()

    ## 도움말 Dialog
    def helpMe(self):
        labelHelpMe = QLabel(
            '''이 프로그램은 사용자의....... 활성화 에너지를 구해줍니다.
            문의 사항이 있으시면 리더에게 개인적으로 연락 바랍니다.''')
        btnHelpMe = QPushButton("Close", self.helpMeDialog)
        btnHelpMe.clicked.connect(self.closeDialog)

        layout = QVBoxLayout()
        layout.addWidget(labelHelpMe)
        layout.addWidget(btnHelpMe)
        self.helpMeDialog.setLayout(layout)

        self.helpMeDialog.setWindowTitle("프로그램 설명")
        self.helpMeDialog.setWindowModality(Qt.ApplicationModal)

        self.helpMeDialog.setFixedSize(500, 500)
        self.helpMeDialog.show()

    ## 파일 열어서 지우가 만든 함수 실행
    def fileOpenDialog(self):

        fname = QFileDialog.getOpenFileName(self, "Open File : ", "", "text File(*.txt)")
        if fname[0]:
            ## 텍스트 파일 내용 읽기
            f = open(fname[0], 'r', encoding="UTF8") # 파일을 읽는다.
            with f:
                data = calculate_reactant1_energy(f)
              #  self.dialog.textEdit.setText(data) # data는 str 형식이니 참고바람
                return data
        else:
            QMessageBox.about(self, 'Warning', '파일을 선택하지 않았습니다.')

    ## Dialog 닫기 이벤트
    def closeDialog(self):
        self.madeByDialog.close()
        self.helpMeDialog.close()

    ## 부서 입력 Dialog
    def showDepartmentDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')

        if ok:
            self.le.setText(str(text))

        self.dialog.show()

    ## 메인 기능 실행 Dialog
    def programRunDialog(self):

        self.programRunDialog.setFixedSize(500, 500)

        self.programRunDialog.reactant1 = QPushButton("반응물1", self.programRunDialog)
        self.programRunDialog.reactant2 = QPushButton("반응물2", self.programRunDialog)
        self.programRunDialog.reactant3 = QPushButton("전이구조", self.programRunDialog)
        self.programRunDialog.textEdit1 = QTextEdit(self.programRunDialog)
        self.programRunDialog.textEdit2 = QTextEdit(self.programRunDialog)
        self.programRunDialog.textEdit3 = QTextEdit(self.programRunDialog)

        self.programRunDialog.reactant1.resize(100, 30)
        self.programRunDialog.reactant2.resize(100, 30)
        self.programRunDialog.reactant3.resize(100, 30)
        self.programRunDialog.textEdit1.resize(100, 100)
        self.programRunDialog.textEdit2.resize(100, 100)
        self.programRunDialog.textEdit3.resize(100, 100)

        self.programRunDialog.reactant1.move(100, 30)
        self.programRunDialog.reactant2.move(250, 30)
        self.programRunDialog.reactant3.move(400, 30)
        self.programRunDialog.textEdit1.move(100, 300)
        self.programRunDialog.textEdit2.move(250, 300)
        self.programRunDialog.textEdit3.move(400, 300)

        data = self.programRunDialog.reactant1.clicked.connect(self.fileOpenDialog)
        self.programRunDialog.textEdit1.setText("data")

        self.programRunDialog.setWindowTitle("Dialog")
        self.programRunDialog.setWindowModality(Qt.ApplicationModal)
        self.programRunDialog.setFixedSize(600, 500)

        self.programRunDialog.show()