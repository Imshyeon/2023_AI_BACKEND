from abc import ABCMeta, abstractmethod

class Mobile:
    def __init__(self,mobileName="",batterySize=0,osType=""):
        self.__mobileName = mobileName
        self.__batterySize = batterySize
        self.__osType = osType

    @abstractmethod
    def operate(self,time):
        pass

    def setM(self,mobileName):
        self.__mobileName=mobileName
    def getM(self):
        return self.__mobileName
    def setB(self,batterySize):
        self.__batterySize=batterySize
    def getB(self):
        return self.__batterySize
    def setOs(self,osType):
        self.__osType=osType
    def getOs(self):
        return self.__osType

class IChange:
    @abstractmethod
    def charge(self,time):
        pass

class Ltab(Mobile,IChange):
    def __init__(self, mobileName="", batterySize=0, osType=""):
        Mobile.__init__(self, mobileName, batterySize, osType)
    def operate(self,time):
        realTime= time
        my_bat = Mobile.getB(self)
        for i in range(1,realTime+1):
            my_bat -= 10
        return Mobile.setB(self,my_bat)
    def charge(self,time):
        realTime= time
        my_bat=Mobile.getB(self)
        for i in range(1,realTime+1):
            my_bat+=10
        return Mobile.setB(self,my_bat)

class Otab(Mobile,IChange):
    def __init__(self, mobileName="", batterySize=0, osType=""):
        Mobile.__init__(self, mobileName, batterySize, osType)
    def operate(self, time):
        realTime = time
        my_bat = Mobile.getB(self)
        for i in range(1, realTime + 1):
            my_bat -= 12
        return Mobile.setB(self,my_bat)
    def charge(self, time):
        realTime = time
        my_bat = Mobile.getB(self)
        for i in range(1, realTime + 1):
            my_bat += 8
        return Mobile.setB(self,my_bat)

if __name__ == '__main__':
    m1=Ltab("Ltab",500,"AP-01")
    m2=Otab("Otab",1000,"AND-20")
    print(f'Mobile\t\tBattery\t\tOS')
    print(f'---------------------------------------')
    print(f'{m1.getM()}\t\t{m1.getB()}\t\t\t{m1.getOs()}')
    print(f'{m2.getM()}\t\t{m2.getB()}\t\t{m2.getOs()}')
    print(f'---------------------------------------')
    print()

    m1.charge(10)
    m2.charge(10)
    print('10분 충전')
    print(f'Mobile\t\tBattery\t\tOS')
    print(f'---------------------------------------')
    print(f'{m1.getM()}\t\t{m1.getB()}\t\t\t{m1.getOs()}')
    print(f'{m2.getM()}\t\t{m2.getB()}\t\t{m2.getOs()}')
    print(f'---------------------------------------')
    print()

    m1.operate(5)
    m2.operate(5)
    print('5분 통화')
    print(f'Mobile\t\tBattery\t\tOS')
    print(f'---------------------------------------')
    print(f'{m1.getM()}\t\t{m1.getB()}\t\t\t{m1.getOs()}')
    print(f'{m2.getM()}\t\t{m2.getB()}\t\t{m2.getOs()}')
    print(f'---------------------------------------')
