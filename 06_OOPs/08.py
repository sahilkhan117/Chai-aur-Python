# @property
# - make read only for a obj
# - call as a vaariable not a method without "()"

# read only attribute model

# @property is a built-in decorator that transforms a method within a class into a "property." This allows the method to be accessed and manipulated like a regular attribute, while still enabling the execution of custom logic (like validation, computation, or access control) when the attribute is accessed, modified, or deleted.

class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand

    def fullname(self):
        return f"This car is {self.__brand} {self.__model}"
    
    def fuel_type(self):
        return f"Deisel or Pertol"
    
    @staticmethod
    def general_decription():
        return f"Car are means of transpport"
    
    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return f"Electric Charge"


my_car = Car("Toyota", "Corolla")
my_new_car = ElectricCar("Tesla", "X", "85kWh")

# my_car.model = "City" # 🌟 no setter
# print(my_car.model) # 🌟 not callable
# print(my_car.model()) #  🌟 not callable as a method

print(my_car.model) 