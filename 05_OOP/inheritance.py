from basic_class import Car


class Electric_Car(Car):
    def __init__(self, car_name, car_model, car_battery):
        super().__init__(car_name, car_model)
        self.battery = car_battery

my_electric_car = Electric_Car("Tesla", "Model S", "85kwh")

print(my_electric_car.name)
print(my_electric_car.brand_with_model())