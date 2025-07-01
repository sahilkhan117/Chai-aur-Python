# Static method

# only accessed by class general decription

# 🔐 a static method is a method that belongs to a class but does not operate on instances of that class. It is defined using the @staticmethod decorator. 
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
    
    @staticmethod
    def general_decription():
        return f"Car are means of transpport"
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return f"Electric Charge"


my_car = Car("Toyota", "Corolla")
my_new_car = ElectricCar("Tesla", "X", "85kWh")

print("My Car "+ my_car.general_decription())
print("Car "+ Car.general_decription())