class Car():
    def __init__(self, model):
        self.model = model
    def __str__(self):  #2
        return "New model is created"
    
c1 = Car("Safari")
print(c1)   # <__main__.Car object at 0x0000021A55FA70E0> m-- memory created at the location of "0x0000021A55FA70E0" (default __str__ method)

print(c1) #2 overriding the __str__ magic method

print(dir(c1))
    