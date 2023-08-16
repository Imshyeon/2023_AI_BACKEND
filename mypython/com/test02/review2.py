from dataclasses import dataclass

class ICharge:
    def charge(self,time):
        pass

@dataclass
class Mobile:
    mobileName : str =""
    batterySize : int = 0
    osType : str =""

    def operate(self,time):
        pass


@dataclass
class Ltab(Mobile,ICharge):
    def operate(self,time):
        usedAmount = time * 10
        self.batterySize -= usedAmount
        return self.batterySize

    def charge(self,time):
        chargedAmount = time * 10
        self.batterySize += chargedAmount
        return self.batterySize


@dataclass
class Otab(Mobile, ICharge):
    def operate(self, time):
        usedAmount = time * 12
        self.batterySize -= usedAmount
        return self.batterySize

    def charge(self, time):
        chargedAmount = time * 8
        self.batterySize += chargedAmount
        return self.batterySize

if __name__ == '__main__':
    m1 = Ltab("Ltab", 500, "AP-01")
    m2 = Otab("Otab", 1000, "AND-20")
    print(f'Mobile\t\tBattery\t\tOS')
    print(f'---------------------------------------')
    print(f'{m1.mobileName}\t\t{m1.batterySize}\t\t\t{m1.osType}')
    print(f'{m2.mobileName}\t\t{m2.batterySize}\t\t{m2.osType}')
    print(f'---------------------------------------')
    print()

    m1.charge(10)
    m2.charge(10)
    print('10분 충전')
    print(f'Mobile\t\tBattery\t\tOS')
    print(f'---------------------------------------')
    print(f'{m1.mobileName}\t\t{m1.batterySize}\t\t\t{m1.osType}')
    print(f'{m2.mobileName}\t\t{m2.batterySize}\t\t{m2.osType}')
    print(f'---------------------------------------')
    print()

    m1.operate(5)
    m2.operate(5)
    print('5분 통화')
    print(f'Mobile\t\tBattery\t\tOS')
    print(f'---------------------------------------')
    print(f'{m1.mobileName}\t\t{m1.batterySize}\t\t\t{m1.osType}')
    print(f'{m2.mobileName}\t\t{m2.batterySize}\t\t{m2.osType}')
    print(f'---------------------------------------')