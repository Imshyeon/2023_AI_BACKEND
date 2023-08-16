from dataclasses import make_dataclass

IChange = make_dataclass("IChange", fields=[], bases=(), namespace={"charge": lambda self, time: None})

Mobile = make_dataclass(
    "Mobile",
    fields=[("mobileName", str), ("batterySize", int), ("osType", str)],
    bases=(),
    namespace={"operate": lambda self, time: None},
)

LTab = make_dataclass(
    "LTab",
    bases=(Mobile, IChange),
    fields=[],
    namespace={
        "charge": lambda self, time: setattr(self, "batterySize", self.batterySize + time * 10),
        "operate": lambda self, time: setattr(self, "batterySize", self.batterySize - time * 10),
    },
)

OTab = make_dataclass(
    "OTab",
    bases=(Mobile, IChange),
    fields=[],
    namespace={
        "charge": lambda self, time: setattr(self, "batterySize", self.batterySize + time * 8),
        "operate": lambda self, time: setattr(self, "batterySize", self.batterySize - time * 12),
    },
)

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
