# iterator
list1 = [1,2,3,4]
print(iter(list1))  # <list_iterator object at 0x00000270D4FCB3D0>

for i in iter(list1):
    print(i)

def func_square(n):
    for i in range(n):
        yield i**2

print(func_square(2)) # <generator object func_square at 0x000001BBA88EA4D0>

square = func_square(3)
for i in square:
    print(i)
