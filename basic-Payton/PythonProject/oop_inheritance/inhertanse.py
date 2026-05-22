class Account:
    def __init__(self):
        self.accountHolder = ''
        self.balance = 0

    def setAccountHolder(self, name):
        self.accountHolder = name

    def getAccountHolder(self):
        return self.accountHolder

    def deposit(self, amount):
        self.balance += amount

    def getBalance(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self):
        super().__init__()   # 👈 parent constructor call
        self.interestRate = 0

    def setInterestRate(self, rate):
        self.interestRate = rate

    def getInterestRate(self):
        return self.interestRate

    def addInterest(self):
        self.balance += self.balance * self.interestRate / 100


# object create
acc = SavingsAccount()

acc.setAccountHolder("Rahul")
acc.deposit(1000)
acc.setInterestRate(5)
acc.addInterest()

print("Account Holder:", acc.getAccountHolder())
print("Balance:", acc.getBalance())
print("Interest Rate:", acc.getInterestRate())