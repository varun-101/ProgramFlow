age = int(input("Please enter your age: "))

#if age > 15 and age < 66:
if 15 < age < 66:
    print("Have a good day at work")
else:
    print("Enjoy your free time")

print("-"*80)

if age<16 or age>65:
    print("Enjoy your free time")
else:
    print("Have a good day at work")