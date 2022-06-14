import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class QtGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Appia Qt GUI")
        self.resize(300, 300)
        self.listv = []
        button = QPushButton('Button', self)
        button.move(10, 10)
        button.clicked.connect(lambda: self.disable_but(button))
        self.listv.append(button)
        button1 = QPushButton('Button1', self)
        button1.move(10, 40)
        button1.clicked.connect(lambda: self.disable_but(button1))
        self.listv.append(button1)
        button2 = QPushButton('Button2', self)
        button2.move(10, 70)
        button2.released.connect(lambda: self.disable_but(button2))
        self.listv.append(button2)
        button3 = QPushButton('Refresh', self)
        button3.move(100, 10)
        button3.clicked.connect(self.refrsh_all)
        self.setWindowTitle("Appia Qt GUI")
        self.show()

    def disable_but(self, vbutton):
        vbutton.setEnabled(False)

    def refrsh_all(self):
        for i in self.listv:
            i.setEnabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QtGUI()
    app.exec_()
