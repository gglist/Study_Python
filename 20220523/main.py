import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtSerialPort import QSerialPort
from PyQt5.QtSerialPort import QSerialPortInfo
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui

import glob
import serial
import queue as Queue
import math
import re

import logging

# UI PY 형식 파일 import
from ui_main import Ui_MainWindow

logger = logging.getLogger()
logger.setLevel(level= logging.DEBUG)
logging.Formatter(
    fmt = None,
    datefmt= None,
    style= '%'
)
# handler 객체 생성
stream_handler = logging.StreamHandler()
# formatter 객체 생성
formatter = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# handler에 level 설정
stream_handler.setLevel(logging.INFO)
# handler에 format 설정
stream_handler.setFormatter(formatter)
# logger에 생성한 handler 추가
logger.addHandler(stream_handler)
# Read OS Platform
__platform__ = sys.platform

SER_TIMEOUT = 0.1  # Timeout for serial Rx
hexmode = False  # Flag to enable hex display

# Convert a string to bytes
def str_bytes(s):
    return s.encode('utf-8')


# Convert bytes to string
def bytes_str(d):
    return d if type(d) is str else "".join([chr(b) for b in d])


# Return hexadecimal values of data
def hexdump(data):
    return " ".join(["%02X" % ord(b) for b in data])


# Return a string with high-bit chars replaced by hex values
def textdump(data):
    return "".join(["[%02X]" % ord(b) if b > '\x7e' else b for b in data])


# Display incoming serial data
def display(s):
    if not hexmode:
        sys.stdout.write(textdump(str(s)))
    else:
        sys.stdout.write(hexdump(s) + ' ')

# Custom text box, catching keystrokes
class MyTextBox(QTextEdit):
    def __init__(self, *args):
        QTextEdit.__init__(self, *args)

    def keyPressEvent(self, event):  # Send keypress to parent's handler
        self.parent().keypress_handler(event)

class mainWindow(QMainWindow) :
    # Custom Signal
    text_update = QtCore.pyqtSignal(str)

    def __init__(self) :
        super().__init__()
        # UI 선언
        self.main_ui = Ui_MainWindow()
        # UI 준비
        self.main_ui.setupUi(self)
        # status bar 선언
        self.statusbar = self.main_ui.statusbar
        # Terminal 선언
        self.terminal = self.main_ui.textEdit_terminal

        # serial 선언
        self.serial = QSerialPort()
        self.serial_info = QSerialPortInfo()
        self.initSerialInfo()
        self.serialState = 0
        # UI Init 만약 설정의 양이 많으면 나중에 함수로 빼자
        self.main_ui.textEdit_terminal.setReadOnly(True)

        # Serial Port 변경시 시스템 포트 재 확인
        self.main_ui.pushButton_scanport.clicked.connect(self.UpdatSerialPort)
        self.main_ui.pushButton_connect.clicked.connect(self.openSerial)

        self.main_ui.checkBox.stateChanged.connect(self.updateCheckBox)
        self.main_ui.checkBox_2.stateChanged.connect(self.updateCheckBox)

        #self.text_update.connect(self.append_text)
        #self.main_ui.textEdit_terminal.

        sys.stdout = self #Redirect sys.stdout to self

        #self.serialThread = SerialThread()
        #self.serialThread.start()

        self.serial.readyRead.connect(self.readFromPort)

        self.main_ui.pushButton_send.clicked.connect(self.sendDataLineEdit)
        self.main_ui.pushButton_clear.clicked.connect(self.terminalClear)
        self.terminal.keyPressEvent  = self.keyPressEvent

        self.hexview = 0

    def terminalClear(self):
        self.terminal.clear()

    def keyPressEvent(self, event):
        k = event.key()
        s = "\n" if k == QtCore.Qt.Key_Return else event.text()
        logger.info(s)
        if len(s) > 0 and s[0] == "\x16":  # Detect ctrl-V paste
            cb = QApplication.clipboard()
            self.serial.write(cb.text().encode())  # Send paste string to serial driver
        else:
            self.serial.write(s.encode())  # ..or send keystrok


    def SendDataTextEdit(self):
        string = self.terminal.toPlainText()
        logger.info(string)
        self.serial.write(string.encode())

    def sendDataLineEdit(self):
        string = self.main_ui.lineEdit.text()
        logger.info(string)
        self.serial.write(string.encode())

    def updateCheckBox(self):

        if self.main_ui.checkBox.isChecked():
            self.hexview = 1
        elif not self.main_ui.checkBox.isChecked():
            self.hexview = 0

        if self.main_ui.checkBox_2.isChecked():
            logger.info("2is Checked")
        else:
            logger.info("else")
            logger.info(self.main_ui.checkBox.isChecked())

    def write(self, text):
        self.text_update.emit(text)
        logger.info(text)

    def flush(self):  # Handle sys.stdout.flush: do nothing
        pass

    #def closeEvent(self, event):  # Window closing
        #self.serth.running = False  # Wait until serial thread terminates
        #self.serth.wait()

    def readFromPort(self):

        data = self.serial.readAll()
        rowSize = 20
        if self.hexview == 0:
            if len(data) > 0:
                self.terminal.insertPlainText(QtCore.QTextStream(data).readAll())
        else:
            appendText = QtCore.QTextStream(data).readAll()

            lastData = self.terminal.toPlainText().split('\n')[-1]
            lastLength = math.ceil(len(lastData) / 3)

            appendLists = []
            splitedByTwoChar = re.split('(..)', appendText.encode().hex())[1::2]
            if lastLength > 0:
                t = splitedByTwoChar[: rowSize - lastLength] + ['\n']
                appendLists.append(' '.join(t))
                splitedByTwoChar = splitedByTwoChar[rowSize - lastLength:]

            appendLists += [' '.join(splitedByTwoChar[i * rowSize: (i + 1) * rowSize] + ['\n']) for i in
                            range(math.ceil(len(splitedByTwoChar) / rowSize))]
            if len(appendLists[-1]) < 47:
                appendLists[-1] = appendLists[-1][:-1]

            for insertText in appendLists:
                self.terminal.insertPlainText(insertText)

    def append_text(self, text):  # Text display update handler
        cur = self.main_ui.textEdit_terminal.textCursor()
        cur.movePosition(QtGui.QTextCursor.End)  # Move cursor to end of text
        s = str(text)
        logger.info(s)
        while s:
            head, sep, s = s.partition("\n")  # Split line at LF
            cur.insertText(head)  # Insert text at cursor
            if sep:  # New line if LF
                cur.insertBlock()
        self.main_ui.textEdit_terminal.setTextCursor(cur)  # Update visible cursor

    def openSerial(self):
        if self.serialState is not True:
            print(self.main_ui.comboBox_comport.currentText(), end=", ")
            print(self.main_ui.comboBox_baudrate.currentText(), end=", ")
            print(self.main_ui.comboBox_databits.currentText(), end=", ")
            print(self.main_ui.comboBox_parity.currentText(), end=", ")
            print(self.main_ui.comboBox_stopbits.currentText(), end=", ")
            print(self.main_ui.comboBox_flowcontrol.currentText())

            self.serial.setPort(QSerialPortInfo(self.main_ui.comboBox_comport.currentText()))
            self.serial.setBaudRate(self.BAUDRATES[self.main_ui.comboBox_baudrate.currentIndex()])
            self.serial.setDataBits(self.DATABITS[self.main_ui.comboBox_databits.currentIndex()])
            self.serial.setParity(self.PARITY[self.main_ui.comboBox_parity.currentIndex()])
            self.serial.setStopBits(self.STOPBITS[self.main_ui.comboBox_stopbits.currentIndex()])
            self.serial.setFlowControl(self.FLOWCONTROL[self.main_ui.comboBox_flowcontrol.currentIndex()])

            # Serial Port Open
            self.serialState = self.serial.open(QIODevice.ReadWrite)
            # 시리얼이 연결되지 않았을 때의 메시지가 필요
            self.statusbar.showMessage("Open Serial Port")
            # Status Bar를 활용해 보자

            # UI ComboBox Disable
            self.main_ui.comboBox_baudrate.setEnabled(False)
            self.main_ui.comboBox_comport.setEnabled(False)
            self.main_ui.comboBox_parity.setEnabled(False)
            self.main_ui.comboBox_flowcontrol.setEnabled(False)
            self.main_ui.comboBox_databits.setEnabled(False)
            self.main_ui.comboBox_stopbits.setEnabled(False)
            self.main_ui.pushButton_connect.setText("Disconnect")

            self.main_ui.textEdit_terminal.clear()
            self.main_ui.textEdit_terminal.setReadOnly(False)
        else:
            # Serial Port Close
            self.serialState = self.serial.close()

            # UI ComboBox Enable
            self.main_ui.comboBox_baudrate.setEnabled(True)
            self.main_ui.comboBox_comport.setEnabled(True)
            self.main_ui.comboBox_parity.setEnabled(True)
            self.main_ui.comboBox_flowcontrol.setEnabled(True)
            self.main_ui.comboBox_databits.setEnabled(True)
            self.main_ui.comboBox_stopbits.setEnabled(True)
            self.main_ui.pushButton_connect.setText("Connect")

            self.main_ui.textEdit_terminal.setReadOnly(True)
            #self.main_ui.textEdit_terminal.setEnabled(False)
            # Statusbar message 표시
            self.statusbar.showMessage("Close Serial Port")

    def initSerialInfo(self):
        # 시리얼포트 상수 값
        self.BAUDRATES = (
            QSerialPort.Baud1200,
            QSerialPort.Baud2400,
            QSerialPort.Baud4800,
            QSerialPort.Baud9600,
            QSerialPort.Baud19200,
            QSerialPort.Baud38400,
            QSerialPort.Baud57600,
            QSerialPort.Baud115200,
        )

        self.DATABITS = (
            QSerialPort.Data5,
            QSerialPort.Data6,
            QSerialPort.Data7,
            QSerialPort.Data8,
        )

        self.FLOWCONTROL = (
            QSerialPort.NoFlowControl,
            QSerialPort.HardwareControl,
            QSerialPort.SoftwareControl,
        )

        self.PARITY = (
            QSerialPort.NoParity,
            QSerialPort.EvenParity,
            QSerialPort.OddParity,
            QSerialPort.SpaceParity,
            QSerialPort.MarkParity,
        )

        self.STOPBITS = (
            QSerialPort.OneStop,
            QSerialPort.OneAndHalfStop,
            QSerialPort.TwoStop,
        )
        self.flow_name = {0: "None", 1: "Hardware", 2: "Software"}
        self.parity_name = {0: "None", 2: "Even", 3: "Odd", 4: "Space", 5: "Mark"}
        self.stopbits_name = {1: "1", 3: "1.5", 2: "2"}

        # Insert Serial Port
        self.UpdatSerialPort()
        # Insert Serial Baudrate
        self.main_ui.comboBox_baudrate.insertItems(0, [str(x) for x in self.BAUDRATES])
        # Insert Serial Databits
        self.main_ui.comboBox_databits.insertItems(0, [str(x) for x in self.DATABITS])
        # Insert Serial Parity
        self.main_ui.comboBox_parity.insertItems(0, [self.parity_name[x] for x in self.PARITY])
        # Insert Serial Stopbits
        self.main_ui.comboBox_stopbits.insertItems(0, [self.stopbits_name[x] for x in self.STOPBITS])
        # Insert Serial FlowControl
        self.main_ui.comboBox_flowcontrol.insertItems(0, [self.flow_name[x] for x in self.FLOWCONTROL])
        # Initial Set Baudrate
        self.main_ui.comboBox_baudrate.setCurrentIndex(self.BAUDRATES.index(QSerialPort.Baud115200))
        # Initial Set Databits
        self.main_ui.comboBox_databits.setCurrentIndex(self.DATABITS.index(QSerialPort.Data8))
        # Initial Set Parity
        self.main_ui.comboBox_parity.setCurrentIndex(self.PARITY.index(QSerialPort.NoParity))
        # Initial Set Stopbits
        self.main_ui.comboBox_stopbits.setCurrentIndex(self.STOPBITS.index(QSerialPort.OneStop))
        # Initial Set Flowcontrol
        self.main_ui.comboBox_flowcontrol.setCurrentIndex(self.FLOWCONTROL.index(QSerialPort.NoFlowControl))

    def UpdatSerialPort(self):
        self.main_ui.comboBox_comport.clear()
        self.main_ui.comboBox_comport.insertItems(0, self.SearchSerialPorts())

    def SearchSerialPorts(self):
        """ Lists serial port names
               :raises EnvironmentError:
               On unsupported or unknown platforms
               :returns:
               A list of the serial ports available on the system
           """
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')
        result = list()
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result

    @staticmethod
    def get_port_path():
        """
        현재플래폼에 맞게 경로 또는 지정어를 반환
        :return:
        """
        return {"linux": '/dev/ttyS', "win32": 'COM'}[__platform__]

    def _get_available_port(self):
        """
        255개의 포트를 열고 닫으면서 사용가능한 포트를 찾아서 반환
        :return:
        """
        available_port = list()
        port_path = self.get_port_path()

        for number in range(255):
            port_name = port_path + str(number)
            if not self._open(port_name):
                continue
            available_port.append(port_name)
            self.serial.close()
        return available_port

    def _open(self,
              port_name,
              baudrate=QSerialPort.Baud9600,
              data_bits=QSerialPort.Data8,
              flow_control=QSerialPort.NoFlowControl,
              parity=QSerialPort.NoParity,
              stop_bits=QSerialPort.OneStop):
        """
        인자값으로 받은 시리얼 접속 정보를 이용하여 해당 포트를 연결한다.
        :param port_name:
        :param baudrate:
        :param data_bits:
        :param flow_control:
        :param parity:
        :param stop_bits:
        :return: bool
        """
        info = QSerialPortInfo(port_name)
        self.serial.setPort(info)
        self.serial.setBaudRate(baudrate)
        self.serial.setDataBits(data_bits)
        self.serial.setFlowControl(flow_control)
        self.serial.setParity(parity)
        self.serial.setStopBits(stop_bits)
        return self.serial.open(QIODevice.ReadWrite)

# Thread to handle incoming & outgoing serial data
class SerialThread(QtCore.QThread):
    def __init__(self, portname, baudrate):  # Initialise with serial port details
        QtCore.QThread.__init__(self)
        self.portname, self.baudrate = portname, baudrate
        self.txq = Queue.Queue()
        self.running = True

    def ser_out(self, s):  # Write outgoing data to serial port if open
        self.txq.put(s)  # ..using a queue to sync with reader thread

    def ser_in(self, s):  # Write incoming serial data to screen
        display(s)

    def run(self):  # Run serial reader thread
        print("Opening %s at %u baud %s" % (self.portname, self.baudrate,
                                            "(hex display)" if hexmode else ""))
        try:
            self.ser = serial.Serial(self.portname, self.baudrate, timeout=SER_TIMEOUT)
            time.sleep(SER_TIMEOUT * 1.2)
            self.ser.flushInput()
        except:
            self.ser = None
        if not self.ser:
            print("Can't open port")
            self.running = False
        while self.running:
            s = self.ser.read(self.ser.in_waiting or 1)
            if s:  # Get data from serial port
                self.ser_in(bytes_str(s))  # ..and convert to string
            if not self.txq.empty():
                txd = str(self.txq.get())  # If Tx data in queue, write to serial port
                self.ser.write(str_bytes(txd))
        if self.ser:  # Close serial port when thread finished
            self.ser.close()
            self.ser = None


#self.show()
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = mainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
