enter_age = int(input("Enter your age: "))
if enter_age < 13:
    print("Child")
elif enter_age > 13 and enter_age < 19:
    print("Teenager")
elif enter_age > 20 and enter_age < 59:
    print("Adult")
else:
    print("Senior")