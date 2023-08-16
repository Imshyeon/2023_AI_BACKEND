class Account:
    def __init__(self, account="", balance=0, interestRate=0.0):
        self.__account = account
        self.__balance = balance
        self.__interestRate = interestRate

    def setAccount(self, account):
        self.__account = account

    def getAccount(self):
        return self.__account

    def getBalance(self):
        return self.__balance

    def calculateInterest(self):
        interest = self.__balance * (self.__interestRate / 100)
        return interest

    def deposit(self, money):
        self.__balance += money

    def withdraw(self, money):
        self.__balance -= money
