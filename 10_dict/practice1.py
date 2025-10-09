import random


# 1

expenses = {
    "food": 2500,
    "transport": 800,
    "entertainment": 1200,
    "bills": 2200,
    "misc": 500
}
res_key = [key for key, val in expenses.items() if val==max(expenses.values())]
print(f"Key - {res_key[0]}, val - {max(expenses.values())}")

# 2

emails = [
    "pratik@gmail.com",
    "ayaan@yahoo.com",
    "karan@gmail.com",
    "chandrima@outlook.com",
    "dev@yahoo.com"
]

my_dict = {}
for mail in emails:
    domain = mail.split('@')[1]
    my_dict.setdefault(domain, []).append(mail)

print(my_dict)

# 3
marks = {
    "Ayaan": [85, 90, 88],
    "Chandrima": [78, 82, 89],
    "Riya": [92, 88, 95]
}

for name, numbers in marks.items():
    print(f"{name}:{round(sum(numbers)/len(numbers), 2)}")


print("\n\n")

# 4 
cart = {
    "Shirt": {"price": 1200, "qty": 2},
    "Shoes": {"price": 2500, "qty": 1},
    "Jeans": {"price": 1800, "qty": 1}
}
res = 0
for items in cart.values():
    res += items["price"] * items["qty"]
print(res)

# 5
players = ["Ayaan", "Chandrima", "Pratik", "Riya"]
print(random.choice(players))

