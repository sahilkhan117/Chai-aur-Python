# Encapsulation
# some of the obj variables not directly acessed by obj but acssed by a Getter Methode

# Encapsulation is a concept of wrapping data (variables) and code acting on the data (methods) together as a single unit.

# 🌟 the "__brand"  > "__" shows that this is a private variable only accessed by class
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand

    def fullname(self):
        return f"This car is {self.__brand} {self.model}"
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_new_car = ElectricCar("Tesla", "X", "85kWh")
# print(my_new_car.__brand) #🌟remove the access
print(my_new_car.get_brand())