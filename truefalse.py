day = "Monday"
temperature = 30
raining = True

if day == "Monday" and temperature > 27 or not raining:
    print("Go swimming")
else:
    print("Learn Python")

print("-"*80)

name = input("Please enter your name: ")
#if name:
if name != "":
    print("Hello, {}".format(name))
else:
    print("Are you a man with no name?")