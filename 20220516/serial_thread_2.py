import serial
import time  # Optional (required if using time.sleep() below)

ser = serial.Serial(port='COM8', baudrate=115200)

while (True):
    # Check if incoming bytes are waiting to be read from the serial input
    # buffer.
    # NB: for PySerial v3.0 or later, use property `in_waiting` instead of
    # function `inWaiting()` below!
    if (ser.inWaiting() > 0):
        # read the bytes and convert from binary array to ASCII
        data_str = ser.read(ser.inWaiting()).decode('ascii')
        # print the incoming string without putting a new-line
        # ('\n') automatically after every print()
        if data_str == '\r':
            print(data_str, end='\n')
        else:
            print(data_str, end='')

        # Put the rest of your code you want here

    # Optional, but recommended: sleep 10 ms (0.01 sec) once per loop to let
    # other threads on your PC run during this time.
    time.sleep(0.01)