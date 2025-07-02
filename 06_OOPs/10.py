# Multiple inheritence

# Multiple inheritance in Python allows a class to inherit from two or more parent classes, combining their attributes and methods. This enables a child class to acquire functionalities from multiple sources, promoting code reusability and allowing for the modeling of complex relationships between objects.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

class Battery:
    def battery_info(self):
        return f"This is battery"

class Engine:
    def engine_info(self):
        return f"This is engine"

class EVCar(Battery, Engine, Car):
    pass

my = EVCar("Tesla", "Model S")

print(my.battery_info())
print(my.engine_info())