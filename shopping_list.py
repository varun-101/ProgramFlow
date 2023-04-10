shopping = ["milk", "pasta", "bread", "spam", "rice", "eggs"]

for items in shopping:
    if items == "spam":
        continue

    print(items)

for items in shopping:
    if items == "spam":
        break

    print(items)