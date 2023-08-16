from dataclasses import dataclass, make_dataclass,field

ICharge = make_dataclass('ICharge',
                         fields=[],
                         namespace={'charge': lambda self, time : None})

Mobile = make_dataclass('Mobile',
                        [('mobileName',int),
                        ('batterySize', int),
                        ('osType',int)],
                        namespace={'operate' : lambda self, time : None})

Ltab = make_dataclass('Ltab',
                      bases=(Mobile,ICharge),
                      fields=[],
                      namespace={
                          'operate' : lambda self, time : setattr(self,'batterySize',self.batterySize - time * 10),
                          'charge' : lambda self, time : setattr(self, 'batterySize',self.batterySize + time * 10)
                      })

Otab = make_dataclass('Otab',
                      bases=(Mobile,ICharge),
                      fields=[],
                      namespace={
                          'operate' : lambda self, time : setattr(self,'batterySize',self.batterySize - time * 12),
                          'charge' : lambda self, time : setattr(self, 'batterySize',self.batterySize + time * 8)
                      })

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