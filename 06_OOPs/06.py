# Class Variable

# In Python, a class variable (also known as a class attribute or static variable) is a variable that is owned by the class itself, rather than by any specific instance (object) of that class. This means that all instances of a class share the same copy of a class variable.

class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand

    def fullname(self):
        return f"This car is {self.__brand} {self.model}"
    
    def fuel_type(self):
        return f"Deisel or Pertol"
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return f"Electric Charge"


my_car = Car("Toyota", "Corolla")
my_new_car = ElectricCar("Tesla", "X", "85kWh")
Car("Toyota", "Corolla")
Car("Toyota", "Corolla")
Car("Toyota", "Corolla")
Car("Toyota", "Corolla")
Car("Toyota", "Corolla")
Car("Toyota", "Corolla")

print(my_car.fuel_type())
print(my_new_car.fuel_type())

# Acess class variable
print("Total Cars:" , Car.total_car)