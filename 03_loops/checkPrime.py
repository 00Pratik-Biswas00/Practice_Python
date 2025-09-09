number = int(input("Enter number: "))

is_prime = True
if number == 1:
    is_prime=False
for num in range(2,number):
    if number % num ==0:
        is_prime=False
        break

if is_prime == True:
    print("Prime")
else:
    print("not prime")
