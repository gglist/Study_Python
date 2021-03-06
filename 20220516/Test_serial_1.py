from sys import stdin, stdout
from threading import Thread
from serial import Serial

class Terminal:

    def __init__(self, port, baud):
        self.sp = Serial(port, baud)
        self.reader_thread = Thread(None, target=self.read, name="Reader")
        self.writer_thread = Thread(None, target=self.write, name="Writer")
        self.alive = False

    def start(self):
        self.reader_thread.start()
        self.reader_thread.join()

    def read(self):
        self.alive = True
        self.writer_thread.start()
        ch = stdin.read(1)
        while ch != '#':
            self.sp.write(ch.encode('ascii'))
            ch = stdin.read(1)
        self.alive = False
        self.sp.write(b' ')
        self.writer_thread.join()

    def write(self):
        while self.alive:
            ch = self.sp.read()
            ##stdout.write(ch)
            #print(ch.decode("ascii"))
            if ch == '\r':
                print(ch.decode('ascii'), end='\n')
            else:
                print(ch.decode('ascii'), end='')


if __name__ == "__main__":
    term = Terminal("COM8", 115200)

    term.start()