def odd_even(num):
    if num%2==0:
        return f"{num} is even."
    else:
        return f"{num} is odd."
    
l = [1,2,3,42,34,45,54,56,90]

print(list(map(odd_even, l))) # map(function, iterable)