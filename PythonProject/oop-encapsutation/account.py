class Account:
    print("Insufficient fund transfer")


# Example usage
acc = Account()
acc.set_number("12345")
acc.set_account_type("Saving")
acc.set_balance(1000)
print("Account Number:", acc.get_number())
print("Account Type:", acc.get_account_type())
print("Balance:", acc.get_balance())

acc1 = Account()

# print("\nPerforming transactions:")
# acc.deposit(500)
# acc.withdrawal(2000)