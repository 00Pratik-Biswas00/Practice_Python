class Car:
    def __init__(self, car_name, car_model):
        self.name = car_name
        self.model = car_model

    def brand_with_model(self):
        return f"{self.name} -  {self.model}"




my_car1 = Car("Toyota", "Corolla")
my_car2 = Car("Tata", "Safari")

print(my_car1.name)
print(my_car2.model)
print(my_car2.brand_with_model())

