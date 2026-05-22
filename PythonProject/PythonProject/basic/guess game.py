secrets = 10
chance = 3
while chance > 0:
    guess = int(input("number dalo"))
    if guess == secrets:
        print("right ans")
        break
    else:
        print("wrong ans")
        chance -= 1
        if chance == 0:
            print("game over")