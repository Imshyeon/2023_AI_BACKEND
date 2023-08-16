from dataclasses import dataclass

class IChange:
    def charge(self, time):
        pass

@dataclass
class Mobile:
    mobileName: str = ""
    batterySize: int = 0
    osType: str = ""

    def operate(self, time):
        pass

@dataclass
class LTab(Mobile, IChange):
    def charge(self, time):
        chargedAmount = time * 10
        self.batterySize += chargedAmount
        return self.batterySize

    def operate(self, time):
        usedAmount = time * 10
        self.batterySize -= usedAmount
        return self.batterySize

@dataclass
class OTab(Mobile, IChange):
    def charge(self, time):
        chargedAmount = time * 8
        self.batterySize += chargedAmount
        return self.batterySize

    def operate(self, time):
        usedAmount = time * 12
        self.batterySize -= usedAmount
        return self.batterySize

if __name__ == "__main__":
    lt = LTab("LTab", 500, "AP-01")
    ot = OTab("OTab", 1000, "AND-20")

    print("  Mobile\t\tBattery\t\tOS")
    print("---------------------------------------------")
    print(f"{lt.mobileName}\t\t{lt.batterySize}\t\t{lt.osType}")
    print(f"{ot.mobileName}\t\t{ot.batterySize}\t\t{ot.osType}")
    print("---------------------------------------------")
    print()

    print("10 충전      ")
    lt.charge(10)
    ot.charge(10)
    print("  Mobile\t\tBattery\t\tOS")
    print("---------------------------------------------")
    print(f"{lt.mobileName}\t\t{lt.batterySize}\t\t{lt.osType}")
    print(f"{ot.mobileName}\t\t{ot.batterySize}\t\t{ot.osType}")
    print("---------------------------------------------")
    print()

    print("5분 통화 ")
    lt.operate(5)
    ot.operate(5)
    print("  Mobile\t\tBattery\t\tOS")
    print("---------------------------------------------")
    print(f"{lt.mobileName}\t\t{lt.batterySize}\t\t{lt.osType}")
    print(f"{ot.mobileName}\t\t{ot.batterySize}\t\t{ot.osType}")
    print("---------------------------------------------")
