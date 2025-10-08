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


# Parent Class 1
class Engine:
    def start(self):
        print("Engine is starting...")

# Parent Class 2
class MusicSystem:
    def play_music(self):
        print("Playing music...")

    def start(self):
        print("Music system is starting...")

# Child Class (inherits from both)
class Car(Engine, MusicSystem):
    def drive(self):
        print("Car is now driving...")

# Usage
c = Car()
c.start()        # Which start() will it call?
c.play_music()   # Playing music...
c.drive()        # Car is now driving...

# Checking MRO
print(Car.mro())

# When we call c.start(), Python checks the order in which parents are inherited (left to right → Engine first, then MusicSystem