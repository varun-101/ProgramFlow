low = 1
high = 1000

print("Please think of a number between 1 and 1000 ")
input("Press ENTER to start")
guess = 0
guesses = 1

while low != high:
    guess += 1
    guesses = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower?"
                     "Enter h or l, or c if my guess is correct"
                     .format(guesses)).casefold()
    if high_low == "h" :
        low = guesses + 1
    elif high_low == "l" :
        high = guesses - 1
    elif high_low == "c":
        print("I got it in {} guesses".format(guess))
        break
    else:
        print("Enter h, l, or c")
else:
    print("You thought of the number {}".format(low))
    print("I got it in {} guesses".format(guess))