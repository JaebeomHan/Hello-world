import sys
sys.dont_write_bytecode = True
from PyQt5.QtWidgets import (QWidget, QPushButton, QAction, QVBoxLayout, QHBoxLayout, QComboBox, QGridLayout, QMessageBox,
                            QDesktopWidget, QLabel, QLineEdit, QInputDialog, QFileDialog, QDialog, QTextEdit)
from PyQt5.QtCore import QCoreApplication, Qt
from calculate_reactant1_energy import calculate_reactant1_energy

class MainWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.setMainWidget()

    def setMainWidget(self):

        ## 빈 리스트 생성
        self.resultList = []

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

        ## 프로그램 설명 버튼
        self.programExplanation = QPushButton('프로그램 설명', self)
        self.programExplanation.move(860, 400)
        self.programExplanation.resize(110, 40)
        self.programExplanation.clicked.connect(self.helpMeFunction)

        ## 만든이 버튼
        self.madeByBtn = QPushButton('만든이', self)
        self.madeByBtn.move(860, 450)
        self.madeByBtn.resize(110, 40)
        self.madeByBtn.clicked.connect(self.madeByInfo)

        ## 사용자 정보 콤보박스 1
        self.userProfileCBox = QComboBox(self)
        self.userProfileCBox.addItem('선택')
        self.userProfileCBox.addItem('학부')
        self.userProfileCBox.addItem('석사')
        self.userProfileCBox.addItem('박사&교수')
        self.userProfileCBox.addItem('연구원')
        self.userProfileCBox.addItem('기타')
        self.userProfileCBox.move(370, 250)
        self.userProfileCBox.resize(120, 30)

        ## 사용자 정보 콤보박스 2
        self.userDepartmentCBox = QComboBox(self)
        self.userDepartmentCBox.addItem('선택')
        self.userDepartmentCBox.addItem('화학과')
        self.userDepartmentCBox.addItem('물리학과')
        self.userDepartmentCBox.addItem('공학계열')
        self.userDepartmentCBox.addItem('기타')
        self.userDepartmentCBox.move(370, 290)
        self.userDepartmentCBox.resize(120, 30)

        ## 학과 입력 칸
        self.userProfileLabel = QLabel("직업", self)
        self.userProfileLabel.move(320, 250)
        self.userProfileLabel.resize(50, 30)

        self.departmentLabel = QLabel("학과", self)
        self.departmentLabel.move(320, 290)
        self.departmentLabel.resize(50, 30)


        ## 기능 시작 버튼
        self.startProgram = QPushButton('시작하기', self)
        self.startProgram.move(530, 249)
        self.startProgram.resize(150, 72)
        self.startProgram.clicked.connect(self.programRunFunction)

        ## dialog 설정
        self.programRunDialog = QDialog()
        self.madeByDialog = QDialog()
        self.helpMeDialog = QDialog()
        self.plzInputProfileDialog = QDialog()

    ## 만든이 정보 함수
    def madeByInfo(self):
        LEADER = QLabel('Leader : 최지우', self.madeByDialog)
        GUI = QLabel('GUI : 한재범', self.madeByDialog)
        DATABASE = QLabel('Database : 이경훈', self.madeByDialog)
        btnMadeBy = QPushButton("Close", self.madeByDialog)
        btnMadeBy.clicked.connect(self.closeDialogFunction)

        self.madeByDialog.setWindowTitle('만든이')
        self.madeByDialog.setWindowModality(Qt.ApplicationModal)

        LEADER.move(30, 30)
        GUI.move(30, 60)
        DATABASE.move(30, 90)
        btnMadeBy.resize(100, 30)
        btnMadeBy.move(50, 130)

        self.madeByDialog.setFixedSize(200, 180)
        self.madeByDialog.show()

    ## 도움말 Dialog
    def helpMeFunction(self):
        labelHelpMe = QLabel(
            '''        1. 사용자 정보 입력
        2. 계산 파일 입력
        3. 활성화 에너지 계산
        4. 다양한 단위로 변환.''', self.helpMeDialog)
        btnHelpMe = QPushButton("Close", self.helpMeDialog)
        btnHelpMe.clicked.connect(self.closeDialogFunction)

        labelHelpMe.resize(400, 200)
        labelHelpMe.move(20, -20)
        btnHelpMe.resize(100, 30)
        btnHelpMe.move(100, 150)

        self.helpMeDialog.setWindowTitle("프로그램 설명")
        self.helpMeDialog.setWindowModality(Qt.ApplicationModal)

        self.helpMeDialog.setFixedSize(300,200)
        self.helpMeDialog.show()

    ## Dialog 닫기 이벤트
    def closeDialogFunction(self):
        self.madeByDialog.close()
        self.helpMeDialog.close()
        self.plzInputProfileDialog.close()

    ## 정보 입력 안했을 때 경고문
    def plzInputProfileFunction(self):
        self.plzInputProfileDialog.plzInputProfileLabel = QLabel("사용자 정보를 입력해주세요", self.plzInputProfileDialog)
        self.plzInputProfileDialog.closeProfileDialog = QPushButton("Close", self.plzInputProfileDialog)
        self.plzInputProfileDialog.closeProfileDialog.clicked.connect(self.closeDialogFunction)

        self.plzInputProfileDialog.plzInputProfileLabel.move(50, 35)
        self.plzInputProfileDialog.closeProfileDialog.move(100, 80)
        self.plzInputProfileDialog.setWindowModality(Qt.ApplicationModal)
        self.plzInputProfileDialog.setWindowTitle("경고")
        self.plzInputProfileDialog.setFixedSize(300, 120)
        self.plzInputProfileDialog.show()

    ## 다음 아래 세 함수들은 programRunDialog 함수와 연결되어 있다는걸 참고바람

    def reactant_1_Function(self):

        fname = QFileDialog.getOpenFileName(self, "Open File : ", "", "text File(*.txt)")
        if fname[0]:
            f = open(fname[0], 'r', encoding="UTF8")
            with f:
                global data_1
                data_1 = calculate_reactant1_energy(f)
                self.programRunDialog.textEdit1.setText(str(data_1))
        else:
            QMessageBox.about(self, 'Warning', '파일을 선택하지 않았습니다.')

    def reactant_2_Function(self):

        fname = QFileDialog.getOpenFileName(self, "Open File : ", "", "text File(*.txt)")
        if fname[0]:
            f = open(fname[0], 'r', encoding="UTF8")
            with f:
                global data_2
                data_2 = calculate_reactant1_energy(f)
                self.programRunDialog.textEdit2.setText(str(data_2))
        else:
            QMessageBox.about(self, 'Warning', '파일을 선택하지 않았습니다.')

    def reactant_TS_Function(self):

        fname = QFileDialog.getOpenFileName(self, "Open File : ", "", "text File(*.txt)")
        if fname[0]:
            f = open(fname[0], 'r', encoding="UTF8")
            with f:
                global data_TS
                data_TS = calculate_reactant1_energy(f)
                self.programRunDialog.textEdit3.setText(str(data_TS))
                if float(data_TS)<0 :
                    self.programRunDialog.textEdit4.setText("올바른 전이 구조를 구하셨습니다.")
                else :
                    self.programRunDialog.textEdit4.setText("전이 구조가 잘못되었습니다.")
        else:
            QMessageBox.about(self, 'Warning', '파일을 선택하지 않았습니다.')

    def saveList(self):

        self.resultList.append("id")
        self.resultList.append(str(self.userProfileCBox.currentText()))
        self.resultList.append(str(self.userDepartmentCBox.currentText()))
        self.resultList.append(str(data_1))
        self.resultList.append(str(data_2))
        self.resultList.append(str(data_TS))
        self.resultList.append("created")

        with open("megaton_result.txt", 'w') as f:
            f.write("<< This is the result of your experiment >>")
            f.write("\nReactant1 : " + str(data_1))
            f.write("\nReactant2 : " + str(data_2))
            f.write("\nTransition State : " + str(data_TS))

            for num in range(0, 7):
                f.write("\n" + str(self.resultList[num]))


    ## 메인 기능 실행 Dialog
    def programRunFunction(self):

        if (self.userProfileCBox.currentText() != "선택"):
        
            self.programRunDialog.setFixedSize(500, 500)

            self.programRunDialog.reactant1 = QPushButton("반응물1", self.programRunDialog)
            self.programRunDialog.reactant2 = QPushButton("반응물2", self.programRunDialog)
            self.programRunDialog.reactant3 = QPushButton("전이구조", self.programRunDialog)
            self.programRunDialog.textEdit1 = QTextEdit(self.programRunDialog)
            self.programRunDialog.textEdit2 = QTextEdit(self.programRunDialog)
            self.programRunDialog.textEdit3 = QTextEdit(self.programRunDialog)
            self.programRunDialog.textEdit4 = QTextEdit(self.programRunDialog)

            self.programRunDialog.reactant1.resize(140, 30)
            self.programRunDialog.reactant2.resize(140, 30)
            self.programRunDialog.reactant3.resize(140, 30)
            self.programRunDialog.textEdit1.resize(140, 50)
            self.programRunDialog.textEdit2.resize(140, 50)
            self.programRunDialog.textEdit3.resize(140, 50)
            self.programRunDialog.textEdit4.resize(440, 50)

            self.programRunDialog.reactant1.move(50, 30)
            self.programRunDialog.reactant2.move(200, 30)
            self.programRunDialog.reactant3.move(350, 30)
            self.programRunDialog.textEdit1.move(50, 100)
            self.programRunDialog.textEdit2.move(200, 100)
            self.programRunDialog.textEdit3.move(350, 100)
            self.programRunDialog.textEdit4.move(50, 200)

            self.programRunDialog.textEdit4.setFontPointSize(10)

            self.programRunDialog.reactant1.clicked.connect(self.reactant_1_Function)
            self.programRunDialog.reactant2.clicked.connect(self.reactant_2_Function)
            self.programRunDialog.reactant3.clicked.connect(self.reactant_TS_Function)

            self.programRunDialog.saveListBtn = QPushButton("저장", self.programRunDialog)
            self.programRunDialog.saveListBtn.move(200, 300)
            self.programRunDialog.saveListBtn.resize(150, 50)
            self.programRunDialog.saveListBtn.clicked.connect(self.saveList)

            self.programRunDialog.setWindowTitle("활성화 에너지 구하기")
            self.programRunDialog.setWindowModality(Qt.ApplicationModal)
            self.programRunDialog.setFixedSize(540, 400)

            self.programRunDialog.show()

        else:
            self.startProgram.clicked.connect(self.plzInputProfileFunction)


