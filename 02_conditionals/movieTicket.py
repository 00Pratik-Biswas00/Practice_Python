enter_age = int(input("Enter age: "))
enter_day = input("Enter day: ")

price = 12 if enter_age >=18 else 8
if enter_day == "wednesday":
    price-=2

print(f"Ticket price - {price}")