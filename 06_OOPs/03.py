# Inheritence

# 👇🏻👇🏻⬇️⬇️
# Inheritance allows us to define a class that inherits all the methods and properties from another class.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fullname(self):
        return f"This car is {self.brand} {self.model}"
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size # 🌟New Attribute


# 👇🏻👇🏻⬇️⬇️
# my_car = Car("toyota", "corolla")
# print(my_car.model)
# print(my_car.fullname())

my_new_car = ElectricCar("Tesla", "X", "85kWh")
print(my_new_car.fullname())