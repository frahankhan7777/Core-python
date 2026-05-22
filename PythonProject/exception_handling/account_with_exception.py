class InsufficientFundException(Exception):
    def __init__(self, msg):
        super().__init__(msg)



class account:
    def __init__(self):
        self.balance = 0
        self.count = 0

    def set_balance(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance


    def deposit(self,amount):

        if amount > 50000:
            raise InsufficientFundException("you cannat deposite more than 50000 at a time ")
        self.balance += amount
        print(f"Deposited: {amount}, Current Balance: {self.balance}")


    def withdrawal(self, amount):
        if amount < 20000:
            raise InsufficientFundException("you cannot withdrawal more than 20000 in a single transaction..")

        if self.count >= 2:
            raise InsufficientFundException("withdrawalll limlit excceede. maximum 3 withdrawall allow")

        if self.balance - amount >= 2000:
            self.balance -= amount
            self.count += 1
            print(f"withdew: {amount}, Remaining balance: {self.balance}")

        else:
            raise InsufficientFundException("Insufficient balance . minimum ")

acc = account()
acc.set_balance(50000)
print(acc.get_balance())


try:
    acc.deposit(2000)  # balance = 7000
    acc.withdrawal(3000)  # balance = 4000
    acc.withdrawal(2500)
    acc.withdrawal(21000)

except InsufficientFundException as e:
    print("exception:", e)