import collections
# arr =  [54, 43, 2, 1, 5]

# for item in arr:
#     print(item-1, end=" ")

# max and min element's index

# print(arr.index(max(arr)))
# print(arr.index(min(arr)))




# seperate even odd ------------

# even_list = []
# odd_list = []
# for num in arr:
#     if(num%2==0):
#         even_list.append(num)
#     else:
#         odd_list.append(num)

# print("even:", *even_list, "odd:", *odd_list)




# flatten a list ------------

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


# 4 ------------
# lst = [1, 2, 3]
# lst = lst * 0
# # lst = 99
# print(lst)

# 5 ------------
# t=(1,2,[3,4])
# t[2][0]= 99
# print(t)
# print(t+(4,5))


# print(tuple('abc'))

# tu = (1,2,3,4,2)
# print(tu.index(2,2))

# 6 ------------

# transactions = [
#     ("deposit", 2000),
#     ("withdraw", 500),
#     ("deposit", 1200),
#     ("withdraw", 700),
# ]

# balance = 0
# for transaction in transactions:
#     if transaction[0] == "deposit":
#         balance+=transaction[1]
#     elif transaction[0] == "withdraw":
#         balance-=transaction[1]
#     else:
#         print("Wrong command")

# print(balance)

# 7 -------------

# invoices = [
#     {"id": 101, "amount": 1200},
#     {"id": 102, "amount": 3400},
#     {"id": 103, "amount": 1500}
# ]

# print(sum(invoive["amount"] for invoive in invoices))


# 8 -------------

grades = ["A", "B", "A", "C", "B", "A", "D", "C"]
print(dict(collections.Counter(grades)))