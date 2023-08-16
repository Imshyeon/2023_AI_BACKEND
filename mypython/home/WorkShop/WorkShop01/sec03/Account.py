class Account:
    def __init__(self,a,b,i) -> None:
        super().__init__()
        self.__a=str(a)
        self.__b=int(b)
        self.__i=float(i)

    def setAccount(self,a):
        self.__a=str(a)

    def getAccount(self):
        return self.__a

    def getBalance(self):
        return self.__b

    def calculateInterest(self):
        interest = self.__b * self.__i / 100
        interest = round(interest,1)
        return interest

    def deposit(self,money):
        self.__b = self.__b + money


    def withdraw(self,money):
        if self.__b - money < 0:
            return '잔액 부족'
        else:
            self.__b = self.__b - money
            #self.__b -= money 랑 같은 코드


class AccountTest():
    def main(self,*args):
        m1=Account('441-0290-1203',500000,7.3)
        print(f'계좌정보: {m1.getAccount()} 현재잔액: {m1.getBalance()}')
        m1.deposit(20000)
        print(f'계좌정보: {m1.getAccount()} 현재잔액: {m1.getBalance()}')
        print(f'이자: {m1.calculateInterest()}')