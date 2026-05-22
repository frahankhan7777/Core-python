
def SumNum(a ,*args):
    total = 0
    for num in args:
        total += num
    return total

total=SumNum(1, 2, 3, 4, 5)
print("The total is:", total)
