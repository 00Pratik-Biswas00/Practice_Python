class A:
    def method(self):
        print("A is called")

class B(A):
    def method(self):
        print("B is called")
    def method1(self):
        print("B from method 1 is called")

class C(A):
    def method(self):
        print("C is called")

class D(B,C):
    def method(self):
        print("D is called")

d = D()
d.method()
d.method1()

A.method(d)
B.method(d)


### Eval function

print(eval(input("Enter your expression: ")))

x=100
res = eval("x+y", {"x": x, "y":100})
print(res)