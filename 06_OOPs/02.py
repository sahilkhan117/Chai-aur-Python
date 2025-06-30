# Methode and self
# make a methoded display full name

# Basic Classes and Object
# Create a car classs with attributes like model, brand. make a insatnce
# 🌟 Class 🍚>📥📐 -> 📤📐>🍙 : SBI Genelized form

# 🌟 Constructer (__init__): run immidiately after making a object
# 🌟 self ☎️📞: Connect Class with each object seprately (remember who call you)

class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # self 🌟: seprate each obj
    # Method 🌟: own by class used by obj
    def fullname(self):
        return f"This car is {self.brand} {self.model}"

my_car = Car("Tesla", "S")
print(my_car.model)
print(my_car.fullname())


my_new_car = Car("Tesla", "X")
print(my_new_car.model)