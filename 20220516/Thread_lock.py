import threading


# 공유된 변수를 위한 클래스
class ThreadVariable():
    def __init__(self):
        self.lock = threading.Lock()
        self.lockedValue = 0

    # 한 Thread만 접근할 수 있도록 설정한다
    def plus(self, value):
        # Lock해서 다른 Thread는 기다리게 만든다.
        self.lock.acquire()
        try:
            self.lockedValue += value
        finally:
            # Lock을 해제해서 다른 Thread도 사용할 수 있도록 만든다.
            self.lock.release()


# CounterThread
class CounterThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, name='Timer Thread')

    # CounterThread가 실행하는 함수
    def run(self):
        global totalCount

        # 2,500,000번 카운트 시작
        for _ in range(2500000):
            totalCount.plus(1)
        print('2,500,000번 카운팅 끝!')


if __name__ == '__main__':
    # 전역 변수로 totalCount를 선언
    global totalCount
    # totalCount를 ThreadVariable 오브젝트로 초기화한다
    totalCount = ThreadVariable()

    # totalCount를 1씩 더하는
    # Counter Thread를 4개 만들어서 동작시킨다.
    for _ in range(4):
        timerThread = CounterThread()
        timerThread.start()

    print('모든 Thread들이 종료될 때까지 기다린다.')
    mainThread = threading.current_thread()
    for thread in threading.enumerate():
        # Main Thread를 제외한 모든 Thread들이
        # 카운팅을 완료하고 끝날 때 까지 기다린다.
        if thread is not mainThread:
            thread.join()

    print('totalCount = ' + str(totalCount.lockedValue))