class Account:
    def __init__(self):
        self.number = None
        self.accType = None
        self.balance = 00

    def set_number(self,number):
        self.number = number
    def get_number(self):
        return self.number

    def set_accType(self,accType):
        self.accType = accType
    def get_accType(self):
        return self.accType

    def set_balance(self,balance):
        self.balance = balance
    def get_balance(self):
        return self.balance

    # deposite function
    def deposite(self,amount):
        if amount > 200000:
            print("You can't deposite more then 2,00,000 in one time ")
        else:
            self.balance += amount
            print("The amount available after deposite is :", self.balance)

    # withdraw function
    count = 0
    def withdraw(self, amount):
        if Account.count > 4:
            print("Your daily withdraw limit is exeed")
        elif amount > 50000:
          print("You Can't withdraw more than 50,000 in one time")
        elif amount > self.balance:
            print("Insufficient amount.....")
        elif (self.balance - amount) > 2000:
            self.balance -= amount
            print("The amount available after withdraw is :", self.balance)
            Account.count += 1
        else:
            print("The amount is not sufficient as the minimum amount in the account should be 2000")


acc = Account()
acc.set_number(6265314244)
acc.set_accType("Saving")
acc.set_balance(15000)

print(acc.get_number())
print(acc.get_accType())
print(acc.get_balance())

acc.deposite(10000)
acc.withdraw(60000)
acc.withdraw(23000)

# acc.minimum(5000)

acc.deposite(500000)
acc.deposite(200000)

acc.withdraw(10000)
acc.withdraw(10000)
acc.withdraw(10000)
acc.withdraw(220000)
acc.withdraw(10000)
acc.withdraw(5500)
acc.withdraw(15000)


# def withdraw(self, amount):
#     if amount > 50000:
#         print("You Can't withdraw more than 50,000 in one time")
#     elif amount > self.balance:
#         print("Insufficient amount.....")
#     elif (self.balance - amount) > 2000:
#         self.balance -= amount
#         print("The amount available after withdraw is :", self.balance)
#     else:
#         print("The amount is not sufficient as the minimum am