# suggets best pet food Based on Pet's Species and Age.
# e.g.: 

Pet = "Dog"
species = "Puppy"
Age = 2

Food_types = {
    "Dog": {
        "Puppy": {2: "puppy Food", 5: " big Puppy Food", 100: None},
        ...: ...
    },
    "Cat": {
        "Cute": {5: "Junior Cat Food", 100: "Senior cat Food" },
        ...: ...
    },
    ...: ...
}

for f in Food_types[Pet][species]:
    suggestion = Food_types[Pet][species][f]
    if Age < f:
        break

print("Best Food For Your pet is :", suggestion)