# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\GGLIST\Job\Software\Study\Python\20220523\ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(956, 631)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_serial = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_serial.setGeometry(QtCore.QRect(10, 10, 231, 291))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(12)
        self.groupBox_serial.setFont(font)
        self.groupBox_serial.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_serial.setFlat(False)
        self.groupBox_serial.setCheckable(False)
        self.groupBox_serial.setObjectName("groupBox_serial")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox_serial)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 19, 213, 181))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(12)
        self.gridLayoutWidget.setFont(font)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_comport = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(12)
        self.comboBox_comport.setFont(font)
        self.comboBox_comport.setObjectName("comboBox_comport")
        self.gridLayout.addWidget(self.comboBox_comport, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.comboBox_databits = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(12)
        self.comboBox_databits.setFont(font)
        self.comboBox_databits.setObjectName("comboBox_databits")
        self.gridLayout.addWidget(self.comboBox_databits, 2, 1, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(11)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
        self.comboBox_parity = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(12)
        self.comboBox_parity.setFont(font)
        self.comboBox_parity.setObjectName("comboBox_parity")
        self.gridLayout.addWidget(self.comboBox_parity, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.comboBox_baudrate = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(12)
        self.comboBox_baudrate.setFont(font)
        self.comboBox_baudrate.setObjectName("comboBox_baudrate")
        self.gridLayout.addWidget(self.comboBox_baudrate, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.comboBox_stopbits = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(12)
        self.comboBox_stopbits.setFont(font)
        self.comboBox_stopbits.setObjectName("comboBox_stopbits")
        self.gridLayout.addWidget(self.comboBox_stopbits, 4, 1, 1, 1)
        self.comboBox_flowcontrol = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(12)
        self.comboBox_flowcontrol.setFont(font)
        self.comboBox_flowcontrol.setObjectName("comboBox_flowcontrol")
        self.gridLayout.addWidget(self.comboBox_flowcontrol, 5, 1, 1, 1)
        self.pushButton_connect = QtWidgets.QPushButton(self.groupBox_serial)
        self.pushButton_connect.setGeometry(QtCore.QRect(119, 210, 101, 28))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(12)
        self.pushButton_connect.setFont(font)
        self.pushButton_connect.setObjectName("pushButton_connect")
        self.pushButton_clear = QtWidgets.QPushButton(self.groupBox_serial)
        self.pushButton_clear.setGeometry(QtCore.QRect(10, 250, 210, 28))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(12)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_scanport = QtWidgets.QPushButton(self.groupBox_serial)
        self.pushButton_scanport.setGeometry(QtCore.QRect(10, 210, 101, 28))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(12)
        self.pushButton_scanport.setFont(font)
        self.pushButton_scanport.setObjectName("pushButton_scanport")
        self.groupBox_terminal = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_terminal.setGeometry(QtCore.QRect(250, 150, 691, 431))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(12)
        self.groupBox_terminal.setFont(font)
        self.groupBox_terminal.setObjectName("groupBox_terminal")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_terminal)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 671, 401))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(12)
        self.gridLayoutWidget_2.setFont(font)
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textEdit_terminal = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(11)
        self.textEdit_terminal.setFont(font)
        self.textEdit_terminal.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.textEdit_terminal.setObjectName("textEdit_terminal")
        self.gridLayout_2.addWidget(self.textEdit_terminal, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(260, 10, 231, 131))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.checkBox_timeview = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_timeview.setGeometry(QtCore.QRect(20, 20, 111, 19))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(12)
        self.checkBox_timeview.setFont(font)
        self.checkBox_timeview.setObjectName("checkBox_timeview")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_5.setGeometry(QtCore.QRect(20, 40, 96, 19))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(12)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(510, 10, 231, 131))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(10, 20, 96, 19))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 40, 96, 19))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(12)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 60, 96, 19))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(12)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 80, 96, 19))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(12)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 330, 231, 31))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(12)
        font.setUnderline(False)
        font.setKerning(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit.setMouseTracking(True)
        self.lineEdit.setAcceptDrops(True)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_send = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_send.setGeometry(QtCore.QRect(20, 370, 210, 28))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(12)
        self.pushButton_send.setFont(font)
        self.pushButton_send.setObjectName("pushButton_send")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 310, 221, 16))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 956, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_serial.setTitle(_translate("MainWindow", "Serial Option"))
        self.label_6.setText(_translate("MainWindow", "Flow Control"))
        self.label_1.setText(_translate("MainWindow", "COM Port"))
        self.label_5.setText(_translate("MainWindow", "Stop Bits"))
        self.label_3.setText(_translate("MainWindow", "Data Bits"))
        self.label_4.setText(_translate("MainWindow", "Parity"))
        self.label_2.setText(_translate("MainWindow", "Baud Rate"))
        self.pushButton_connect.setText(_translate("MainWindow", "Connect"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear"))
        self.pushButton_scanport.setText(_translate("MainWindow", "Scan Port"))
        self.groupBox_terminal.setTitle(_translate("MainWindow", "Terminal"))
        self.groupBox.setTitle(_translate("MainWindow", "Terminal option"))
        self.checkBox_timeview.setText(_translate("MainWindow", "Time View"))
        self.checkBox_5.setText(_translate("MainWindow", "CR/LF"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Char Option"))
        self.checkBox.setText(_translate("MainWindow", "Show HEX"))
        self.checkBox_2.setText(_translate("MainWindow", "Send HEX"))
        self.checkBox_3.setText(_translate("MainWindow", "Send CR"))
        self.checkBox_4.setText(_translate("MainWindow", "Send LF"))
        self.pushButton_send.setText(_translate("MainWindow", "Send"))
        self.label.setText(_translate("MainWindow", "Send Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
