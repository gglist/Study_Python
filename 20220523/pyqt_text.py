from PyQt5.QtWidgets import *
from PyQt5 import uic   # ui 파일을 사용하기 위한 모듈 import

import pyqt_ui3

form_class = uic.loadUiType("lineeditTest.ui")[0]

class MyWindow(QMainWindow, pyqt_ui3.Ui_Dialog):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.lineEdit_2.textChanged.connect(self.lineeditTextFunction)
        self.lineEdit_2.returnPressed.connect(self.printTextFunction)
        self.pushButton.clicked.connect(self.changeTextFunction)

    def lineeditTextFunction(self):
        self.label.setText(self.lineEdit_2.text())

    def printTextFunction(self):
        # self.lineedit이름.text()
        # Lineedit에 있는 글자를 가져오는 메서드
        print(self.lineEdit_2.text())

    def changeTextFunction(self):
        # self.lineedit이름.setText("String")
        # Lineedit의 글자를 바꾸는 메서드
        self.lineEdit_2.setText("Change Text")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = MyWindow()
    MainWindow.show()
    sys.exit(app.exec_())
