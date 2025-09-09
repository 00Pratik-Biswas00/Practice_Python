def even_num_gen(limit):
    for i in range(2, limit+1, 2):
        print(i)
even_num_gen(10)

def even_num_gen_with_yield(limit):
    for i in range(2, limit+1, 2):
        yield i

for num in even_num_gen_with_yield(10):
    print(num)

# fibonacci

def fib(number):
    a,b = 0,1
    for _ in range(number):
        yield a
        a, b = b, a+b

for num in fib(5):
    print(num, end=" ")