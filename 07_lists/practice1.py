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

# a = [1, [2, 3], [4, [5, 6]]]  

# # Recursive function to flatten list  
# def flatten(a):  
#     res = []  
#     for x in a:  
#         if isinstance(x, list):  
#             res.extend(flatten(x))  
#         else:  
#             res.append(x) 
#     return res  

# print(flatten(a))

lst = [1, 2, 3]
lst = lst * 0
# lst = 99
print(lst)


t=(1,2,[3,4])
t[2][0]= 99
print(t)
print(t+(4,5))


print(tuple('abc'))

tu = (1,2,3,4,2)
print(tu.index(2,2))