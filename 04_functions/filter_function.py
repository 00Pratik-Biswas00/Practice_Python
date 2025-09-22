def even(num):
    if num%2==0:
        return True
    
l = [1,2,3,42,34,45,54,56,90]

print(list(filter(even, l))) # filter(function, iterable)

print(list(filter(lambda num:num%2==0, l)))