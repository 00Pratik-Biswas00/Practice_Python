# n = 5
# for i in range(1,11):
    # print(n*i, end=" ")

# s = "DoctorPhenomenal"
# for letter in range(0, len(s), 2):
#     print(s[letter], end="")

# x=3
# while x>=0:
#     print(x, end=" ")
#     x-=1

# x=10
# num=1
# while num**2 <=10:
#     print(num**2, end=" ")
#     num+=1

# n = -3
# if n==0:
#     print("already zero")

# while n!=0:
#     if n>0:
#         print(n-1, end=" ")
#         n-=1
#     elif n<0:
#         print(n, end=" ")
#         n+=1

# n=15
# def isPrime(num):
#     is_prime=True
#     for i in range(2,num):
#         if num%i==0:
#             is_prime = False
#             break
    
#     return is_prime

# while n<=500:
#     if(isPrime(n+1)):
#         print(n+1)
#         break
#     n+=1

# n = 4

# if n == 0:
#     ans = 0
# elif n == 1:
#     ans = 1
# else:
#     prev, curr = 0, 1
#     for i in range(2, n+1):
#         nxt = prev + curr
#         ans = nxt
#         prev, curr = curr, nxt

# print(ans)

# n=4
# arr=[3,23,30,45]
# res = 1
# for nums in arr:
#     res *= nums
# str_res = str(res)

# for s in range(len(str_res)-1, -1, -1):
#     if(str_res[s]!='0'):
#         print(str_res[s])
#         break

# count = 0
# while count < 5:
#    print("Count:", count)
#    count += 1
#    if count == 3:
#        continue
#    print("After Continue")

def outer():
    x = 10
    def inner():
        nonlocal x
        x += 5
        return x
    return inner

closure = outer()
print(closure())
print(closure())


