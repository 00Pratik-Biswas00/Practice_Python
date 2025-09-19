# second largest element
arr = [12, 35, 1, 10, 34, 1]

largest = second_largest = float('-inf')

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num < largest and num > second_largest:
        second_largest = num
    else:
        second_largest = -1

print(second_largest)
