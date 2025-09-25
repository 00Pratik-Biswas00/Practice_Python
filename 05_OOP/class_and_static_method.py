import datetime
now = datetime.datetime.now()
class Car:
    base_price = 100000 # class variable
    def __init__(self, model):
        self.model = model
    @classmethod # class method
    def updated_base_price(cls, inflation): # cls is the keyword to access the class variables
        cls.base_price = cls.base_price + (cls.base_price*inflation)//100

    @staticmethod
    def check_year():
        if now.year == 2025:
            return True
        else:
            return False


car1 = Car("Safari")    
# print(car1.base_price)
# print(Car.base_price)

if(car1.check_year()):
    print("Price is already updated")
else:
    Car.updated_base_price(10)

print(Car.base_price)