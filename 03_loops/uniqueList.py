number_of_items = int(input("Enter number of items: "))
item_list = []
for item in range(number_of_items):
    item_name = input(f"Enter {item+1} item: ")
    item_list.append(item_name)
print(item_list)

is_unique = True
for item in item_list:
    if item_list.count(item)>1:
        print(item)
        is_unique = False
        break
if is_unique:
    print("All items are unique")

unique_item = set()
for item in item_list:
    if item in unique_item:
        print(item)
        break
    else:
        unique_item.add(item)
        