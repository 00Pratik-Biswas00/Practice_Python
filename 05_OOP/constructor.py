class Animal:
    def __init__(self, type):
        self.type = type
    def __init__(self, type, age):
        self.type = type
        self.age = age

# animal = Animal("dog")
# print(animal) # Animal.__init__() missing 1 required positional argument: 'age'

animal = Animal("dog", 10)
print(animal.age)


# not a good practice
class Veg:
    def __init__(self, *args):
        if len(args)==1:
            self.type=args[0]
        elif len(args)==2:
            self.type=args[0]
            self.age=args[1]

veg1 = Veg("bird")
print(veg1.type)