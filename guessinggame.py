import random
highest = 10
answer = random.randint(1, highest)
guess = int(input("Please guess a number between 1 and {}: ".format(highest)))

if guess == answer:
    print("You got it first time!!!")
else:
    while guess != answer:
        if guess>answer:
            print("Go lower")
        else:
            print("Go higher")
        guess = int(input())
        if guess == answer:
            print("You Got It")
        if guess == 0:
            print("Game Over")
            break
