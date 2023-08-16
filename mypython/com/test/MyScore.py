class Score:
    '''
    이름 국어 영어 -> private
    총점 평균 출력 메소드 ->public
    '''

    def __init__(self,name,kor,eng):
        self.__name = name
        self.__kor = kor
        self.__eng = eng

    def setKor(self,kor):
        self.__kor = kor
    def getKor(self):
        return self.__kor

    def setEng(self,eng):
        self.__eng = eng
    def getEng(self):
        return self.__eng

    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name

    def getTot(self):
        return self.__kor + self.__eng
    def getAvg(self):
        return self.getTot() / 2

    def __repr__(self):
        return f"{self.__name} {self.__kor} {self.__eng} {self.getTot()} {self.getAvg()}"


class MyScore(Score):
    '''
    Score를 상속받아 3과목을 총평균
    '''

    def __init__(self,name,kor,eng,mat) -> None:
        super().__init__(name,kor,eng)
        self.__mat = mat

    def setMat(self,mat):
        self.__mat = mat
    def getMat(self):
        return self.__mat

    def getTot(self):
        return super().getTot() + self.__mat
    def getAvg(self):
        return self.getTot()/3

    def __repr__(self):
        return f"이름 : {super().getName()}, 국어 : {super().getKor()}, 영어 : {super().getEng()}" \
               f", 수학 : {self.getMat()}"\
               f", 총점 : {self.getTot()}, 평균 : {self.getAvg():5.1f}"

if __name__ == '__main__':
    print(MyScore('홍길동',100,100,100))