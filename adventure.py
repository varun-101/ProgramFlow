available_exits = ["north","south", "east", "west"]
chosen_exit = ""

while chosen_exit not in available_exits:
    chosen_exit = input("Please enter a direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game Over")
        break
print("Aren't you glad you are out")