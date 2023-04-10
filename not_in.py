activity = input("What would you like to do today? ")

if "cinema" not in activity:
     print("But i want to go to the cinema today")

print("-"*80)

if "cinema" not in activity.casefold():
    print("But I want to go to the cinema today")