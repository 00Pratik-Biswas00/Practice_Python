x = "global x"   # Global

def outer():
    # x = "enclosing x"   # Enclosing
    
    def inner():
        x = "local x"   # Local
        print(x)        # Python picks "local x"
    
    inner()
    print(x)            # Python picks "enclosing x"

outer()
print(x)                # Python picks "global x"
print(len("abc"))       # Built-in


x = 10   # global

def outer2():
    y = 20   # enclosing
    
    def inner2():
        nonlocal y   #with this we can now mdify the enclosing scope variable
        global x     #with this we can now mdify the enclosing scope variable
        y += 1   # modifies enclosing y
        x += 1   # modifies global x
        print("y:", y, "x:", x)
    
    inner2()

outer2()
print("Final global x:", x)



def make_multipliers():
    funcs = []
    for i in range(1, 4):
        def multiplier(x):
        # def multiplier(x, i=i):
            return x * i
        funcs.append(multiplier)
    return funcs

f1, f2, f3 = make_multipliers()

print(f1(2))  # Expect 2*1 = 2, but gets 6
print(f2(2))  # Expect 2*2 = 4, but gets 6
print(f3(2))  # Expect 2*3 = 6, gets 6