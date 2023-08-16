from abc import ABC, abstractmethod
#IChange
class IChange(ABC):
    @abstractmethod
    def charge(self, time):
        pass

#--------------------Mobile

class Mobile(ABC):
    def __init__(self, mobileName="", batterySize=0, osType=""):
        self.__mobileName = mobileName
        self.__batterySize = batterySize
        self.__osType = osType

    def getMobileName(self):
        return self.__mobileName

    def setMobileName(self, mobileName):
        self.__mobileName = mobileName

    def getBatterySize(self):
        return self.__batterySize

    def setBatterySize(self, batterySize):
        self.__batterySize = batterySize

    def getOsType(self):
        return self.__osType

    def setOsType(self, osType):
        self.__osType = osType

    @abstractmethod
    def operate(self, time):
        pass

#------------------LTAB----------------------------------------------------
class LTab(Mobile, IChange):
    def __init__(self, mobileName, batterySize, osType):
        super().__init__(mobileName, batterySize, osType)

    def charge(self, time):
        chargedAmount = time * 10
        self.setBatterySize(self.getBatterySize() + chargedAmount)
        return self.getBatterySize()

    def operate(self, time):
        usedAmount = time * 10
        self.setBatterySize(self.getBatterySize() - usedAmount)
        return self.getBatterySize()
#------------------OTAB----------------------------------------------------
class OTab(Mobile, IChange):
    def __init__(self, mobileName, batterySize, osType):
        super().__init__(mobileName, batterySize, osType)

    def charge(self, time):
        chargedAmount = time * 8
        self.setBatterySize(self.getBatterySize() + chargedAmount)
        return self.getBatterySize()

    def operate(self, time):
        usedAmount = time * 12
        self.setBatterySize(self.getBatterySize() - usedAmount)
        return self.getBatterySize()

#------------ㅡmain

if __name__ == "__main__":
    lt = LTab("LTab", 500, "AP-01")
    ot = OTab("OTab", 1000, "AND-20")

    print("  Mobile\t\tBattery\t\tOS")
    print("---------------------------------------------")
    print(f"{lt.getMobileName()}\t\t{lt.getBatterySize()}\t\t{lt.getOsType()}")
    print(f"{ot.getMobileName()}\t\t{ot.getBatterySize()}\t\t{ot.getOsType()}")
    print("---------------------------------------------")
    print()

    print("10 충전      ")
    lt.charge(10)
    ot.charge(10)
    print("  Mobile\t\tBattery\t\tOS")
    print("---------------------------------------------")
    print(f"{lt.getMobileName()}\t\t{lt.getBatterySize()}\t\t{lt.getOsType()}")
    print(f"{ot.getMobileName()}\t\t{ot.getBatterySize()}\t\t{ot.getOsType()}")
    print("---------------------------------------------")
    print()

    print("5분 통화 ")
    lt.operate(5)
    ot.operate(5)
    print("  Mobile\t\tBattery\t\tOS")
    print("---------------------------------------------")
    print(f"{lt.getMobileName()}\t\t{lt.getBatterySize()}\t\t{lt.getOsType()}")
    print(f"{ot.getMobileName()}\t\t{ot.getBatterySize()}\t\t{ot.getOsType()}")
    print("---------------------------------------------")
