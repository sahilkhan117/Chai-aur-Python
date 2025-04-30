# Basic Classes and Object
# Create a car classs with attributes like model, brand. make a insatnce


# 🌟 Class 🍚>📥📐 -> 📤📐>🍙 : SBI Genelized form
class Car:

    # 🌟 Constructer (__init__): run immidiately after making a object
    # 🌟 self ☎️📞: Connect Class with each object seprately (remember who call you)
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


# 🌟 Object🍙: user / product 
my_car = Car("Tesla", "S")
print(my_car.model)

my_new_car = Car("Tesla", "X")
print(my_new_car.model)