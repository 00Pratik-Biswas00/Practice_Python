numbers = []
n = int(input("How many numbers do you want to enter? "))
sum=0
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

for num in numbers:
    if num%2 ==0:
        sum+=num

print(sum)