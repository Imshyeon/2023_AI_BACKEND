class MyCalc:
    def __init__(self,a=400,b=200) -> None:
        super().__init__()
        self.__a=a
        self.__b=b

    def getA(self):
        return self.__a
    def getB(self):
        return self.__b
    def setA(self,a):
        self.__a=a
    def setB(self,b):
        self.__b=b

    def getHap(self):
        result = self.__a+self.__b
        return result
    def getSub(self):
        result = self.__a - self.__b
        return result
    def getMul(self):
        result = self.__a * self.__b
        return result
    def getDiv(self):
        result = self.__a / self.__b
        return result

    def __repr__(self):
        return f'{self.__a}+{self.__b} = {self.getHap()}\n'\
               f'{self.__a}-{self.__b} = {self.getSub()}\n' \
               f'{self.__a}*{self.__b} = {self.getMul()}\n' \
               f'{self.__a}/{self.__b} = {self.getDiv()}'