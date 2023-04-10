shopping = ["milk", "pasta", "bread", "spam", "rice", "eggs"]

item_to_find = input("Please enter the item ")
found_at = None
# for s in range(len(shopping)):
#     if shopping[s] == item_to_find:
#         print("Item found at position {}".format(s+1))
#         p = 1
#         break
if item_to_find in shopping:
    found_at = shopping.index(item_to_find)

if found_at is not None:
    print("Item found at position {}".format(found_at+1))
else:
    print("{} not found".format(item_to_find))