# isinstance(obj, class)

# The isinstance(obj, classinfo) function in Python is a built-in function used to check if an object obj is an instance of a specified class or type, or an instance of a subclass of that class or type. 

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

print(isinstance(my_new_car, ElectricCar))
# true
print(isinstance(my_new_car, Car))
# true