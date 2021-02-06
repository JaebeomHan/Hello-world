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

        # 기능 시작 버튼 - 파일을 읽기만 함!
        self.startProgram = QPushButton('시작하기', self)
        self.startProgram.move(520, 250)
        self.startProgram.resize(100, 30)
        self.startProgram.clicked.connect(self.dialogOpen)

        # QDialog 설정
        self.dialog = QDialog()

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
        userPrifile.addItem('직업을 선택해주세요')
        userPrifile.addItem('대학원생')
        userPrifile.addItem('교수님')
        userPrifile.addItem('연구원')
        userPrifile.move(330, 250)
        userPrifile.resize(170, 30)

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

    # 버튼 이벤트 함수
    def dialogOpen(self):
        
        # 버튼 추가
        btnDialog = QPushButton("OK", self.dialog)
        btnDialog.move(570, 750)
        btnDialog.clicked.connect(self.dialogClose)
        self.dialog.textEdit = QTextEdit(self.dialog)
        self.dialog.textEdit.move(50, 20)
        self.dialog.textEdit.resize(1100, 700)

        # QDialog 세팅
        self.dialog.setWindowTitle('Dialog')
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.resize(1200, 800)

        fname = QFileDialog.getOpenFileName(self, 'Open File', '',
                                            'text File(*.txt)')
        if fname[0]:
            # 텍스트 파일 내용 읽기
            f = open(fname[0], 'r', encoding='UTF8') # Path 정보로 파일을 읽는다.
            with f:
                data = f.read()
                self.dialog.textEdit.setText(data)
        else:
            QMessageBox.about(self, 'Warning', '파일을 선택하지 않았습니다.')


        self.dialog.show()

    # Dialog 닫기 이벤트
    def dialogClose(self):
        self.dialog.close()