class Withtest:
    #초기화 메서드 정의
    def __init__(self):
        self.temp = "초기화 메서드"

    #객체가 호출될 때 자동으로 실행
    def __enter__(self):
        print(self.temp)
        return self
        # 반환값이 있어야 VARIABLE를 블록내에서 사용할 수 있다

    def printText(self):
        print("메소드 호출 테스트")

    #with 구문 통해 객체가 종료될 때 자동으로 실행
    def __exit__(self, exc_type, exc_val, exc_tb):
        #종료 구문 설정하기(세션의 종료 등)
        print('with 통해 종료')

#객체 생성 및 with 구문 실행
if __name__ == "__main__":
    withclass = Withtest()
    with withclass as wc:
        wc.printText()

