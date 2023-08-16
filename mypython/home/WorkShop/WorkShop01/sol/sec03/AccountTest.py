from Account import Account

if __name__ == '__main__':
    account = Account("441-0290-1203", 500000, 7.3)

    print("계좌번호: " + account.getAccount() + " 잔액: " + str(account.getBalance()))
    account.deposit(20000)

    print("계좌번호: " + account.getAccount() + " 잔액: " + str(account.getBalance()))

    print("이자: " + str( account.calculateInterest() ) )