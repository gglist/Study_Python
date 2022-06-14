import sys
import glob
import numpy as np
from collections import deque
import serial
import serial.tools.list_ports as sp

#import threading
#import matplotlib.pyplot as plt
#import matplotlib.animation as animation

list = sp.comports()
connected = []

## PC 연결된 COM Port 정보를 list에 넣어 환인한다.

for idx in list:
    connected.append(idx.device)
print("Connected COM Ports: " + str(connected))

def serial_ports():
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
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

if __name__ == "__main__":
    ports = []
    ports = serial_ports()
    print(ports)