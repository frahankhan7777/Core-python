#_______ATM__________


blance = 10000
pin = 123456


print("=====WELCOME TO ATM======")

user_pin = int(input("ENTER YOUR PIN"))

if user_pin == pin:
    while True:
        print("\n1. CHECK YOUR BALANCE" )
        print("2. DEPOSIT MONEY")
        print("3. WITHDRAW MONEY")
        print("4. EXIT")


        choice = input ("ENTER  YOUR CHOICE>")

        if choice =="1":
            print("YOUR BALANCE IS : ", blance)

        elif choice =="2":
            amount = int(input("ENTER DEPOSIT MONEY"))
            blance += amount
            print("MONEY DEPOSIT SUCCFULL:")
            print("NEW BALANCE :", blance)

        elif choice =="3":
            amount = int(input("ENTER YOUR WITHDRAW AMOUNT:"))

            if amount <= blance:
               blance -= amount
               print("PLEASE COLLECT YOUR CASH")
               print("REMAINING BLANCE :", blance)

            else:
               print("INSUFFICIENT BALANCE")

        elif choice == "4":
                print("Thank You For Using ATM")
                break

        else:
            print("INVALID CHOISE")

else:
    print("WRONG PIN")