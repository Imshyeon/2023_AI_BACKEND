# from time import time,sleep
from abc import abstractmethod, ABCMeta

class IChange(metaclass=ABCMeta):
    @abstractmethod
    def charge(self,time):
        pass

class Mobile(metaclass=ABCMeta):
    def __init__(self,mobileName="",batterySize=0,osType=""):
        self.__mobileName = mobileName
        self.__batterySize = batterySize
        self.__osType = osType

    def Name(self):
        return self.__mobileName
    def Name(self,mobileName):
        self.__mobileName = mobileName

    def Bat(self):
        return self.__batterySize
    def Bat(self,batteryName):
        self.__batterySize = batteryName

    def OS(self):
        return self.__osType
    def OS(self,osType):
        self.__osType = osType

    @abstractmethod
    def operate(self,time):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class Ltab(Mobile,IChange):

    def __init__(self, mobileName="", batterySize=0, osType=""):
        super().__init__(mobileName, batterySize, osType)

    # def Ltab(self, mobileName, batterySize, osType):
    #     self.mobileName = mobileName
    #     self.batterySize = batterySize
    #     self.osType = osType

    def operate(self,time):
        for i in range(1,time+1):
            self.__batterySize -=10
        return self.__batterySize

    def charge(self,time):
        for i in range(1,time+1):
            self.__batterySize += 10
        return self.__batterySize

    def __repr__(self):
        return f'Mobile      Battery     OS\n'\
            f'-------------------------------\n'\
            f'{self.__Name("Ltab")}\t\t{self.__Bat(500)}\t\t{self.__OS("AP-10")}\n'

class Otab(Mobile,IChange):
    def __init__(self, mobileName="", batterySize=0, osType=""):
        super().__init__(mobileName, batterySize, osType)

    # def Otab(self, mobileName, batterySize, osType):
    #     self.mobileName = mobileName
    #     self.batterySize = batterySize
    #     self.osType = osType

    def operate(self,time):
        for i in range(1, time + 1):
            self.__batterySize -= 12
        return self.__batterySize

    def charge(self,time):
        for i in range(1, time + 1):
            self.__batterySize += 8
        return self.__batterySize

    def __repr__(self):
        return f'{self.__Name("Otab")}\t\t{self.__Bat(1000)}\t\t{self.__OS("AND-20")}\n'\
            f'---------------------------------'


if __name__ == '__main__':

    m1=Ltab("Ltab", 500, "AP-10")
    m2=Otab("Otab", 1000, "AND-20")
    print(m1,m2)
    print()
    print('10분 충전')
    m1.charge(10)
    m2.charge(10)
    print(m1,m2)
    print()
    print('5분 통화')
    m1.operate(5)
    m2.operate(5)
    print(m1,m2)
    # m2.mobile = ("Otab", 1000, "AND-20")

