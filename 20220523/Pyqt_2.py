import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic   # ui 파일을 사용하기 위한 모듈 import

import pyqt_ui
import pyqt_ui1
import pyqt_ui2
import pyqt_ui3

#UI파일 연결 코드
UI_class = uic.loadUiType("pyqt_ui.ui")[0]

class MyWindow(QMainWindow, pyqt_ui3.Ui_MainWindow) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.show()

        #self.pushButton.clicked.connect(self.button1Function)
        #self.pushButton_2.clicked.connect(self.button2Function)

        self.radioButton.clicked.connect(self.groupboxRadFunction)
        self.radioButton_2.clicked.connect(self.groupboxRadFunction)
        self.radioButton_3.clicked.connect(self.groupboxRadFunction)
        self.radioButton_4.clicked.connect(self.groupboxRadFunction)

        self.checkBox_1.stateChanged.connect(self.groupchkFunction)
        self.checkBox_2.stateChanged.connect(self.groupchkFunction)
        self.checkBox_3.stateChanged.connect(self.groupchkFunction)
        self.checkBox_4.stateChanged.connect(self.groupchkFunction)

    def groupchkFunction(self):
        if self.checkBox_1.isChecked(): print("chk_1 isChecked")
        if self.checkBox_2.isChecked(): print("chk_2 isChecked")
        if self.checkBox_3.isChecked(): print("chk_3 isChecked")
        if self.checkBox_4.isChecked(): print("chk_4 isChecked")

    def groupboxRadFunction(self):
        if self.radioButton.isChecked():
            print("GroupBox_rad1 Chekced")
        elif self.radioButton_2.isChecked():
            print("GroupBox_rad2 Checked")
        elif self.radioButton_3.isChecked():
            print("GroupBox_rad3 Checked")
        elif self.radioButton_4.isChecked():
            print("GroupBox_rad4 Checked")

    def button1Function(self):
        print("btn 1 clicked")

    def button2Function(self):
        print("btn 2 clicked")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = MyWindow()
    #MainWindow.show()
    sys.exit(app.exec_())
