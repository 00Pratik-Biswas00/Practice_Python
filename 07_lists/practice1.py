arr =  [54, 43, 2, 1, 5]

# for item in arr:
#     print(item-1, end=" ")

# max and min element's index

# print(arr.index(max(arr)))
# print(arr.index(min(arr)))

# seperate even odd

# even_list = []
# odd_list = []
# for num in arr:
#     if(num%2==0):
#         even_list.append(num)
#     else:
#         odd_list.append(num)

# print("even:", *even_list, "odd:", *odd_list)

# flatten a list

a = [1, [2, 3], [4, [5, 6]]]  

# Recursive function to flatten list  
def flatten(a):  
    res = []  
    for x in a:  
        if isinstance(x, list):  
            res.extend(flatten(x))  
        else:  
            res.append(x) 
    return res  

print(flatten(a))