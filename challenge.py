name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if 17<age<31:
    print("Hello {}, we hope you enjoy your holiday".format(name))
else:
    print("No holiday for you sucker")