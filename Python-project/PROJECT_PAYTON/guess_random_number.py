import random

number = random.randint(1,10)
print("CHOSEE 1 TO 10 ANY NUMBER ")

while True:

    guess = input("your guess number >>>")
    guess = int(guess)

    if guess == number:
        print("congratulation you win")
        break

    elif guess < number:
        print("kuch badha socho,")

    else:
        print("kuch chota soch ho")