
while True:
    num1 = input("inter first calculation ==")
    if num1 == 'quit':
        break

    op = input("op (+, -, /, *) ==")

    if op == 'quit':
        break

    num2 = input("inter 2 number ==")

    if num2 == 'quit':
        break

    n1 = float(num1)
    n2 = float(num2)

    if op == "+":
        result = n1 + n2
        print(result)

    elif op == '-':
        result = n1 - n2
        print(result)

    elif op == '/':
        result = n1 / n2
        print(result)

    elif op == '*':
        result = n1 * n2
        print(result)

    else:
        print("wrong op")

print("")


