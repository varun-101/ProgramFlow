name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

# if age >= 18:
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# elif age == 900:
#     print("Immortal Soldier") #else if
# else:
#     print("Please come back in {0} years".format(18-age))

if age < 18:
    print("Please come back in {0} years".format(18-age))
elif age == 900:
    print("Immortal soldier")
else:
    print("You are old enough to vote")
    print("Please put an X in the box")