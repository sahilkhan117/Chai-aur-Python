# find duplicate in a list if found exit the loop and print duplicate

items = ["apple", "banana", "orange", "apple", "mango"]
unique_item = set()

for i in items:
    if i in unique_item:
        print("duplicate:", i)
        break
    unique_item.add(i)