# polymorphism

# same methodes in both of the classes but that one is more appropriate or nearest can only execute 

# 🚀 Polymorphism in Python, derived from Greek words meaning "many forms," is a core concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common type. This enables a single interface to represent different underlying forms, promoting code reusability and flexibility. 

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand

    def fullname(self):
        return f"This car is {self.__brand} {self.model}"
    
    def fuel_type(self): # for Car
        return f"Deisel or Pertol"
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self): # for ElectricCar
        return f"Electric Charge"


my_car = Car("Toyota", "Corolla")
my_new_car = ElectricCar("Tesla", "X", "85kWh")

print(my_car.fuel_type())
print(my_new_car.fuel_type())