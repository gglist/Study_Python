import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

import pyqt_ui
# UI 파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야 한다.
UI_FILE_PATH = './pyqt_ui.ui'
UI_PY_FILE_PATH = './pyqt_ui.py'

#form_class = uic.loadUiType('pyqt_ui1.ui')[0]

class WindowClass(QMainWindow, pyqt_ui.Ui_MainWindow):
    def __init_(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = WindowClass()
    window.show()
    sys.exit(app.exec_())